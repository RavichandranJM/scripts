#!/bin/sh
if [ $# -ne 3 ]
then 
 echo "Usage - $0 x y z"
 echo "where x,y and z are numeric inputs "
 exit 1
fi
if [ $1 -gt $2 ] 
then 
 if [ $1 -gt $3 ]
 then
  echo "$1 is the biggest number"
  exit 1
 fi 
 elif [ $2 -gt $3 ]
 then
  echo "$2 is the biggest number"
  exit 1
fi
echo "$3 is the biggest number"

