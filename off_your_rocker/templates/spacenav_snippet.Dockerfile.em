# TODO different snippet for non-ubuntu base images
RUN apt-get update \
 && apt-get install -y libspnav-dev \
 && apt-get clean