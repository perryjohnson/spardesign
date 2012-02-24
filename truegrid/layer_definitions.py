layer[1].layer_no = 1 # layer 1
layer[1].material = matl[1] # uniaxial GFRP
layer[1].theta3 = 0.0 # 0 degrees, layup angle
layer[1].color = 'red' # color to fill elements assigned with this layer
layer[1].rgb = (1,0,0) # RGB code for fill color

layer[2].layer_no = 2 # layer 2
layer[2].material = matl[2] # biaxial GFRP
layer[2].theta3 = 45.0 # 45 degrees, layup angle
layer[2].color = 'green' # color to fill elements assigned with this layer
layer[2].rgb = (0,0.514,0) # RGB code for fill color

layer[3].layer_no = 3 # layer 3
layer[3].material = matl[2] # biaxial GFRP
layer[3].theta3 = -45.0 # -45 degrees, layup angle
layer[3].color = 'cyan' # color to fill elements assigned with this layer
layer[3].rgb = (0,1,1) # RGB code for fill color

layer[4].layer_no = 4 # layer 4
layer[4].material = matl[3] # triaxial GFRP
layer[4].theta3 = 45.0 # 45 degrees, layup angle
layer[4].color = 'tan' # color to fill elements assigned with this layer
layer[4].rgb = (0,0.706,0.549)

layer[5].layer_no = 5 # layer 5
layer[5].material = matl[3] # triaxial GFRP
layer[5].theta3 = -45.0 # -45 degrees, layup angle
layer[5].color = 'yellow' # color to fill elements assigned with this layer
layer[5].rgb = (1,1,0) # RGB code for fill color

layer[6].layer_no = 6 # layer 6
layer[6].material = matl[3] # triaxial GFRP
layer[6].theta3 = 0.0 # 0 degrees, layup angle
layer[6].color = 'blue' # color to fill elements assigned with this layer
layer[6].rgb = (0,0,1) # RGB code for fill color

layer[7].layer_no = 7 # layer 7
layer[7].material = matl[4] # foam
layer[7].theta3 = 0.0 # 0 degrees, layup angle
layer[7].color = 'magenta' # color to fill elements assigned with this layer
layer[7].rgb = (1,0,1) # RGB code for fill color
