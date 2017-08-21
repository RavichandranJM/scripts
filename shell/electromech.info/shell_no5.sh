#!/bin/bash
usage ()
{
    echo "$0 dir_name1 extension"
    echo "Ex : $0 /etc *.txt"
    exit
}
if [ $# -eq 0 ]
then
    usage
fi
while [ $# -gt 1 ]
do
if [ -d $1 ]
then
    echo "Listing only $2 from $1"
    #cd $1
    ls $1/$2
    shift
    shift
else
    echo "Directory does not exist"
fi
done
