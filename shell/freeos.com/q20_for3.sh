#!/bin/bash
i=1
while [ $i -le 5 ]
do
for((j=1;j<=i;j++))
do
echo -n "$j"
done
i=`expr $i + 1`
echo " " 
done
