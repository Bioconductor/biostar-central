#!/bin/bash
set -ue

# This is required so that the default configuration file works.
source /home/www-data/biostar-central/live/deploy.env

# Location of the log file
LOGFILE=/home/www-data/biostar-central/live/logs/celery-beat.log

# The name of the application.
APP="biostar"

# The gunicorn instance to run.
CELERY="/home/www-data/.virtualenvs/biostarsenv/bin/celery"

echo "starting celery beat with DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE"

$CELERY -A $APP beat -l info -f $LOGFILE

