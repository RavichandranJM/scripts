#! /usr/bin/python

fn=open("inline.csv", 'w');
str = "hello";
str1 = "world"
print >> fn, ("%s") % (str);
print >> fn, ("%s") % (str1);
fn.close();
