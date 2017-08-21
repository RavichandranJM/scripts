#!/bin/sh
if [ $# -ne 1 ] 
then
 echo "Usage : $0 filename"
 echo "where filename is which you want to look for"
 exit 1;
fi
if [ -f $1 ]
then
 echo "File exists"
 exit 1;
fi 
echo "file does not exist"
