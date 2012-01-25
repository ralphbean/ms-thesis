#!/bin/bash

CMD="set grid ;
set xlabel 'amplitude coefficient' ;
set ylabel 'maximal lyapunov exponent' ;
set title 'Random Single Point Crossover - Generation 4000' ;
set terminal jpeg ; set output '0.0.0.0.spread_final.jpg' ;
plot '< ./visualize.py 0.0.0.0 3999 spread_frame'"
echo $CMD | gnuplot
CMD="set grid ;
set xlabel 'amplitude coefficient' ;
set ylabel 'maximal lyapunov exponent' ;
set title 'Fixed Single Point Crossover - Generation 4000' ;
set terminal jpeg ; set output '0.1.0.0.spread_final.jpg' ;
plot '< ./visualize.py 0.1.0.0 3999 spread_frame'"
echo $CMD | gnuplot
CMD="set grid ;
set xlabel 'amplitude coefficient' ;
set ylabel 'maximal lyapunov exponent' ;
set title 'Gaussian Crossover - Generation 4000' ;
set terminal jpeg ; set output '0.2.0.0.spread_final.jpg' ;
plot '< ./visualize.py 0.2.0.0 3999 spread_frame'"
echo $CMD | gnuplot
CMD="set grid ;
set xlabel 'amplitude coefficient' ;
set ylabel 'maximal lyapunov exponent' ;
set title 'Fourier Gaussian Crossover - Generation 4000' ;
set terminal jpeg ; set output '0.3.0.0.spread_final.jpg' ;
plot '< ./visualize.py 0.3.0.0 3999 spread_frame'"
echo $CMD | gnuplot

CMD="set grid ;
set xlabel 'generation' ;
set ylabel 'maximal lyapunov exponent' ;
set title 'Random Single Point Crossover - Average Maximal Lyapunov Exponent' ;
set terminal jpeg ; set output '0.0.0.0.avg_fitness.jpg' ;
plot '< ./visualize.py 0.0.0.0 3999 avg_fitness' w lines"
echo $CMD | gnuplot
CMD="set grid ;
set xlabel 'generation' ;
set ylabel 'maximal lyapunov exponent' ;
set title 'Fixed Single Point Crossover - Average Maximal Lyapunov Exponent' ;
set terminal jpeg ; set output '0.1.0.0.avg_fitness.jpg' ;
plot '< ./visualize.py 0.1.0.0 3999 avg_fitness' w lines"
echo $CMD | gnuplot
CMD="set grid ;
set xlabel 'generation' ;
set ylabel 'maximal lyapunov exponent' ;
set title 'Gaussian Crossover - Average Maximal Lyapunov Exponent' ;
set terminal jpeg ; set output '0.2.0.0.avg_fitness.jpg' ;
plot '< ./visualize.py 0.2.0.0 3999 avg_fitness' w lines"
echo $CMD | gnuplot
CMD="set grid ;
set xlabel 'generation' ;
set ylabel 'maximal lyapunov exponent' ;
set title 'Fourier Gaussian Crossover - Average Maximal Lyapunov Exponent' ;
set terminal jpeg ; set output '0.3.0.0.avg_fitness.jpg' ;
plot '< ./visualize.py 0.3.0.0 3999 avg_fitness' w lines"
echo $CMD | gnuplot

