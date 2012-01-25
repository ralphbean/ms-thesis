#!/bin/bash
echo 'set terminal jpeg ; set output "fitness_surface1.jpg" ; set grid ;  set xrange [0:0.2] ; set yrange [-3:3] ; set xlabel "Amplitude coefficient" ; set ylabel "Maximal lyapunov exponent" ; splot y + x' | gnuplot
echo 'set terminal jpeg ; set output "fitness_surface2.jpg" ; set grid ; set xrange [0:0.2] ; set yrange [-3:3] ; set xlabel "Amplitude coefficient" ; set ylabel "Maximal lyapunov exponent" ; splot y / x' | gnuplot
echo 'set terminal jpeg ; set output "fitness_surface3.jpg" ; set grid ; set xrange [0:0.2] ; set yrange [-3:3] ; set xlabel "Amplitude coefficient" ; set ylabel "Maximal lyapunov exponent" ; splot tanh(y) + tanh(10*(x-0.12))' | gnuplot
gthumb fitness_surface*

