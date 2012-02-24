# uniaxial GFRP
material_list[1].material_no = 1
material_list[1].orth_flag = 1
material_list[1].material_name = 'E-LT-5500/EP-3'
(material_list[1].E1, material_list[1].E2, material_list[1].E3) = (41.8E+09, 14.0E+09, 14.0E+09)
(material_list[1].G12, material_list[1].G13, material_list[1].G23) = (2.63E+09, 2.63E+09, 2.63E+09)
(material_list[1].nu12, material_list[1].nu13, material_list[1].nu23) = (0.28, 0.28, 0.28)
material_list[1].rho = 1.92E+03
material_list[1].color = 'grey'
material_list[1].rgb = (0.502,0.502,0.502)

# biaxial GFRP
material_list[2].material_no = 2
material_list[2].orth_flag = 1
material_list[2].material_name = 'Saertex/EP-3'
(material_list[2].E1, material_list[2].E2, material_list[2].E3) = (13.6E+09, 13.3E+09, 13.3E+09)
(material_list[2].G12, material_list[2].G13, material_list[2].G23) = (11.8E+09, 11.8E+09, 11.8E+09)
(material_list[2].nu12, material_list[2].nu13, material_list[2].nu23) = (0.51, 0.51, 0.51)
material_list[2].rho = 1.78E+03
material_list[2].color = 'teal'
material_list[2].rgb = (0,0.502,0.502)

# triaxial GFRP
material_list[3].material_no = 3
material_list[3].orth_flag = 1
material_list[3].material_name = 'SNL Triax'
(material_list[3].E1, material_list[3].E2, material_list[3].E3) = (27.7E+09, 13.65E+09, 13.65E+09)
(material_list[3].G12, material_list[3].G13, material_list[3].G23) = (7.20E+09, 7.20E+09, 7.20E+09)
(material_list[3].nu12, material_list[3].nu13, material_list[3].nu23) = (0.39, 0.39, 0.39)
material_list[3].rho = 1.85E+03
material_list[3].color = 'pink'
material_list[3].rgb = (1,0.753,0.796)

# foam
material_list[4].material_no = 4
material_list[4].orth_flag = 0
material_list[4].material_name = 'Foam'
material_list[4].E = 0.256E+09
material_list[4].nu = 0.3
material_list[4].rho = 0.20E+03
material_list[4].color = 'orange'
material_list[4].rgb = (1,0.647,0)
