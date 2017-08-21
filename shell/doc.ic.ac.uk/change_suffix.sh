#!/bin/sh
for f in *.log; do
    mv $f `basename $f .log`.log1
done
