#!/bin/bash
for i in `ls *.csv`
 do
 echo " File name : $i"
 cat $i
 echo -e "\n\n\n"
done


