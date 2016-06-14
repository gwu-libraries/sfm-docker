FROM ubuntu:14.04
MAINTAINER Justin Littman <justinlittman@gwu.edu>


ENV sfm_twitter_version 1.0.0
ENV sfm_flickr_version 1.0.0
ENV sfm_weibo_version 1.0.0
ENV sfm_docker_version 0.6.1
# This pre-fetches the most recent requirements.apt.
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-docker/${sfm_docker_version}/requirements/processing_requirements.apt /opt/sfm-setup/
RUN apt-get update
RUN cat /opt/sfm-setup/processing_requirements.apt | tr "\n" " " | xargs apt-get install -y
#Upgrade pip
RUN pip install pip==7.1.2
# Twitter
WORKDIR /tmp
ADD https://github.com/gwu-libraries/sfm-twitter-harvester/archive/${sfm_twitter_version}.zip /tmp/
RUN unzip ${sfm_twitter_version}.zip
RUN mv sfm-twitter-harvester-${sfm_twitter_version} /opt/sfm-twitter-harvester
WORKDIR /opt/sfm-twitter-harvester
RUN pip install -r requirements/requirements.txt
RUN pip install .
# Flickr
WORKDIR /tmp
ADD https://github.com/gwu-libraries/sfm-flickr-harvester/archive/${sfm_flickr_version}.zip /tmp/
RUN unzip ${sfm_flickr_version}.zip
RUN mv sfm-flickr-harvester-${sfm_flickr_version} /opt/sfm-flickr-harvester
WORKDIR /opt/sfm-flickr-harvester
RUN pip install -r requirements/requirements.txt
RUN pip install .
# Weibo
WORKDIR /tmp
ADD https://github.com/gwu-libraries/sfm-weibo-harvester/archive/${sfm_weibo_version}.zip /tmp/
RUN unzip ${sfm_weibo_version}.zip
RUN mv sfm-weibo-harvester-${sfm_weibo_version} /opt/sfm-weibo-harvester
WORKDIR /opt/sfm-weibo-harvester
RUN pip install -r requirements/requirements.txt
RUN pip install .
# Clone twarc so that have utilities
RUN git clone https://github.com/edsu/twarc.git /opt/twarc
# Add warctools
RUN pip install warctools
# Add JWAT-tools
ADD https://bitbucket.org/nclarkekb/jwat-tools/downloads/jwat-tools-0.6.2.zip /tmp/
RUN unzip /tmp/jwat-tools-0.6.2.zip -d /tmp/
RUN mv /tmp/jwat-tools-0.6.2 /opt/jwat-tools
CMD git -C /opt/twarc pull \
    && cd /sfm-data \
    && /bin/bash
