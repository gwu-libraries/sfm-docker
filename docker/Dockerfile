FROM python:2.7
MAINTAINER Justin Littman <justinlittman@gwu.edu>

RUN apt-get update && apt-get install -y \
    wget \
    zip \
    iceweasel \
    xvfb
#Upgrade pip
RUN pip install --upgrade pip
RUN wget --no-check-certificate https://github.com/gwu-libraries/sfm-docker/archive/master.zip
RUN unzip sfm-docker-master.zip
RUN mv sfm-docker-master /opt/sfm-test
WORKDIR /opt/sfm-test
RUN pip install -r requirements.txt
CMD pip install -r requirements.txt --upgrade && python -m unittest discover