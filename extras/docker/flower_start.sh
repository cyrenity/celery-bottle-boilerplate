#!/bin/sh
cd /app
exec flower -A tasks --address=0.0.0.0 --port=5555 --url_prefix=flower --natural-time
