# Single-node Slurm 25.05 with slurmrestd (JWT auth) for testing the proxy client.
#
# Builds Slurm from source, so it works on amd64 and arm64 (e.g. Apple Silicon).
# Test use only: one container runs slurmctld, slurmd and slurmrestd; no
# accounting database, no cgroups.
#
#   docker build -t slurm-cli-proxy-test testing/slurm-container
#   testing/slurm-container/start.sh        # build, run, print env for the client

FROM ubuntu:24.04 AS build
ARG SLURM_TAG=slurm-25-05-9-1
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential ca-certificates git pkg-config python3 \
        libmunge-dev libjwt-dev libjson-c-dev libhttp-parser-dev libyaml-dev \
        libssl-dev libpam0g-dev libreadline-dev liblz4-dev zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /build
RUN git clone --quiet --depth 1 --branch "${SLURM_TAG}" https://github.com/SchedMD/slurm.git . \
    && ./configure --prefix=/opt/slurm --sysconfdir=/etc/slurm \
        --with-jwt --with-json --with-http-parser --with-yaml \
        --disable-debug > /dev/null \
    && make -j"$(nproc)" > /dev/null \
    && make install > /dev/null

FROM ubuntu:24.04
ARG DEBIAN_FRONTEND=noninteractive
# Runtime libraries + python for Dask workers (see tests marked "dask")
RUN apt-get update && apt-get install -y --no-install-recommends \
        munge libmunge2 libjwt2 libjson-c5 libhttp-parser2.9 libyaml-0-2 \
        libssl3t64 libreadline8t64 liblz4-1 zlib1g ca-certificates \
        python3 python3-venv procps \
    && rm -rf /var/lib/apt/lists/*
COPY --from=build /opt/slurm /opt/slurm
ENV PATH=/opt/slurm/bin:/opt/slurm/sbin:$PATH

# Users: slurm (daemons), slurmrest (slurmrestd must not run as root/SlurmUser),
# testuser (submits jobs in tests). /home/tmp is used by the existing tests.
RUN useradd -r -U -d /var/lib/slurm slurm \
    && useradd -r -U -s /usr/sbin/nologin slurmrest \
    && useradd -m -U -s /bin/bash testuser \
    && mkdir -p /etc/slurm /var/spool/slurmctld /var/spool/slurmd /var/log/slurm /run/munge /home/tmp \
    && chown slurm:slurm /var/spool/slurmctld /var/log/slurm \
    && chmod 1777 /home/tmp

# Python environment for Dask workers / in-container tests (run_dask_test.sh), with the
# proxy client's runtime dependencies so it can be installed without network access
RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir "dask[distributed]" dask-jobqueue pytest \
        setuptools wheel PyYAML "pydantic>=2" python-dateutil "typing-extensions>=4.7.1" "urllib3>=2.1,<3"

# Slurm commands on the PATH of login shells (su - testuser)
RUN echo 'export PATH=/opt/slurm/bin:$PATH' > /etc/profile.d/slurm.sh

COPY slurm.conf /etc/slurm/slurm.conf
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 6820
HEALTHCHECK --interval=5s --timeout=5s --retries=30 CMD scontrol ping | grep -q UP
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
