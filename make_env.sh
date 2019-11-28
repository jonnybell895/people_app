#!/bin/bash

if [[ ! -d env ]]
then
    printf '\nCreating virtualenv'
    virtualenv env -p python3
    . env/bin/activate
    pip install -r requirements.txt
else
    printf '\nWARNING: env directory already exists\n'
fi
