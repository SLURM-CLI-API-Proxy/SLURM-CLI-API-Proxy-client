#!/bin/bash
# Run the Dask integration test inside the Slurm test container.
#
# The Dask scheduler, the proxy CLI and the Slurm workers all run in the container,
# so this works the same on Linux and on Docker Desktop (Mac), where containers
# can't reach a scheduler on the host. The workers are submitted and cancelled only
# through the proxy's sbatch/scancel -> slurmrestd (not the real Slurm CLI).
#
#   testing/slurm-container/run_dask_test.sh
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
NAME="${SLURM_TEST_NAME:-testslurm}"

# shellcheck source=/dev/null
source "$HERE/start.sh"

echo "Installing the proxy client in the container..."
docker exec "$NAME" rm -rf /tmp/proxy-src
tar -C "$REPO" --exclude=.git --exclude='*.egg-info' --exclude=__pycache__ -cf - . | docker exec -i "$NAME" bash -c 'mkdir -p /tmp/proxy-src && tar -C /tmp/proxy-src -xf -'
docker exec "$NAME" /opt/venv/bin/pip install --quiet --no-deps --no-build-isolation /tmp/proxy-src
docker exec "$NAME" chmod -R a+rX /tmp/proxy-src

TOKEN="$(docker exec "$NAME" scontrol token username=testuser lifespan=3600)"
docker exec -u testuser -w /home/testuser \
    -e PROXY_SLURM_API_URL=http://localhost:6820 -e SLURM_USER=testuser -e "$TOKEN" \
    -e DASK_WORKER_PYTHON=/opt/venv/bin/python -e DASK_LOG_DIR=/home/testuser/dask-logs \
    "$NAME" /opt/venv/bin/python -m pytest -v -p no:cacheprovider -m dask \
    /tmp/proxy-src/src/tests/integration/test_dask_jobqueue.py "$@"
