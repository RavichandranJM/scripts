#!/bin/sh
if [ $# -ne 3 ]
then
 echo "Usage: $0 value1 operator value2"
 echo "Where value1 and value2 are numeric values"
 echo "operator can be +,-,/,x (For Multiplication)"
 exit 1;
fi
case $2 in
+) echo "Addition of $1 and $3 is" `expr $1 + $3`;; 
-) echo "Subtraction of $1 and $3 is" `expr $1 - $3`;; 
x) echo "Multiplication of $1 and $3 is" `expr $1 \* $3`;; 
/) echo "Division of $1 and $3 is" `expr $1 / $3`;; 
*) echo "Warning -$2 is invalid operator ,only +,-,x,/ opertor allowed"
   exit;;
esac

 

