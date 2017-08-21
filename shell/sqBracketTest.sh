#!/bin/bash

if grep "/bin/bash" "$1"
then
    echo "File is shell script"
else
    echo "File is not a shell script"
fi
