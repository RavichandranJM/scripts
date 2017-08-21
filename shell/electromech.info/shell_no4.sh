#!/bin/bash
usage ()
{
    echo "$0 dir_name1 dir_name2 and so on"
    exit
}
if [ $# -eq 0 ]
then
    usage
fi
while [ $# -gt 0 ]
do
if [ -d $1 ]
then
    echo "Contents of $1"
    ls -lrt $1
    shift
else
    echo "Directory does not exist"
fi
done
