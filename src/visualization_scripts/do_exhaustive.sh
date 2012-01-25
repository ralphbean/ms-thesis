#!/bin/bash

START=-0.081
STOP=-0.0796
STEP=0.00005
CMD="set terminal jpeg ; set output 'exhaustive.jpg' ; set xrange[$START:$STOP] ; set yrange[$START:$STOP] ; plot '< ./exhaustive_plot.py $START $STOP $STEP' w dots"
CMD="unset surface ; set contour ; set terminal jpeg ; set output 'exhaustive.jpg' ; set xrange[$START:$STOP] ; set yrange[$START:$STOP] ; splot '< ./exhaustive_plot.py $START $STOP $STEP'"
echo $CMD | gnuplot
gthumb exhaustive.jpg


