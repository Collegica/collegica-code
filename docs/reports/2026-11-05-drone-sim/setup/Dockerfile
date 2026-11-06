FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
      libvulkan1 vulkan-tools libxext6 libx11-6 libegl1 libsdl2-2.0-0 libomp5 \
      libjpeg8 libtiff5 libpng16-16 xdg-user-dirs \
      python3 python3-pip procps && rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache-dir numpy Pillow msgpack-rpc-python && pip3 install --no-cache-dir --no-deps airsim
COPY carla_python_module.tar.gz /tmp/
RUN tar xzf /tmp/carla_python_module.tar.gz -C /usr/local/lib/python3.10/dist-packages && rm /tmp/carla_python_module.tar.gz
ENV LD_LIBRARY_PATH=/usr/local/lib/python3.10/dist-packages/carla.libs
COPY nvidia_icd.json /etc/vulkan/icd.d/nvidia_icd.json
RUN useradd -u 950 -m sim
USER sim
