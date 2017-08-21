#!/bin/sh
if [ $# -ne 1 ]
then
 echo "Usage : $0 number"
 echo "where number is which we have to find out sum of the digits"
 exit 1
fi
num=$1
sum=0
temp=0
while [ $num -gt 0 ]
do
 temp=`expr $num % 10`
 sum=`expr $sum + $temp`
 num=`expr $num / 10`
done
echo "sum of numbers : $sum"
  



