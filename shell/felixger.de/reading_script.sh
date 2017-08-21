#!/bin/sh
N=`basename $0`
if [ "$1" = "-v" ] ;
then
 VERBOSE="-v"
shift
 fi
 if [ "$3" = "" -o "$1" = "-h" -o "$1" = "--help" ] ;
 then
 echo "$N: Usage" echo " $N [-h|--help] [-v] <regexp-search> \ <regexp-replace> <glob-file>"
 echo exit 0
 fi
 S="$1" ;
 shift ;
 R="$1" ;
 shift
 T=$$replc
 if echo "$1" | grep -q / ;
 then
 for i in "$@" ;
 do
 SEARCH=`echo "$S" | sed 's,/,\\\\/,g'`
 REPLACE=`echo "$R" | sed 's,/,\\\\/,g'`
 cat $i | sed "s/$SEARCH/$REPLACE/g" > $T
 D="$?"
 if [ "$D" = "0" ] ;
 then
 if diff -q $T $i >/dev/null ;
 then
 :
 else if [ "$VERBOSE" = "-v" ] ;
 then
 echo $i 
fi
 cat $T > $i
 fi
 rm -f $T
 fi
 done
 else find . -type f -name "$1" | xargs $0 $VERBOSE "$S" "$R"
 fi
