#!/bin/bash
usage ()
{
 echo " Usage : $0 < -c | -d | -e editor >"
 echo "-c clear the screen"
 echo "-d lists the content in  current directory"
 echo "-e editor_name to open "
 exit 1
}
if [ $# -lt 1 ]
then
 usage
fi
while  getopts e:cd opt
do
 case "$opt" in  
 c) echo "$(clear)" ;;
 d) echo "$(ls -lrt)" ;;
 e) echo "`$OPTARG` > stdout";;
 \?)usage;;
 esac
done

