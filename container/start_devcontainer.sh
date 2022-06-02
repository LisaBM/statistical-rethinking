set -e

DOCKER_TAG=statistical_rethinking:latest
WORKING_DIR=/statistical_rethinking
ENTRYPOINT="bash"

docker build \
    .. \
    -f Dockerfile \
    -t $DOCKER_TAG

docker run \
    -it \
    --rm \
    --entrypoint bash \
    -v $(pwd)/..:$WORKING_DIR \
    -w $WORKING_DIR \
    statistical_rethinking:latest \
    container/on_start.sh
