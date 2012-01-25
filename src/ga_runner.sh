#!/bin/bash

#./get_combos.py $1 | xargs -d \n ./ga.py

# START OF SCRIPT
# Get the total number of experiments..
N=`wc -l combos$1.txt | awk ' { print $1 } '`
exec < combos$1.txt
while read line
do
    N=$(($N-1))
    echo "./ga.py $line # $N experiments left."
    notify-send "ga_runner.py $1" "Finished one.  $N experiments left."
    ./ga.py $line
done
#END OF SCRIPT
