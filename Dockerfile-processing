FROM ubuntu:16.04
MAINTAINER Social Feed Manager <sfm@gwu.edu>

ARG DEBIAN_FRONTEND=noninteractive
# This pre-fetches the most recent requirements.apt.
ADD requirements/processing_requirements.apt /opt/sfm-setup/
RUN apt-get update
RUN cat /opt/sfm-setup/processing_requirements.apt | tr "\n" " " | xargs apt-get install -y

# Symlinks for python
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

#Upgrade pip
RUN pip install pip==9.0.1
#Avoid the warning of https
RUN pip install --upgrade ndg-httpsclient

# Twitter
RUN git clone https://github.com/gwu-libraries/sfm-twitter-harvester.git /opt/sfm-twitter-harvester
WORKDIR /opt/sfm-twitter-harvester
RUN git checkout 2.2.0
RUN pip install -r requirements/common.txt -r requirements/release.txt
RUN pip install .

# Flickr
RUN git clone https://github.com/gwu-libraries/sfm-flickr-harvester.git /opt/sfm-flickr-harvester
WORKDIR /opt/sfm-flickr-harvester
RUN git checkout 2.2.0
RUN pip install -r requirements/common.txt -r requirements/release.txt
RUN pip install .

#Weibo
RUN git clone https://github.com/gwu-libraries/sfm-weibo-harvester.git /opt/sfm-weibo-harvester
WORKDIR /opt/sfm-weibo-harvester
RUN git checkout 2.2.0
RUN pip install -r requirements/common.txt -r requirements/release.txt
RUN pip install .

# Tumblr
RUN git clone https://github.com/gwu-libraries/sfm-tumblr-harvester.git /opt/sfm-tumblr-harvester
WORKDIR /opt/sfm-tumblr-harvester
RUN git checkout 2.2.0
RUN pip install -r requirements/common.txt -r requirements/release.txt
RUN pip install .

# Clone twarc so that have utilities
RUN git clone https://github.com/docnow/twarc.git /opt/twarc
WORKDIR /opt/twarc
RUN pip install -r requirements/python3.txt
RUN pip install .

# Add warctools
RUN pip install warctools

# Add JWAT-tools
ADD https://bitbucket.org/nclarkekb/jwat-tools/downloads/jwat-tools-0.6.2.zip /tmp/
RUN unzip /tmp/jwat-tools-0.6.2.zip -d /tmp/
RUN mv /tmp/jwat-tools-0.6.2 /opt/jwat-tools

# Add CSVKit
RUN pip install csvkit

# Add gron
ADD https://github.com/tomnomnom/gron/releases/download/v0.5.2/gron-linux-amd64-0.5.2.tgz /tmp/
WORKDIR /tmp
RUN tar xzf gron-linux-amd64-0.5.2.tgz
RUN mv gron /usr/local/bin/

# Add sync scripts
ADD docker/processing/*.sh /opt/processing/
RUN chmod +x /opt/processing/*.sh

WORKDIR /sfm-processing
CMD /bin/bash
