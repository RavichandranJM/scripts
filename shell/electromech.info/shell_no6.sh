#!/bin/bash
echo "Please give input :"
read input
if [ $input ]
then
    echo "your input $input"
else
    echo "you forgot to give input"
fi
