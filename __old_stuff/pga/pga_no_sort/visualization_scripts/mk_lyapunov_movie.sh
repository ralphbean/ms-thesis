#!/bin/sh

for ((  v=0 ;  v<=$1;  v++  ))
do
    frame=`printf "%010d" $v`
    CMD="set xlabel 'amplitude coefficient'; set ylabel 'maximal lyapunov exponent' ; set grid ; set xrange [0:0.06] ; set yrange [-3:3] ; set terminal jpeg ; set output '../output/frames/jpg/lyapunov.$frame.jpg' ; plot '< ./real_string_lyapunov.py 0 0.06 0.0005 $v $1' w lines"

    echo "Plotting lyapunov.$frame.jpg ($v of $1)."
    /bin/echo $CMD | /usr/bin/gnuplot
done
echo "Done processing frames."

echo "Processing avi output in ../output/lyapunov.avi"
mencoder "mf://../output/frames/jpg/lyapunov.*.jpg" -mf fps=25:type=jpg -ovc lavc -lavcopts vcodec=mpeg4 -of avi -o ../output/lyapunov.avi

#echo "Removing all the old jpgs."
#/bin/rm ../output/frames/jpg/lyapunov.*.jpg

echo "Done.  Output at:"
echo "../output/lyapunov.avi"
