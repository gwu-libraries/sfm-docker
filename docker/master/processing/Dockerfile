FROM ubuntu:14.04
MAINTAINER Justin Littman <justinlittman@gwu.edu>


# This pre-fetches the most recent requirements.apt.
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-docker/master/requirements/processing_requirements.apt /opt/sfm-setup/
RUN apt-get update
RUN cat /opt/sfm-setup/processing_requirements.apt | tr "\n" " " | xargs apt-get install -y
#Upgrade pip
RUN pip install pip==7.1.2
WORKDIR /tmp
ADD https://github.com/gwu-libraries/sfm-twitter-harvester/archive/master.zip /tmp/
RUN unzip master.zip
RUN mv sfm-twitter-harvester-master /opt/sfm-twitter-harvester
WORKDIR /opt/sfm-twitter-harvester
RUN pip install -r requirements/master.txt
# Clone twarc so that have utilities
RUN git clone https://github.com/edsu/twarc.git /opt/twarc
WORKDIR /opt/sfm-twitter-harvester
CMD git -C /opt/twarc pull \
    && cd /sfm-data \
    && /bin/bash
