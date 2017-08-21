#!/bin/sh
if [ $# -lt 3 ]
then
 echo " usage : $0 a_line_num range_from_that_line_no file_name"
 exit 1
fi
if [ -e $3 ]
then
var1=`expr $1 + $2 - 1`
head -n $var1 $3 | tail -n $2
else 
 echo "No such file"
fi
