FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-devel

# timezone setting
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

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
        libpng-dev \
        wget && \
        rm -rf /var/lib/apt/lists/*

# scikit-learnに必要なパッケージ
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
        libglib2.0-0 \
        libsm6 \
        libxrender1 \
        libxext6 \
        libgl1-mesa-dev

# pythonライブラリ
RUN pip3 install --no-cache-dir \
        matplotlib \
        pandas \
        opencv-python \
        scikit-learn \
        scikit-image \
        openpyxl \
        tensorflow \
        torchsummary \
        segmentation_models_pytorch \
        ipykernel \
        fastprogress \
        flake8 \
        black
