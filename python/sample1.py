#!/usr/bin/python
#import Numeric;
import array;
import numpy;
count=0;
arr={};
arr[0]=4;
arr[1]=2;
arr[2]=7;
numpy.sort(arr);
a=10;
b=20;
c=1;
#print "%d"%arr.sum();


int_array = array.array('i',[5,4,10,23,8])
int_array.append(9);
int_array = array.array('i',sorted(int_array));
print "Sum : %d"%sum(int_array);
print "Median : %d"%numpy.median(int_array);
