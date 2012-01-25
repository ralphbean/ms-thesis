#!/bin/sh

for ((  v=0 ;  v<=$1;  v++  ))
do
    frame=`printf "%010d" $v`
    CMD="set xlabel 'amplitude coefficient'; set ylabel 'approximate set of attracting orbits' ; set grid ; set xrange [0:0.06] ; set yrange [-0.25:1.25] ; set terminal jpeg ; set output '../output/frames/jpg/bifurcation.$frame.jpg' ; plot '< ./real_string_bifurcation.py 0 0.06 0.0001 $v $1' w dots"

    echo "Plotting bifurcation.$frame.jpg ($v of $1)."
    /bin/echo $CMD | /usr/bin/gnuplot
done
echo "Done processing frames."

echo "Processing avi output in ../output/bifurcation.avi"
mencoder "mf://../output/frames/jpg/bifurcation.*.jpg" -mf fps=25:type=jpg -ovc lavc -lavcopts vcodec=mpeg4 -of avi -o ../output/bifurcation.avi

#echo "Removing all the old jpgs."
#/bin/rm ../output/frames/jpg/bifurcation.*.jpg

echo "Done.  Output at:"
echo "../output/bifurcation.avi"
