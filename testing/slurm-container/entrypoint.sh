#!/bin/bash
# Start munge, slurmctld, slurmd and slurmrestd (JWT) in one container.
set -euo pipefail

# Node definition from the actual container resources
NODE_LINE=$(slurmd -C | head -1 | sed -E 's/^NodeName=[^ ]+/NodeName=localhost/; s/ UpTime=.*//')
MEM=$(echo "$NODE_LINE" | sed -E 's/.*RealMemory=([0-9]+).*/\1/')
NODE_LINE=$(echo "$NODE_LINE" | sed -E "s/RealMemory=[0-9]+/RealMemory=$((MEM * 9 / 10))/")
sed -i "s|^@NODE@|${NODE_LINE} State=UNKNOWN|; s|^@PARTITIONS@|PartitionName=debug Nodes=localhost Default=YES MaxTime=INFINITE State=UP\nPartitionName=batch Nodes=localhost MaxTime=INFINITE State=UP|" /etc/slurm/slurm.conf

# Keys (fresh per container)
[ -f /etc/munge/munge.key ] || { mkdir -p /etc/munge; dd if=/dev/urandom bs=1024 count=1 of=/etc/munge/munge.key 2>/dev/null; }
chown -R munge:munge /etc/munge /run/munge; chmod 0400 /etc/munge/munge.key
KEY=/var/spool/slurmctld/jwt_hs256.key
[ -f $KEY ] || dd if=/dev/urandom bs=32 count=1 of=$KEY 2>/dev/null
chown slurm:slurm $KEY; chmod 0600 $KEY

su -s /bin/sh munge -c "/usr/sbin/munged"
slurmctld
for _ in $(seq 30); do scontrol ping 2>/dev/null | grep -q UP && break; sleep 1; done
slurmd
# slurmrestd unshares IPC/file namespaces as hardening; an unprivileged container
# can't, so disable that here (test container only) instead of needing --privileged.
# Only openapi/slurmctld: there is no accounting database (slurmdbd) in this container.
SLURM_JWT=daemon SLURMRESTD_SECURITY=disable_unshare_sysv,disable_unshare_files setpriv --reuid="$(id -u slurmrest)" --regid="$(id -g slurmrest)" --clear-groups \
    slurmrestd -a rest_auth/jwt -s openapi/slurmctld 0.0.0.0:6820 >> /var/log/slurm/slurmrestd.log 2>&1 &

echo "Slurm test cluster up: slurmrestd on :6820 (JWT). Token: scontrol token username=testuser"
# Keep running; show logs on stop
trap 'kill $(jobs -p) 2>/dev/null; exit 0' TERM INT
tail -F /var/log/slurm/slurmctld.log /var/log/slurm/slurmrestd.log &
wait
