#!/bin/bash

x1=$1
x2=$2
xstep=$3
y1=$4
y2=$5
ystep=$6
dim=$7

X=`python -c "print int(($x2-$x1)/$xstep)+2"`
Y=`python -c "print int(($y2-$y1)/$ystep)+2"`

# for formatting consistency:
xstep=`python -c "print $xstep"`
ystep=`python -c "print $ystep"`

#really, now?
name="x"
name="exhaustive-($dim).dim.$X$name"
name="$name$Y.$x1.to.$x2.step_is.$xstep.and.$y1.to.$y2.step_is.$ystep"

echo "Looking at"
echo "$name"
CMD=" set terminal postscript ; set output '$name.ps'; set key off ; set xlabel 'x'; set ylabel 'y'; set xrange[$y1:$y2]; set yrange[$x1:$x2] ; unset colorbox ; plot '$name.image' with image"
echo $CMD | /usr/bin/gnuplot
echo "Wrote to"
echo "$name.ps"
echo "Making pdf"
ps2pdf $name.ps
echo "Done"
echo
