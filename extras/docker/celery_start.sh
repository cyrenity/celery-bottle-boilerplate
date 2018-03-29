#!/bin/sh
cd /app
C_FORCE_ROOT=yes exec celery -A tasks worker -B -E -l $4 --concurrency=$3 --hostname $1@ -Q $2
