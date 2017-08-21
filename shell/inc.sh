#!/bin/sh
var=1
while [ $var -lt 10 ]
do
var=`expr $var + 1`
echo $var
done
