#!/bin/bash

PY=/home/www-data/.virtualenvs/biostarsenv/bin/python 


DIR=/home/www-data/biostar-central

cd $DIR

source live/deploy.env

$PY manage.py cleanup
#$PY manage.py clearsessions

