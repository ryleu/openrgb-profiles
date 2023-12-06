#!/usr/bin/env sh

# activate the venv
. .venv/bin/activate

# run the script, passing in the arguments
python3 main.py "$@"
