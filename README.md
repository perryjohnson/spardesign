Usage
-----

Here, [path\to\spardesign] is a placeholder for the actual location of the
"spardesign" directory on your computer.  

(1) run DYMORE for the biplane spar  
(from Windows Command Prompt):  
  `> cd [path\to\spardesign]`  
  `> cd biplane_spar\untwisted-noRootJoint_full-hSW\24-bispar-rj452-g125`  
  `> rundymore`  

(2) run DYMORE for the monoplane spar  
(from Windows Command Prompt):  
  `> cd [path\to\spardesign]`  
  `> cd monoplane_spar\untwisted\grid_density_1`  
  `> rundymore`  

(3) plot the deflections, bending moments, and axial force resultants  
(from Windows Command Prompt, start a new IPython prompt):  
  `> ipython --pylab`  
 `|> cd [path\to\spardesign]`  
 `|> %run plot_fig_18_deflections_and_bending_moments`  
(these should look similar to Fig. 18 in the "revised_submission.pdf" paper I sent you)  
(note: plots are also saved in the "spardesign" directory as PDF and PNG files)  

(4) exit from the IPython prompt to get back to the Windows command prompt:  
 `|> exit`  

(5) once the analysis is finished, clean up the DYMORE case files  
(from Windows Command Prompt):  
  `> cd [path\to\spardesign]`  
  `> cd biplane_spar\untwisted-noRootJoint_full-hSW\24-bispar-rj452-g125`  
  `> clean`  
  `> cd [path\to\spardesign]`  
  `> cd monoplane_spar\untwisted\grid_density_1`  
  `> clean`  
(the `clean` commands may spit out some `Could Not Find` warnings, but this is okay)  


Notes
-----

Python and IPython must already be installed on your system


Project summary
---------------

Biplane spar structures will be characterized with 3 types of tip loads:  
1. flapwise (along x3-axis)  
2. edgewise (along x2-axis)  
3. torsion  (about x1-axis)  

Currently, the biplane spar and monoplane spar are both loaded with a constant
load distribution in the flapwise direction. The load distributions need to be
changed to tip loads (described above) by modifying the file "loadDist.dat".

monoplane spar:  
`[path\to\spardesign]\monoplane_spar\untwisted\grid_density_1\loadDist.dat`

biplane spar:  
`[path\to\spardesign]\biplane_spar\untwisted-noRootJoint_full-hSW\24-bispar-rj452-g125\loadDist.dat`

Instead of using an `@EDGE_LOAD_DEFINITION`, I think we will need to use a
`@DEAD_LOAD_DEFINITION`. See the DYMORE user's manual, Chapter 15 (page 359) for
details.
