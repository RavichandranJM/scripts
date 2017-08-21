#!/bin/sh
ran=`od -vAn -N1 -tu4 < /dev/urandom`
guess=0
while [ $guess -ne $ran ]
do
    echo "Guess no :"
    read guess
if [ $guess -gt $ran ]
then
    echo "your guess is high"
else 
        echo "your guess is low"
fi
done
echo " your guess is correct $ran"



