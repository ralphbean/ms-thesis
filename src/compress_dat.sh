#!/bin/bash

ID=$1
echo "Compressing ID $ID."
cd dat/$ID
/bin/tar --bzip2 -cf $ID.pops.bz2 $ID.*.pop && echo "Now removing $ID.*.pop" && /bin/rm -f $ID.*.pop && echo "Done with $ID"
cd -


