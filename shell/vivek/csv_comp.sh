#!/bin/bash
linecount1=$(wc -l file1 | cut -d\  -f 1 )
count1=1
echo "How many fields need to check"
read f_count
fields=`sed -n '1p' file1.csv | awk -F "," {'print NF'}`
if [ $fields -lt $f_count ] 
then
 echo " Specified field exceeded maximum of field in the file "
 exit 1
fi
#echo $f_count
while [ $count1 -le $linecount1 ]
do
line1=`head -n $count1 file1.csv | tail -1`
line2=`head -n $count1 file2.csv | tail -1`
count=1
while [ $count -le $f_count ]
do
string1=`echo $line1 | cut -d "," -f$count`
string2=`echo $line2 | cut -d "," -f$count`
if [ $string1 != $string2 ]
then
 echo "file difference found at field no $count"  
 echo -e "$string1 \n $string2"
 exit
fi
count=`expr $count + 1`
done
count1=`expr $count1 + 1`
done
echo "No difference found" 
