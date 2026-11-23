#!/bin/bash
# Build (if needed) and start the single-node Slurm test container, then set the
# environment variables the proxy client needs.
#
#   source testing/slurm-container/start.sh     # exports PROXY_SLURM_API_URL, SLURM_JWT, SLURM_USER
#
# Env: SLURM_TEST_PORT (default 6821), SLURM_TEST_NAME (default testslurm),
#      SLURM_TEST_IMAGE (default slurm-cli-proxy-test), SLURM_TEST_REBUILD=1 to force a build.
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PORT="${SLURM_TEST_PORT:-6821}"
NAME="${SLURM_TEST_NAME:-testslurm}"
IMAGE="${SLURM_TEST_IMAGE:-slurm-cli-proxy-test}"

if [ "${SLURM_TEST_REBUILD:-0}" = 1 ] || ! docker image inspect "$IMAGE" >/dev/null 2>&1; then
    echo "Building $IMAGE (compiles Slurm, takes a few minutes the first time)..."
    docker build -t "$IMAGE" "$HERE" || return 1 2>/dev/null || exit 1
fi

if [ -z "$(docker ps -q -f name="^${NAME}$")" ]; then
    docker rm -f "$NAME" >/dev/null 2>&1
    docker run -d --name "$NAME" --hostname localhost -p "${PORT}:6820" "$IMAGE" >/dev/null || return 1 2>/dev/null || exit 1
fi

echo -n "Waiting for Slurm"
for _ in $(seq 60); do
    docker exec "$NAME" scontrol ping 2>/dev/null | grep -q UP && curl -s -o /dev/null "http://localhost:${PORT}/" && break
    echo -n "."; sleep 2
done
echo

export PROXY_SLURM_API_URL="http://localhost:${PORT}"
export SLURM_USER=testuser
export "$(docker exec "$NAME" scontrol token username=testuser lifespan=86400)"
echo "PROXY_SLURM_API_URL=$PROXY_SLURM_API_URL SLURM_USER=$SLURM_USER SLURM_JWT=<set, 24h>"
