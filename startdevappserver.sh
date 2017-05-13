#!/bin/sh

# usage: startdevappserver.sh port

if [ $# -ne 1 ]; then
    echo "usage: $(basename ${0}) port" >&2
    exit 1
fi

PORT=$1

# Verify Python version
PYTHON_VERSION=$(python --version 2>&1 | cut -c8- | awk -F'\.' '{ print $1"."$2 }')
if [ "${PYTHON_VERSION}" != "2.7" ]; then
    echo "error: app engine requires python 2.7, current version is $(python --version 2>&1)" >&2
    exit 1
fi

dev_appserver.py --port=$PORT site
