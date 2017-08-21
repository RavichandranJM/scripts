#!/bin/bash
ls -lrt | awk {'print $8'} | awk -F"." {'print $1'} | tr '[a-z]' '[A-Z]'

