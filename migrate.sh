#!/bin/bash

if [[ ! -d env ]]
then
    ./make_env.sh
fi

. env/bin/activate

python people_manager/manage.py migrate
