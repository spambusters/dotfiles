#!/bin/bash

title=$(audtool --current-song-tuple-data title)
artist=$(audtool --current-song-tuple-data album-artist)
current=$(audtool --current-song-output-length)
length=$(audtool --current-song-length)

# -e allows use of special chars like tab
echo -e "${title} - ${artist}\t\t${current}/${length}"
