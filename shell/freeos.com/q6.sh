#!/bin/sh
if [ $# -ne 1 ]
then
 echo "Usage : $0 number "
 echo "Where \"number\" is the which one we need to reverse"
 exit 1
fi
num=$1
rnum=0
temp=0
while [ $num -gt 0 ]
do
 temp=`expr $num % 10`
 rnum=`expr $rnum \* 10 + $temp`  
 num=`expr $num / 10`
done
echo "In reverse order : $rnum"

