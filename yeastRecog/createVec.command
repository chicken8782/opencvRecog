#!/bin/sh
echo "Hello, World!"
opencv_createsamples -img pos/ -vec vec/image.vec -num 3000 -bgcolor 255 -maxidev 40 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.5
