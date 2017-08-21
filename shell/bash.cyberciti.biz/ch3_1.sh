#!/bin/sh
OLDPS=`echo $PS1`
set $PS1=\w\$
echo $PS1
