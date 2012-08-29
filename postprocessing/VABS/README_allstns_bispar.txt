1. From a Windows command prompt, run the biplane spar DYMORE case
> spardesign\biplane_spar_constload\untwisted-noRootJoint_full-hSW\24-bispar-rj452-g125\rundymore.bat

2. From an mlab Python prompt, run the script to interpolate the DYMORE output data to each spar station
|> cd spardesign/postprocessing/VABS
|> run readDYMOREoutput_bispar

3. From a text editor, check the interpolated data for errors
see: spardesign/biplane_spar_constload/untwisted-noRootJoint/24-bispar-rj452-g125/FIGURES/svy_force_spar_new.mdt

# 4. From a Cygwin command prompt, run clean.sh to copy all the VABS input files (spar_station_*.dat) from # D:\data\2012-08-21 (monoplane cross-sections with VABS recovery)
# $ cd spardesign/VABS/input_files
# $ ./clean.sh
# 
# 5. From a mlab Python prompt, run the script to write the cross-sectional forces and moments (Fi and Mi) to the # end of the VABS input file to all VABS input files
# |> run runVABSrecovery_allstns
# 
# 6. From a text editor, check the VABS recovery output data for errors
# see: spardesign/VABS/input_files/spar_station_**.dat.ELE
# 
# 7. Write the Tecplot input files for all the spar stations
# |> run writeTecplotFile_allstns
# 
# 8. From a Windows command prompt, plot the data in Tecplot with all the different layout files
# > open_all_tecplot.bat
