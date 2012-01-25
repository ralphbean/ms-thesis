#!/bin/bash

for i in `cat best.txt` ; do
    name=`.././get_name_of_experiment.py $i`
    notify-send -t 25 "$i" "$name"
    echo $name
    mplayer -fs ../output/$i.avi
    echo $name
    echo
    echo
done
