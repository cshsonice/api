#!/bin/bash

target_dir=$(dirname $0)
cd ${target_dir}
echo "working in ${PWD}"

while read line; do eval "export $line && echo $line"; done < .env
echo -e "Gunicorn Running... \n"
gunicorn src.app:app \
    -w 4 \
    -b 0.0.0.0:${PORT} \
    --error-logfile log/flask-error.log \
    --access-logfile log/flask-access.log \
    --log-level debug \
    --limit-request-field_size 8190



