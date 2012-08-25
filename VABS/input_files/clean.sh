#!/bin/bash
echo REMOVING:
ls *.dat*
rm *.dat*

echo original VABS input files restored.
cd "/cygdrive/d/data/2012-08-21 (monoplane cross-sections with VABS recovery)"
cp spar_station_*.dat --target-directory=/cygdrive/d/Dropbox/ucla/research/perry/github/spardesign/VABS/input_files
cd -
chmod a+rx spar_station_*
chmod u+w spar_station_*