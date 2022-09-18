#!/usr/bin/env bash

# trigger build (14-6-2021)
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
echo $SCRIPTPATH
cd $SCRIPTPATH
cd ..
source venv/bin/activate
export PYTHONPATH="$(pwd)"
cd tests/tsukuda_fib_py
python -m unittest discover
