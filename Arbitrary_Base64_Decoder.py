#!/usr/bin/env python

# Simple script to base64 decode the contents of a file N times. 
# Arg 1 is the file path. Arg 2 is the number of times to decode.
# Written by strikeoncmputrz

import sys
import base64 


# Catch incorrect number of args and print help message
if len(sys.argv) < 3:
	print '\nThis is a simple script to base64 decode the contents of a file N times.\n'\
		'Arg 1 is the file path. Arg 2 is the number of times to decode.\n'
	sys.exit(1)

#Read all ascii chars from a file (arg[1])
pwfile = open(sys.argv[1], 'r')
encoded_line = pwfile.read()
pwfile.close()

#Second Arg is number of times to decode (arg[2])
num_decode = int(sys.argv[2])

dec = encoded_line

for i in range(0, num_decode):
	dec = base64.decodestring(dec)

print dec
