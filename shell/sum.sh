##!/bin/sh
res=0
arr=(`awk -F"," '{print $8}' new.csv`)  
for val in ${arr[@]}
do
#var1=$val
#res=`expr $res + "$val"`
	res=$(($res + $val))
done
echo $res
