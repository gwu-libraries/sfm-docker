#!/usr/bin/env bash

groupadd -r sfm --gid=$SFM_GID && useradd -r -g sfm --uid=$SFM_UID sfm

export COLLECTION_SET_DIR=/sfm-data/collection_set
if [ ! -d $COLLECTION_SET_DIR ]; then
    echo "Creating collection_sets directory"
    mkdir -p $COLLECTION_SET_DIR
    chown sfm:sfm $COLLECTION_SET_DIR
fi

export CONTAINERS_DIR=/sfm-data/containers
if [ ! -d $CONTAINERS_DIR ]; then
    echo "Creating containers directory"
    mkdir -p $CONTAINERS_DIR
    chown sfm:sfm $CONTAINERS_DIR
fi

export EXPORT_DIR=/sfm-data/export
if [ ! -d $EXPORT_DIR ]; then
    echo "Creating export directory"
    mkdir -p $EXPORT_DIR
    chown sfm:sfm $EXPORT_DIR
fi