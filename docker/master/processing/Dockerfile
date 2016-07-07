FROM ubuntu:14.04
MAINTAINER Justin Littman <justinlittman@gwu.edu>

ARG DEBIAN_FRONTEND=noninteractive
# This pre-fetches the most recent requirements.apt.
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-docker/master/requirements/processing_requirements.apt /opt/sfm-setup/
RUN apt-get update
RUN cat /opt/sfm-setup/processing_requirements.apt | tr "\n" " " | xargs apt-get install -y
#Upgrade pip
RUN pip install pip==7.1.2
# Twitter
WORKDIR /tmp
ADD https://github.com/gwu-libraries/sfm-twitter-harvester/archive/master.zip /tmp/
RUN unzip master.zip
RUN mv sfm-twitter-harvester-master /opt/sfm-twitter-harvester
WORKDIR /opt/sfm-twitter-harvester
RUN pip install -r requirements/master.txt
RUN pip install .
# Flickr
WORKDIR /tmp
ADD https://github.com/gwu-libraries/sfm-flickr-harvester/archive/master.zip /tmp/
RUN unzip master.zip
RUN mv sfm-flickr-harvester-master /opt/sfm-flickr-harvester
WORKDIR /opt/sfm-flickr-harvester
RUN pip install -r requirements/master.txt
RUN pip install .
#Weibo
WORKDIR /tmp
ADD https://github.com/gwu-libraries/sfm-weibo-harvester/archive/master.zip /tmp/
RUN unzip master.zip
RUN mv sfm-weibo-harvester-master /opt/sfm-weibo-harvester
WORKDIR /opt/sfm-weibo-harvester
RUN pip install -r requirements/master.txt
RUN pip install .
# Clone twarc so that have utilities
RUN git clone https://github.com/edsu/twarc.git /opt/twarc
# Add warctools
RUN pip install warctools
# Add JWAT-tools
ADD https://bitbucket.org/nclarkekb/jwat-tools/downloads/jwat-tools-0.6.2.zip /tmp/
RUN unzip /tmp/jwat-tools-0.6.2.zip -d /tmp/
RUN mv /tmp/jwat-tools-0.6.2 /opt/jwat-tools
WORKDIR /opt/sfm-twitter-harvester
CMD git -C /opt/twarc pull \
    && cd /sfm-data \
    && /bin/bash

# To run:
# docker run -it --rm --link=docker_sfmuiapp_1:api --volumes-from=docker_sfmdata_1 gwul/sfm-processing:master
