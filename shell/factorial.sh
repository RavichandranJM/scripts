#!/bin/bash

factorial(){
    n=$1
    if (($n == 0 || $n == 1))
    then
        echo 1
    else
        echo $(( $n * $(factorial $(($n-1))) ))
    fi
}
factorial 5
#echo "factorial 5 = $?"
