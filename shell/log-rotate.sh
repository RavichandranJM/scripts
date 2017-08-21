#!/bin/sh
#cp op.txt op.txt.$(date +%Y-%m-%d) 
#cat /dev/null > op.txt
for i in `ls -lrt | grep -i op.txt`
do
 if [ "$i" = "op.txt.$(date +%Y-%m-%d -d -15day)" ]
 then
 rm -rf $i
 fi
done
