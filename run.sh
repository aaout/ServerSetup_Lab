#!/bin/sh

IMAGE_NAME=$1

if [ "${IMAGE_NAME}" = "" ]; then
exit 1
fi

docker run --rm -it --ipc=host --shm-size=20g --gpus all --env NVIDIA_DISABLE_REQUIRE=1 -v $(pwd):/usr/local/src/${IMAGE_NAME} -w /usr/local/src/${IMAGE_NAME} ${IMAGE_NAME} bash
