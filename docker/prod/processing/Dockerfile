FROM ubuntu:14.04
MAINTAINER Justin Littman <justinlittman@gwu.edu>


ENV sfm_twitter_version 0.4.1
ENV sfm_docker_version 0.6.1
# This pre-fetches the most recent requirements.apt.
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-docker/${sfm_docker_version}/requirements/processing_requirements.apt /opt/sfm-setup/
RUN apt-get update
RUN cat /opt/sfm-setup/processing_requirements.apt | tr "\n" " " | xargs apt-get install -y
#Upgrade pip
RUN pip install pip==7.1.2
WORKDIR /tmp
ADD https://github.com/gwu-libraries/sfm-twitter-harvester/archive/${sfm_twitter_version}.zip /tmp/
RUN unzip ${sfm_twitter_version}.zip
RUN mv sfm-twitter-harvester-${sfm_twitter_version} /opt/sfm-twitter-harvester
WORKDIR /opt/sfm-twitter-harvester
RUN pip install -r requirements/requirements.txt
RUN python setup.py install
# Clone twarc so that have utilities
RUN git clone https://github.com/edsu/twarc.git /opt/twarc
CMD git -C /opt/twarc pull \
    && cd /sfm-data \
    && /bin/bash
