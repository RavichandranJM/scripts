#!/bin/sh
cat "$1" > /tmp/file.$$
grep "*" /tmp/file.$$
#echo "$1" | grep "*"
if [ $? -eq 0 ]
then
 echo " * symbol is not required "
else
 echo "Required ie $1/* " 
fi
rm -rf /tmp/file.$$
