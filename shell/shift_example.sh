#!/bin/bash
if [ $# == 0 ]
then
    echo "usage : $0 -f <file_name> -o <opertaion>"
    echo "file_name : the file which you want to open"
    echo "operation : read or write or append" 
exit 1;
fi
while [ $# -gt 0 ]
do
case $1 in
    -f)
        filename=$2
        shift;shift
        ;;
     -o)
         operation=$2
         shift;shift
         ;;
 esac
done
echo "Given file name $filename requested for open with $operation mode"
