#!/bin/bash

#./get_combos.py $1 | xargs -d \n ./ga.py

# START OF SCRIPT
# Get the total number of experiments..
#./get_combos.py > all_combos.txt
N=`wc -l all_combos.txt | awk ' { print $1 } '`
exec < all_combos.txt
while read line
do
    N=$(($N-1))

    echo "$N left.  Creating dat/$line"
    mkdir dat/$line

    #echo "Moving dat/$line.* to dat/$line/."
    #mv dat/$line.* dat/$line/.
done
#END OF SCRIPT
