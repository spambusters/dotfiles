#!/bin/bash

# A shell script which displays the output of uptime --pretty in a minimal fashion.
#
# Changes
# up 2 days, 1 hour, 35 minutes
# into
# 2d 1h 35m
uptime --pretty | sed 's/up //' | sed 's/\ years\?,/y/' | sed 's/\ days\?,/d/' | sed 's/\ hours\?,\?/h/' | sed 's/\ minutes\?/m/'
