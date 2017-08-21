#!/bin/sh
count=5
while [ $count -gt 0 ]
do
echo "$count"
count=`expr $count - 1`
done

