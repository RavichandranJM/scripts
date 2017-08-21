#!/bin/sh
a=5.66
b=8.67
c=`echo $a + $b | bc` 
echo "The sum : $c"
