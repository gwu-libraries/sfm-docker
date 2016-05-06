FROM ubuntu:14.04
MAINTAINER Justin Littman <justinlittman@gwu.edu>

# This pre-fetches the most recent requirements.apt.
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-docker/master/requirements/processing_requirements.apt /opt/sfm-setup/
RUN apt-get update
RUN cat /opt/sfm-setup/processing_requirements.apt | tr "\n" " " | xargs apt-get install -y
#Upgrade pip
RUN pip install pip==7.1.2
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-twitter-harvester/master/requirements/common.txt /tmp/
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-twitter-harvester/master/requirements/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
# Clone twarc so that have utilities
RUN git clone https://github.com/edsu/twarc.git /opt/twarc
WORKDIR /opt/sfm-twitter-harvester
# Really want to use dev.txt, but need a version without warcprox.
CMD python setup.py install \
    && pip install -r requirements/dev_no_warcprox.txt --upgrade \
    && git -C /opt/twarc pull \
    && cd /sfm-data \
    && /bin/bash

# add --no-cache if necessary
# To build:
# docker build -t gwul/sfm-processing:dev docker/dev/processing/
# To run:
# docker run -it --rm --link=docker_sfmapp_1:api --volumes-from=docker_sfmdata_1 --volume=/Users/justinlittman/Data/sfm3/sfm-twitter-harvester:/opt/sfm-twitter-harvester --volume=/Users/justinlittman/Data/sfm3/sfm-utils:/opt/sfm-utils gwul/sfm-processing:dev
