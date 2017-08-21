#!/bin/sh
usage()
{
    echo "usage : $0 process_name1 process_name2 .... and so on "
    echo "process_name : the name of the process to find out process id"
    exit 1;
}
if [ $# -lt 1 ]
then
    usage;
fi
pidof $1
