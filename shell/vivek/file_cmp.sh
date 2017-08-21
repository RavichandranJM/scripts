#!/bin/sh
linecount1=$(wc -l file1 | cut -d\  -f 1 )
count1=1
while [ $count1 -le $linecount1 ]
do
STRING1=`head -n $count1 file1 | tail -1`
STRING2=`head -n $count1 file2 | tail -1`
COUNT=0
while [ $COUNT -lt ${#STRING1} ]
do
    POS=$(($COUNT + 1))
    char1=$(echo "${STRING1}" | cut -c $POS)
    char2=$(echo "${STRING2}" | cut -c $POS)
    if [ $char1 != $char2 ]; then
        echo $STRING1
        echo $STRING2
    fi

    COUNT=$(($COUNT + 1))
done
count1=`expr $count1 + 1`
done
