#!/bin/sh

id=$1
echo "Generating diversity plot for $id."
CMD="set xlabel 'generation'; set ylabel 'diversity' ; set grid ; set terminal jpeg ; set output 'output/$id.diversity.jpg' ; plot '< ./visualize.py $id $2 diversity' w lines"
echo $CMD | gnuplot
echo "Done with:"
echo "output/$id.diversity.jpg"
