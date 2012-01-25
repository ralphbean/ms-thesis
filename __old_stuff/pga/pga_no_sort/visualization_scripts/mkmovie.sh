#!/bin/sh

#id=1239641504  # Done at 3050
#id=1239649351  # Ongoing... at 300
id=$1
for ((  f=0 ;  f<=$2;  f++  ))
do
    frame=`printf "%010d" $f`
    CMD="set xlabel 'amplitude coefficient'; set ylabel 'maximal Lyapunov exponent' ; set grid ; set xrange [0:0.3] ; set yrange [-5:5] ; set terminal jpeg ; set output '../output/frames/jpg/$id.$frame.jpg' ; plot '< ./visualize.py $id $f spread_frame'"

    echo "Plotting $id.$frame.jpg"
    /bin/echo $CMD | /usr/bin/gnuplot
done
echo "Done processing frames."

echo "Processing avi output in ../output/$id.avi"
mencoder "mf://../output/frames/jpg/$id.*.jpg" -mf fps=25:type=jpg -ovc lavc -lavcopts vcodec=mpeg4 -of avi -o ../output/$id.avi

echo "Removing all the old jpgs."
/bin/rm ../output/frames/jpg/$id.*.jpg

echo "Done.  Output at:"
echo "../output/$id.avi"
