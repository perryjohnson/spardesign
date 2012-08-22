1. From a Windows command prompt, run the monoplane spar DYMORE case
> spardesign\monoplane_spar_constload\untwisted\grid_density_1\rundymore.bat

2. From an mlab Python prompt, run the script to interpolate the DYMORE output data to each spar station
|> cd spardesign/postprocessing/VABS
|> run readDYMOREoutput

3. From a text editor, check the interpolated data for errors
see: spardesign/monoplane_spar_constload/untwisted/grid_density_1/FIGURES/svy_force_spar_new.mdt

4. Update the Python script with the interpolated data from DYMORE
edit: spardesign/postprocessing/VABS/runVABSrecovery.py
recovery_dict['F1'] = ?
recovery_dict['F2'] = ?
recovery_dict['F3'] = ?
recovery_dict['M1'] = ?
recovery_dict['M2'] = ?
recovery_dict['M3'] = ?

5. Then, run the script to write the cross-sectional forces and moments (Fi and Mi) to the end of the VABS input file
|> run runVABSrecovery

6. From a text editor, check the VABS recovery output data for errors
see: spardesign/VABS/input_files/spar_station_24.dat.ELE

7. Write the Tecplot input file
|> run writeTecplotFile

8. Plot the data in Tecplot (try using the custom layout file: spardesign/postprocessing/VABS/spar_station_24.lay)