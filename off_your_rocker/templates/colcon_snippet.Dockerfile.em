# TODO different snippet for non-ubuntu base images
RUN apt-get update \
 && apt-get install -y python3-pip \
 && apt-get clean \
 && pip3 install -U setuptools \
 && pip3 install \
    colcon-common-extensions \
    colcon-spawn-shell