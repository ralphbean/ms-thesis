#!/bin/bash

for i in `cat best.txt` ; do
    name=`.././get_name_of_experiment.py $i`
    notify-send "$i" "$name"
    echo $name

    #echo " Bifurcation Diagram (global)."
    #notify-send "Bifurcation diagrams" "Building $i.bifurcation.global.ps"
    #CMD="set title 'Bifurcation Diagram: $name' ; set xlabel 'Amplitude Coefficient' ; set ylabel 'Omega-set of Neuron 1' ; set terminal postscript ; set output 'bifurcs/$i.bifurcation.global.ps' ; plot '< ./pop_bifurcation.py $i global' w dots"
    #echo $CMD | gnuplot
    #convert -rotate 90 bifurcs/$i.bifurcation.global.ps bifurcs/$i.bifurcation.global.jpg
    #echo " Bifurcation Diagram (local)."
    #notify-send "Bifurcation diagrams" "Building $i.bifurcation.local.ps"
    #CMD="set title 'Bifurcation Diagram: $name' ; set xlabel 'Amplitude Coefficient' ; set ylabel 'Omega-set of Neuron 1' ; set terminal postscript ; set output 'bifurcs/$i.bifurcation.local.ps' ; plot '< ./pop_bifurcation.py $i local' w dots"
    #echo $CMD | gnuplot
    #convert -rotate 90 bifurcs/$i.bifurcation.local.ps bifurcs/$i.bifurcation.local.jpg
    echo " Lyapunov Diagram (global)."
    notify-send "Bifurcation diagrams" "Building $i.lyapunov.global.ps"
    CMD="set title 'Maximal Lyapunov Exponent: $name' ; set xlabel 'Amplitude Coefficient' ; set ylabel 'Maximal Lyapunov Exponent' ; set grid ; set terminal postscript ; set output 'bifurcs/$i.lyapunov.global.ps' ; plot '< ./pop_lyapunov.py $i global' w lines"
    echo $CMD | gnuplot
    convert -rotate 90 bifurcs/$i.lyapunov.global.ps bifurcs/$i.lyapunov.global.jpg
    echo " Lyapunov Diagram (local)."
    notify-send "Bifurcation diagrams" "Building $i.lyapunov.local.ps"
    CMD="set title 'Maximal Lyapunov Exponent: $name' ; set xlabel 'Amplitude Coefficient' ; set ylabel 'Maximal Lyapunov Exponent' ; set grid ; set terminal postscript ; set output 'bifurcs/$i.lyapunov.local.ps' ; plot '< ./pop_lyapunov.py $i local' w lines"
    echo $CMD | gnuplot
    convert -rotate 90 bifurcs/$i.lyapunov.local.ps bifurcs/$i.lyapunov.local.jpg

done
notify-send "Bifurcation diagrams" "Done making diagrams."
