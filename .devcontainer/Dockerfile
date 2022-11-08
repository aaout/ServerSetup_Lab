FROM nvidia/cuda:11.6.1-cudnn8-devel-ubuntu20.04

# timezone setting
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-key del 7fa2af80
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
        python3-pip \
        python3-wheel \
        python3-setuptools \
        cmake \
        git \
        curl \
        ca-certificates \
        libjpeg-dev \
        libpng-dev && \
        rm -rf /var/lib/apt/lists/*

# dependent package to install opencv-python
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
        --no-install-recommends libglib2.0-0 libsm6 libxrender1 \
        libxext6 libgl1-mesa-dev

RUN pip3 install --no-cache-dir torch==1.10.1 torchvision==0.11.2 \
        matplotlib pandas Pillow \
        opencv-python==4.5.4.60 tqdm==4.40.0 \
        tensorflow-gpu tensorboardx torchinfo scikit-learn \
        flake8 autopep8 ipywidgets

RUN pip3 install git+https://github.com/pytorch/ignite.git

COPY ./start.sh /
ENTRYPOINT ["/start.sh"]
