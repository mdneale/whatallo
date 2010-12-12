#!/bin/sh

# usage: startdevappserver.sh <port>

if [ $# -ne 1 ]; then
    echo "usage: $(basename ${0}) <port>"
    exit 1
fi

PORT=$1

dev_appserver.py --port=$PORT site
