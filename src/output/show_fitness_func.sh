#!/bin/bash
echo 'set terminal jpeg ; set output "fitness_surface.jpg" ; set grid ; set xrange [0:0.2] ; set yrange [-3:3] ; set xlabel "Amplitude coefficient" ; set ylabel "Maximal lyapunov exponent" ; splot tanh(y) + tanh(20*(x-0.12))' | gnuplot
gthumb fitness_surface.jpg
