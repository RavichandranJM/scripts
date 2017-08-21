#!/bin/sh
for i in `ls *.html` 
do
 mv $i $i.old
done
