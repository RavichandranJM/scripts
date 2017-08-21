#!/bin/bash
for i in {1..9}
do
j=1
for((k=i;k<=9;k++))
do
echo -n " "
done
while [ $j -le $i ]
do
 echo -n " $i"
 j=`expr $j + 1`
done
echo " "
done
