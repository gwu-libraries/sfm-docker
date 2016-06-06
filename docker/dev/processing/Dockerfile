FROM ubuntu:14.04
MAINTAINER Justin Littman <justinlittman@gwu.edu>

# This pre-fetches the most recent requirements.apt.
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-docker/master/requirements/processing_requirements.apt /opt/sfm-setup/
RUN apt-get update
RUN cat /opt/sfm-setup/processing_requirements.apt | tr "\n" " " | xargs apt-get install -y
#Upgrade pip
RUN pip install pip==7.1.2
# Twitter
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-twitter-harvester/master/requirements/common.txt /tmp/
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-twitter-harvester/master/requirements/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
# Flickr
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-flickr-harvester/master/requirements/common.txt /tmp/
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-flickr-harvester/master/requirements/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
# Weibo
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-weibo-harvester/master/requirements/common.txt /tmp/
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-weibo-harvester/master/requirements/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
# Clone twarc so that have utilities
RUN git clone https://github.com/edsu/twarc.git /opt/twarc
# Add warctools
RUN pip install warctools
# Add JWAT-tools
ADD https://bitbucket.org/nclarkekb/jwat-tools/downloads/jwat-tools-0.6.2.zip /tmp/
RUN unzip /tmp/jwat-tools-0.6.2.zip -d /tmp/
RUN mv /tmp/jwat-tools-0.6.2 /opt/jwat-tools
CMD cd /opt/sfm-twitter-harvester \
    && pip install -r requirements/dev_no_warcprox.txt --upgrade \
    && pip install . \
    && cd /opt/sfm-flickr-harvester \
    && pip install -r requirements/dev_no_warcprox.txt --upgrade \
    && pip install . \
    && cd /opt/sfm-weibo-harvester \
    && pip install . \
    && pip install -r requirements/dev_no_warcprox.txt --upgrade \
    && git -C /opt/twarc pull \
    && cd /sfm-data \
    && /bin/bash

# To build:
# docker build -t gwul/sfm-processing:dev docker/dev/processing/
# add --no-cache if necessary

# To run:
# docker run -it --rm --link=docker_sfmuiapp_1:api --volumes-from=docker_sfmdata_1 --volume=/Users/justinlittman/Data/sfm3/sfm-twitter-harvester:/opt/sfm-twitter-harvester --volume=/Users/justinlittman/Data/sfm3/sfm-flickr-harvester:/opt/sfm-flickr-harvester --volume=/Users/justinlittman/Data/sfm3/sfm-weibo-harvester:/opt/sfm-weibo-harvester --volume=/Users/justinlittman/Data/sfm3/sfm-utils:/opt/sfm-utils gwul/sfm-processing:dev
# Note that volumes need to be absolute paths.