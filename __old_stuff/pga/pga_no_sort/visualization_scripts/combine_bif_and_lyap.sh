#!/bin/sh

for ((  v=0 ;  v<=$1;  v++  ))
do
    frame=`printf "%010d" $v`
    convert ../output/frames/jpg/bifurcation.$frame.jpg -rotate 90 ../output/frames/jpg/bifurcation.$frame.rotated.jpg
    convert ../output/frames/jpg/lyapunov.$frame.jpg    -rotate 90 ../output/frames/jpg/lyapunov.$frame.rotated.jpg
    convert ../output/frames/jpg/bifurcation.$frame.rotated.jpg ../output/frames/jpg/lyapunov.$frame.rotated.jpg -append ../output/frames/jpg/combined.$frame.rotated.jpg
    convert ../output/frames/jpg/combined.$frame.rotated.jpg -rotate -90 ../output/frames/jpg/combined.$frame.jpg
    echo "Done with ../output/frames/jpg/combined.$frame.jpg"
done
echo "Done processing frames."

echo "Removing all the rotated jpgs."
/bin/rm ../output/frames/jpg/*.rotated.jpg

echo "Processing avi output in ../output/bifurcation.avi"
mencoder "mf://../output/frames/jpg/combined.*.jpg" -mf w=1280:h=480:fps=$2:type=jpg -ovc lavc -lavcopts vcodec=mpeg4 -of avi -o ../output/combined.avi


echo "Done.  Output at:"
echo "../output/combined.avi"
mplayer -loop 0 ../output/combined.avi
