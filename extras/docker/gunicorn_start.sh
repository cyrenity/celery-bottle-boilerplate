#!/bin/sh

NAME="app"
APPDIR="/app"
SOCKFILE=/tmp/gunicorn.sock
NUM_WORKERS=5
MAX_REQUESTS=5

echo "Starting $NAME as `whoami`"

# Create the run directory if it doesn't exist.
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Programs meant to be run under supervisor should not daemonize themselves
# (do not use --daemon).
exec gunicorn \
    --name $NAME \
    --workers $NUM_WORKERS \
    --max-requests $MAX_REQUESTS \
    --timeout 30 \
    --log-level debug \
    --bind unix:$SOCKFILE \
    --chdir /app \
    app:app

