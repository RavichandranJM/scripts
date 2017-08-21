#!/bin/sh
RANDOM=`date '+%s'`
ran=$[($RANDOM % 60) + 1]
if [ $ran -lt 30 ]
 then
 echo "Would you like to remove[y/n]"
 read result
 if [ $result == y ];
  then
  echo "jobs deleted"
  else
  echo "jobs are not deleted "
 fi
else
echo "no jobs to delete"
fi
