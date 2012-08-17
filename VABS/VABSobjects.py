import numpy as np    # import the numpy module; rename it as np


class nodeObj:        # a node is a grid point (vertex)
    node_no = np.nan  # integer representing the unique number assigned to each node
    x2 = np.nan       # x2-coordinate of this node
    x3 = np.nan       # x3-coordinate of this node

    ### inspect all properties of a node (node number, x2-coordinate, x3-coordinate)
    ###     input: thisNode <vo.nodeObj>, an individual element (for example, node[3])
    ###     output: <none>, prints to the screen
    def inspect(self,funcCallFlag=False):
        if funcCallFlag:
            print '  inspecting node #' + str(self.node_no)
            print '    Coordinates, (x2, x3) = ' + '(' + str(self.x2) + ', ' + str(self.x3) + ')'
        else:
            print 'INSPECTING NODE #' + str(self.node_no)
            print '  Coordinates, (x2, x3) = ' + '(' + str(self.x2) + ', ' + str(self.x3) + ')'
        return


class materialObj:        # a material with its constants (Young's modulus, Poisson's ratio, etc.)
    material_no = np.nan  # integer representing the unique number assigned to each material
    material_name = ''    # string representing the written name of the material
    orth_flag = np.nan    # flag to indicate if matl is isotropic (0), 
                          #                             orthotropic (1), or 
                          #                             general anisotropic (2)
    rho = np.nan          # density

    ### inspect all properties of a material (material number, name, orth_flag, rho)
    ###     input: thisLayer <vo.layerObj>, an individual layer (for example, layer[3])
    ###     output: <none>, prints to the screen
    def inspect(self, funcCallFlag=False, doubleFuncCall=False):
        orth_dict = { 0: 'isotropic',
                      1: 'orthotropic',
                      2: 'general anisotropic' }

        if funcCallFlag:
            spacer = '  '
            if doubleFuncCall:
                spacer = spacer + '  '
            print spacer + 'inspecting material #' + str(self.material_no)
        else:
            spacer = ''
            print 'INSPECTING MATERIAL #' + str(self.material_no)

        print spacer + '  name: ' + self.material_name
        print spacer + '  ' + orth_dict[self.orth_flag]
        if orth_dict[self.orth_flag] == 'isotropic':
            print spacer + '  E    = ' + str('%.3e' % self.E) + ' Pa'
            print spacer + '  nu   = ' + str(self.nu)
        elif orth_dict[self.orth_flag] == 'orthotropic':
            print spacer + '  E1   = ' + str('%.3e' % self.E1) + ' Pa'
            print spacer + '  E2   = ' + str('%.3e' % self.E2) + ' Pa'
            print spacer + '  E3   = ' + str('%.3e' % self.E3) + ' Pa'
            print spacer + '  G12  = ' + str('%.3e' % self.G12) + ' Pa'
            print spacer + '  G13  = ' + str('%.3e' % self.G13) + ' Pa'
            print spacer + '  G23  = ' + str('%.3e' % self.G23) + ' Pa'
            print spacer + '  nu12 = ' + str(self.nu12)
            print spacer + '  nu13 = ' + str(self.nu13)
            print spacer + '  nu23 = ' + str(self.nu23)
        print spacer + '  rho  = ' + str(self.rho) + ' kg/m^3'
        return

class layerObj:        # a layer is a unique combination of material type and layup orientation (theta3)
    layer_no = np.nan  # integer representing the unique number assigned to each layer
    material = materialObj()  # material of this layer
    theta3 = np.nan    # layup angle (in degrees) for this layer
    
    ### inspect all properties of a layer (layer number, material, theta3)
    ###     input: thisLayer <vo.layerObj>, an individual layer (for example, layer[3])
    ###     output: <none>, prints to the screen
    def inspect(self, funcCallFlag=False):
        if funcCallFlag:
            spacer = '  '
            print '  inspecting layer #' + str(self.layer_no)
            doubleCall = True
        else:
            spacer = ''
            print 'INSPECTING LAYER #' + str(self.layer_no)
            doubleCall = False

        self.material.inspect(funcCallFlag=True, doubleFuncCall=doubleCall)
        print spacer + '  theta3 = ' + str(self.theta3) + ' degrees'
        return


class isotropicMatlObj(materialObj):  # an isotropic material object (subclass)
    E = np.nan     # Young's modulus
    nu = np.nan    # Poisson's ratio


class orthotropicMatlObj(materialObj):  # an orthotropic material object (subclass)
    E1 = np.nan     # Young's modulus in x1-direction (along beam axis)
    E2 = np.nan     # Young's modulus in x2-direction (along chord line)
    E3 = np.nan     # Young's modulus in x3-direction (in direction of cross-section thickness)
    G12 = np.nan    # shear modulus in the x1x2-plane
    G13 = np.nan    # shear modulus in the x1x3-plane
    G23 = np.nan    # shear modulus in the x2x3-plane
    nu12 = np.nan   # Poisson's ratio in the x1x2-plane
    nu13 = np.nan   # Poisson's ratio in the x1x3-plane
    nu23 = np.nan   # Poisson's ratio in the x2x3-plane


class elementObj:     # an element (quadrilateral cell) is made up of four nodes
    elem_no = np.nan  # integer representing the unique number assigned to each element

    #   4---7---3
    #   |       |
    #   8   9   6
    #   |       |
    #   1---5---2

    node1 = nodeObj() # node 1 (bottom left corner) of this quadrilateral element
    node2 = nodeObj() # node 2 (bottom right corner) of this quadrilateral element
    node3 = nodeObj() # node 3 (top right corner) of this quadrilateral element
    node4 = nodeObj() # node 4 (top left corner) of this quadrilateral element
    node5 = nodeObj() # node 5 (bottom midside node) of this quadrilateral element
    node6 = nodeObj() # node 6 (right midside node) of this quadrilateral element
    node7 = nodeObj() # node 7 (top midside node) of this quadrilateral element
    node8 = nodeObj() # node 8 (left midside node) of this quadrilateral element
    node9 = nodeObj() # node 9 (node center) of this quadrilateral element
    layer = layerObj() # layer of this element
    theta1 = np.nan   # layer plane angle (in degrees) for the layer used by this element

    ### inspect all properties of an element (element number, properties of all nodes that make up this element)
    ###     input: thisElement <vo.elementObj>, an individual element (for example, element[36])
    ###     output: <none>, prints to the screen
    def inspect(self):
        print 'INSPECTING ELEMENT #' + str(self.elem_no)
        print 'NODE1********'
        self.node1.inspect(funcCallFlag=True)
        print 'NODE2********'
        self.node2.inspect(funcCallFlag=True)
        print 'NODE3********'
        self.node3.inspect(funcCallFlag=True)
        print 'NODE4********'
        self.node4.inspect(funcCallFlag=True)
        print 'NODE5********'
        self.node5.inspect(funcCallFlag=True)
        print 'NODE6********'
        self.node6.inspect(funcCallFlag=True)
        print 'NODE7********'
        self.node7.inspect(funcCallFlag=True)
        print 'NODE8********'
        self.node8.inspect(funcCallFlag=True)
        print 'NODE9********'
        self.node9.inspect(funcCallFlag=True)
        print 'LAYER********'
        self.layer.inspect(funcCallFlag=True)
        print '  theta1 = ' + str(self.theta1) + ' degrees'
        return

    ## find the "middle" x&y coordinates of this element
    ##    input: self <object>, a single element object (e.g. elem[1])
    ##    output: x2_middle <double>, x2-coordinate of the middle of this element
    ##            x3_middle <double>, x3-coordinate of the middle of this element
    def middle(self, print_flag=False):
        x2_middle = (self.node1.x2 + self.node2.x2 + self.node3.x2 + self.node4.x2)/4.0
        x3_middle = (self.node1.x3 + self.node2.x3 + self.node3.x3 + self.node4.x3)/4.0
        if print_flag:
            print "(x2_middle, x3_middle) = (" + str(x2_middle) + ", " + str(x3_middle) + ")"
        return (x2_middle, x3_middle)

    def is_quadratic(self):
        if self.node5.node_no != 0:
            flag = True
        else:
            flag = False
        return flag

    ## find the angle between a vector drawn from the middle of the element (x2_middle, x3_middle) to the horizontal (positive x2-axis)
    def angles(self, print_flag=False):
        (x2_middle, x3_middle) = self.middle()
        from math import atan2, pi
        angle_dict={}

        # find the angle to node1
        y = self.node1.x3 - x3_middle
        x = self.node1.x2 - x2_middle
        angle_dict['node1'] = atan2(y,x) * (180.0/pi)
        if angle_dict['node1'] < 0.0:
            angle_dict['node1'] += 360.0

        # find the angle to node2
        y = self.node2.x3 - x3_middle
        x = self.node2.x2 - x2_middle
        angle_dict['node2'] = atan2(y,x) * (180.0/pi)
        if angle_dict['node2'] < 0.0:
            angle_dict['node2'] += + 360.0

        # find the angle to node3
        y = self.node3.x3 - x3_middle
        x = self.node3.x2 - x2_middle
        angle_dict['node3'] = atan2(y,x) * (180.0/pi)
        if angle_dict['node3'] < 0.0:
            angle_dict['node3'] += + 360.0

        # find the angle to node4
        y = self.node4.x3 - x3_middle
        x = self.node4.x2 - x2_middle
        angle_dict['node4'] = atan2(y,x) * (180.0/pi)
        if angle_dict['node4'] < 0.0:
            angle_dict['node4'] += + 360.0

        if self.is_quadratic():
            # find the angle to node5
            y = self.node5.x3 - x3_middle
            x = self.node5.x2 - x2_middle
            angle_dict['node5'] = atan2(y,x) * (180.0/pi)
            if angle_dict['node5'] < 0.0:
                angle_dict['node5'] += + 360.0

            # find the angle to node6
            y = self.node6.x3 - x3_middle
            x = self.node6.x2 - x2_middle
            angle_dict['node6'] = atan2(y,x) * (180.0/pi)
            if angle_dict['node6'] < 0.0:
                angle_dict['node6'] += + 360.0

            # find the angle to node7
            y = self.node7.x3 - x3_middle
            x = self.node7.x2 - x2_middle
            angle_dict['node7'] = atan2(y,x) * (180.0/pi)
            if angle_dict['node7'] < 0.0:
                angle_dict['node7'] += + 360.0

            # find the angle to node8
            y = self.node8.x3 - x3_middle
            x = self.node8.x2 - x2_middle
            angle_dict['node8'] = atan2(y,x) * (180.0/pi)
            if angle_dict['node8'] < 0.0:
                angle_dict['node8'] += + 360.0

        if print_flag:
            if self.is_quadratic():
                print "node1_angle = " + str('%6.2f' % angle_dict['node1']) + " degrees"
                print "node5_angle = " + str('%6.2f' % angle_dict['node5']) + " degrees"
                print "node2_angle = " + str('%6.2f' % angle_dict['node2']) + " degrees"
                print "node6_angle = " + str('%6.2f' % angle_dict['node6']) + " degrees"
                print "node3_angle = " + str('%6.2f' % angle_dict['node3']) + " degrees"
                print "node7_angle = " + str('%6.2f' % angle_dict['node7']) + " degrees"
                print "node4_angle = " + str('%6.2f' % angle_dict['node4']) + " degrees"
                print "node8_angle = " + str('%6.2f' % angle_dict['node8']) + " degrees"
            else:
                print "node1_angle = " + str('%6.2f' % angle_dict['node1']) + " degrees"
                print "node2_angle = " + str('%6.2f' % angle_dict['node2']) + " degrees"
                print "node3_angle = " + str('%6.2f' % angle_dict['node3']) + " degrees"
                print "node4_angle = " + str('%6.2f' % angle_dict['node4']) + " degrees"

        return angle_dict

    def is_ccw(self, print_flag=False):
        angle_dict = self.angles()
        angleDiff = []
        if self.is_quadratic():
            angleDiff.append(angle_dict['node5'] - angle_dict['node1'])
            angleDiff.append(angle_dict['node2'] - angle_dict['node5'])
            angleDiff.append(angle_dict['node6'] - angle_dict['node2'])
            angleDiff.append(angle_dict['node3'] - angle_dict['node6'])
            angleDiff.append(angle_dict['node7'] - angle_dict['node3'])
            angleDiff.append(angle_dict['node4'] - angle_dict['node7'])
            angleDiff.append(angle_dict['node8'] - angle_dict['node4'])
            angleDiff.append(angle_dict['node1'] - angle_dict['node8'])
        else:
            angleDiff.append(angle_dict['node2'] - angle_dict['node1'])
            angleDiff.append(angle_dict['node3'] - angle_dict['node2'])
            angleDiff.append(angle_dict['node4'] - angle_dict['node3'])
            angleDiff.append(angle_dict['node1'] - angle_dict['node4'])

        if print_flag:
            print "Angle differences:", angleDiff

        negCounter = 0
        for i in range(len(angleDiff)):
            if angleDiff[i] < 0.0:
                negCounter += 1

        if negCounter > 1:
            flag = False
            if print_flag:
                print "this element has the WRONG orientation"
        else:
            flag = True

        return flag


    def reorient(self, print_flag=False):
        if print_flag:
            print "BEFORE:"
            print "node2:", self.node2.node_no
            print "node4:", self.node4.node_no
        if self.is_quadratic():
            # reorder the nodes in a clockwise fashion
            temp = self.node2
            self.node2 = self.node4
            self.node4 = temp

            temp = self.node8
            self.node8 = self.node5
            self.node5 = temp

            temp = self.node6
            self.node6 = self.node7
            self.node7 = temp
        else:
            # reorder the nodes in a clockwise fashion
            temp = self.node2
            self.node2 = self.node4
            self.node4 = temp
        
        if print_flag:
            print "AFTER:"
            print "node2:", self.node2.node_no
            print "node4:", self.node4.node_no
        return


## fill the list with nnode+1 node objects (we won't use the first index, 0)
##    input: nnode <int>, number of nodes in this grid
##           node_list <object>, list of unique node objects
##    output: <none>
def fillNodeObjects(nnode, node_list):
    for i in range(nnode+1):
        node_list.append(nodeObj())
    return


## fill the list with nlayer+1 layer objects (we won't use the first index, 0)
##    input: nlayer <int>, number of layers in this grid
##           layer_list <object>, list of layer objects
##    output: <none>
def fillLayerObjects(nlayer, layer_list):
    for i in range(nlayer+1):  
        layer_list.append(layerObj())
    return


## fill the list with nmate+1 material objects (we won't use the first index, 0)
##    input: nmate <int>, number of layers in this grid
##           material_list <object>, list of layer objects
##    output: <none>
def fillMaterialObjects(nmate, material_list):
    for i in range(nmate+1):  # traverse the list of material objects
        if i == 0:
            material_list.append(materialObj())  # assign a dummy material to the 0th-index
        elif i == 4:  ### WARNING: this is hard-coded! must change for new grids with new materials!
            # assign material4 to be isotropic (this will be foam)
            material_list.append(isotropicMatlObj())
        else:  ### WARNING: this is hard-coded! must change for new grids with new materials!
            # assign all other material numbers to be orthotropic (these with be GFRP composites)
            material_list.append(orthotropicMatlObj())
    return


## assign constants to each material object
##    input: nmate <int>, number of materials in this grid
##           material_list <object>, list of material objects
##    output: <none>
def assignMaterials(nmate, material_list):
    for i in range(1,nmate+1):  # traverse the list of material objects
        material_list[i].material_no = i
        if i == 1:
            # uniaxial GFRP
            material_list[i].orth_flag = 1
            material_list[i].material_name = 'E-LT-5500/EP-3'
            (material_list[i].E1, material_list[i].E2, material_list[i].E3) = (41.8E+09, 14.0E+09, 14.0E+09)
            (material_list[i].G12, material_list[i].G13, material_list[i].G23) = (2.63E+09, 2.63E+09, 2.63E+09)
            (material_list[i].nu12, material_list[i].nu13, material_list[i].nu23) = (0.28, 0.28, 0.28)
            material_list[i].rho = 1.92E+03
            # material_list[i].color = 'grey'
            # material_list[i].rgb = (0.502,0.502,0.502)
        elif i == 2:
            # biaxial GFRP
            material_list[i].orth_flag = 1
            material_list[i].material_name = 'Saertex/EP-3'
            (material_list[i].E1, material_list[i].E2, material_list[i].E3) = (13.6E+09, 13.3E+09, 13.3E+09)
            (material_list[i].G12, material_list[i].G13, material_list[i].G23) = (11.8E+09, 11.8E+09, 11.8E+09)
            (material_list[i].nu12, material_list[i].nu13, material_list[i].nu23) = (0.51, 0.51, 0.51)
            material_list[i].rho = 1.78E+03
            # material_list[i].color = 'teal'
            # material_list[i].rgb = (0,0.502,0.502)
        elif i == 3:
            # triaxial GFRP
            material_list[i].orth_flag = 1
            material_list[i].material_name = 'SNL Triax'
            (material_list[i].E1, material_list[i].E2, material_list[i].E3) = (27.7E+09, 13.65E+09, 13.65E+09)
            (material_list[i].G12, material_list[i].G13, material_list[i].G23) = (7.20E+09, 7.20E+09, 7.20E+09)
            (material_list[i].nu12, material_list[i].nu13, material_list[i].nu23) = (0.39, 0.39, 0.39)
            material_list[i].rho = 1.85E+03
            # material_list[i].color = 'pink'
            # material_list[i].rgb = (1,0.753,0.796)
        elif i == 4:
            # foam
            material_list[i].orth_flag = 0
            material_list[i].material_name = 'Foam'
            material_list[i].E = 0.256E+09
            material_list[i].nu = 0.3
            material_list[i].rho = 0.20E+03
            # material_list[i].color = 'orange'
            # material_list[i].rgb = (1,0.647,0)
    return


## fill the list with nelem+1 element objects (we won't use the first index, 0)
##    input: nelem <int>, number of elements in this grid
##           elem <object>, list of element objects
##    output: <none>
def fillElementObjects(nelem, elem):
    for j in range(nelem+1):  
        elem.append(elementObj())
    return


## assign x&y coordinates to each node object
##    input: nnode <int>, number of nodes in this grid
##           nodeArray <np.array>, array of node numbers and x&y coords for each node
##           node_list <object>, list of unique node objects
##    output: <none>
def assignCoordinatesToNodes(nnode, nodeArray, node_list):
    node_list[0].node_no = 0  # dummy node (not actually used by VABS)
    for i in range(1,nnode+1):  # traverse the list of node objects
        node_list[i].node_no = int(nodeArray[i-1,0])
        node_list[i].x2 = nodeArray[i-1,1]  # assign the x2-coordinate for the i-th node
        node_list[i].x3 = nodeArray[i-1,2]  # assign the x3-coordinate for the i-th node
    return


def assignElementOrientations(esetArray, element):
    for i in range(len(esetArray)):  # traverse the element set
        theta1_angle = esetArray[i,0]
        elem_no = esetArray[i,1]
        element[elem_no].theta1 = theta1_angle
    return


## assign materials and layup angles (theta3) to each layer object
##    ...define each layer manually (for now)
##    input: layer_list <object>, list of layer objects
##           matl <object> list of material objects
##    output: <none>
def assignLayers(layer_list, matl):
    layer_list[1].layer_no = 1       # layer 1
    layer_list[1].material = matl[1] # uniaxial GFRP
    layer_list[1].theta3 = 0.0       # 0 degrees, layup angle

    layer_list[2].layer_no = 2       # layer 2
    layer_list[2].material = matl[2] # biaxial GFRP
    layer_list[2].theta3 = 45.0      # 45 degrees, layup angle

    layer_list[3].layer_no = 3       # layer 3
    layer_list[3].material = matl[2] # biaxial GFRP
    layer_list[3].theta3 = -45.0     # -45 degrees, layup angle

    layer_list[4].layer_no = 4       # layer 4
    layer_list[4].material = matl[3] # triaxial GFRP
    layer_list[4].theta3 = 45.0      # 45 degrees, layup angle

    layer_list[5].layer_no = 5       # layer 5
    layer_list[5].material = matl[3] # triaxial GFRP
    layer_list[5].theta3 = -45.0     # -45 degrees, layup angle

    layer_list[6].layer_no = 6       # layer 6
    layer_list[6].material = matl[3] # triaxial GFRP
    layer_list[6].theta3 = 0.0       # 0 degrees, layup angle

    layer_list[7].layer_no = 7       # layer 7
    layer_list[7].material = matl[4] # foam
    layer_list[7].theta3 = 0.0       # 0 degrees, layup angle

    return


## assign nodes to each element object
##    input: nelem <int>, number of elements in this grid
##           elemArray <array>, array that describes the layer number, element number, and connectivity of each element
##              elemArray[j-1,0] = layer_no
##              elemArray[j-1,1] = elem_no
##              elemArray[j-1,2] = node1
##              elemArray[j-1,3] = node2
##              elemArray[j-1,4] = node3
##              elemArray[j-1,5] = node4
##              elemArray[j-1,6] = node5
##              elemArray[j-1,7] = node6
##              elemArray[j-1,8] = node7
##              elemArray[j-1,9] = node8
##           elem <object>, list of element objects
##           node_list <object>, list of unique node objects
##    output: <none>
def assignNodesAndLayersToElements(nelem, elemArray, elem, node_list, layer_list):
    # determine if linear or quadratic elements are being used
    if elemArray.shape[1] == 10:  # elemArray has 10 columns (layer number, element number, node1, node2, node3, node4, node5, node6, node7, node8)
        is_quadratic = True
        print "  QUADRATIC finite elements were detected"
    elif elemArray.shape[1] == 6: # elemArray has 6 columns  (layer number, element number, node1, node2, node3, node4)
        is_quadratic = False
        print "  LINEAR finite elements were detected"
    else:
        is_quadratic = False
        print "WARNING in VABSobjects.assignNodesAndLayersToElements: elemArray has " + str(elemArray.shape[1]) + " columns, instead of the standard 6 columns (linear elements) or 10 columns (quadratic elements)"

    for j in range(1,nelem+1):  # traverse the list of element objects
        layer_number = elemArray[j-1,0]
        element_number = elemArray[j-1,1]

        elem[j].layer = layer_list[layer_number]
        elem[j].elem_no = element_number

        unique_node_number_for_node1 = elemArray[j-1,2]
        unique_node_number_for_node2 = elemArray[j-1,3]
        unique_node_number_for_node3 = elemArray[j-1,4]
        unique_node_number_for_node4 = elemArray[j-1,5]
        if is_quadratic:
            unique_node_number_for_node5 = elemArray[j-1,6]
            unique_node_number_for_node6 = elemArray[j-1,7]
            unique_node_number_for_node7 = elemArray[j-1,8]
            unique_node_number_for_node8 = elemArray[j-1,9]
        else:
            unique_node_number_for_node5 = 0
            unique_node_number_for_node6 = 0
            unique_node_number_for_node7 = 0
            unique_node_number_for_node8 = 0

        elem[j].node1 = node_list[unique_node_number_for_node1]
        elem[j].node2 = node_list[unique_node_number_for_node2]
        elem[j].node3 = node_list[unique_node_number_for_node3]
        elem[j].node4 = node_list[unique_node_number_for_node4]
        elem[j].node5 = node_list[unique_node_number_for_node5]
        elem[j].node6 = node_list[unique_node_number_for_node6]
        elem[j].node7 = node_list[unique_node_number_for_node7]
        elem[j].node8 = node_list[unique_node_number_for_node8]
        elem[j].node9 = node_list[0]
    return


## find the "middle" x&y coordinates of this element
##    input: single_element <object>, a single element object (e.g. elem[1])
##    output: x_middle <double>, x2-coordinate of the middle of this element
##            y_middle <double>, x3-coordinate of the middle of this element
def findMiddleCoordinatesOfElement(single_element):
    x1 = single_element.node1.x2
    x2 = single_element.node2.x2
    x3 = single_element.node3.x2
    x4 = single_element.node4.x2
    y1 = single_element.node1.x3
    y2 = single_element.node2.x3
    y3 = single_element.node3.x3
    y4 = single_element.node4.x3
    x_middle = (x1 + x2 + x3 + x4)/4.0
    y_middle = (y1 + y2 + y3 + y4)/4.0
    return (x_middle, y_middle)

## determine if the nodes are ordered according to the VABS convention
##     node 1 (bottom left corner) of this element
##     node 2 (bottom right corner) of this element
##     node 3 (top right corner) of this element
##     node 4 (top left corner) of this element
##     input: single_element <object>, a single element object (e.g. elem[1])
##     output: nodes_sorted <logical>, a flag that is True when the nodes are ordered according to the VABS convention
def areNodesSortedByVABSconvention(single_element):
    (x_middle, y_middle) = findMiddleCoordinatesOfElement(single_element)

    x1 = single_element.node1.x2
    x2 = single_element.node2.x2
    x3 = single_element.node3.x2
    x4 = single_element.node4.x2
    y1 = single_element.node1.x3
    y2 = single_element.node2.x3
    y3 = single_element.node3.x3
    y4 = single_element.node4.x3
    
    node1_flag = (x1 < x_middle) and (y1 < y_middle)
    node2_flag = (x2 > x_middle) and (y2 < y_middle)
    node3_flag = (x3 > x_middle) and (y3 > y_middle)
    node4_flag = (x4 < x_middle) and (y4 > y_middle)

    nodes_sorted = node1_flag and node2_flag and node3_flag and node4_flag
    # print node1_flag, node2_flag, node3_flag, node4_flag
    return nodes_sorted


## reassign the nodes on a single element according to the VABS convention
##     node 1 (bottom left corner) of this element
##     node 2 (bottom right corner) of this element
##     node 3 (top right corner) of this element
##     node 4 (top left corner) of this element
##     input: single_element <object>, a single element object (e.g. elem[1])
##     output: <none>
def reassignNodesOnElement(single_element):
    (x_middle, y_middle) = findMiddleCoordinatesOfElement(single_element)

    def updateNodeFlags(one_element):
        n1_flag = (one_element.node1.x2 < x_middle) and (one_element.node1.x3 < y_middle)
        n2_flag = (one_element.node2.x2 > x_middle) and (one_element.node2.x3 < y_middle)
        n3_flag = (one_element.node3.x2 > x_middle) and (one_element.node3.x3 > y_middle)
        n4_flag = (one_element.node4.x2 < x_middle) and (one_element.node4.x3 > y_middle)
        return (n1_flag, n2_flag, n3_flag, n4_flag)

    (node1_flag, node2_flag, node3_flag, node4_flag) = updateNodeFlags(single_element)
    counter1 = 0
    counter2 = 0
    counter3 = 0

    while (node1_flag == False) and (counter1 <= 10):
        temp = single_element.node4  # temporarily store the node assigned to the 4th position
        single_element.node4 = single_element.node1
        single_element.node1 = single_element.node2
        single_element.node2 = single_element.node3
        single_element.node3 = temp
        counter1 = counter1 + 1
        (node1_flag, node2_flag, node3_flag, node4_flag) = updateNodeFlags(single_element)
        
    while (node2_flag == False) and (counter2 <= 10):
        temp = single_element.node4  # temporarily store the node assigned to the 4th position
        single_element.node4 = single_element.node2
        single_element.node2 = single_element.node3
        single_element.node3 = temp
        counter2 = counter2 + 1
        (node1_flag, node2_flag, node3_flag, node4_flag) = updateNodeFlags(single_element)
        
    while (node3_flag == False) and (counter3 <= 10):
        temp = single_element.node4  # temporarily store the node assigned to the 4th position
        single_element.node4 = single_element.node3
        single_element.node3 = temp
        counter3 = counter3 + 1
        (node1_flag, node2_flag, node3_flag, node4_flag) = updateNodeFlags(single_element)
        
    (node1_flag, node2_flag, node3_flag, node4_flag) = updateNodeFlags(single_element)
    # print node1_flag, node2_flag, node3_flag, node4_flag
    return


## reassign nodes on all elements that don't follow the VABS convention
##    input: nelem <int>, number of elements in this grid
##           elem <object>, list of element objects
##    output: <none>
def reassignNodesOnAllBadElements(nelem, elem):
    for j in range(1,nelem+1):
        sorted_node_flag = areNodesSortedByVABSconvention(elem[j])
        if (sorted_node_flag == False):
            reassignNodesOnElement(elem[j])
            sorted_node_flag = areNodesSortedByVABSconvention(elem[j])
        # print elem[j].elem_no, sorted_node_flag
    return

## updated version of reassignNodesOnAllBadElements()
def reorderBadElements(nelem, elem):
    reorder_OK = True
    for j in range(1,nelem+1):
        if not elem[j].is_ccw():
            elem[j].reorient()
            if not elem[j].is_ccw():
                print '  ***WARNING*** element #' + str(elem[j].elem_no) + ' was not properly reoriented!'
                reorder_OK = False
    return reorder_OK

## assign upper and lower borders to each element object
##    ...this will aid with filling in cells with different colors
##    input: nelem <int>, number of elements in this grid
##           elem <object>, list of element objects
##    output: <none>
def assignBordersToElements(nelem, elem):
    for i in range(1,nelem+1):  # traverse the list of element objects
        # assign the upper border y-coordinates (node4, node3)
        elem[i].upper_border_y = [elem[i].node4.x3, elem[i].node3.x3]
        # assign the lower border y-coordinates (node1, node2)
        elem[i].lower_border_y = [elem[i].node1.x3, elem[i].node2.x3]
        # assign the lower border x-coordinates (node1, node2)
        elem[i].lower_border_x = [elem[i].node1.x2, elem[i].node2.x2]
    return


## rewrite connectivity array, based on reassigned nodes [see reassignNodesOnAllBadElements()]
##    input: nelem <int>, the number of elements in this grid
##           elem <object>, the list of element objects
##           connectivity <array>, a numpy array of node numbers describing the connectivity of each element
##    output: <none>
def rewriteConnectivity(nelem, elem, connectivity):
    for i in range(1,nelem+1):  # traverse the list of element objects
        connectivity[i-1,0] = elem[i].node1.node_no
        connectivity[i-1,1] = elem[i].node2.node_no
        connectivity[i-1,2] = elem[i].node3.node_no
        connectivity[i-1,3] = elem[i].node4.node_no
    return





## define x-coordinate boundaries of spar caps and shear webs
##    (all dimensions have units of meters)
##    input: w_sc <double>, width of the spar cap
##           w_sw_biax <double>, width of the biaxial layer of the shear web
##           w_sw_foam <double>, width of the foam layer of the shear web
##    output: xa <double>, # x-coordinate of uniax-biax boundary (right edge of spar cap/left edge of shear web)
##            xb <double>, # x-coordinate of int_biax-foam boundary (right edge of interior biax layer/left edge of foam in shear web)
##            xc <double>, # x-coordinate of foam-ext_biax boundary (right edge of foam/left edge of exterior biax layer in shear web)
##            xd <double>, # x-coordinate of ext_biax boundary (right edge of exterior biax layer in shear web)
def defineSparCapShearWebBoundaries(w_sc, w_sw_biax, w_sw_foam):
    xa = w_sc/2.0        # uniax-biax boundary (right edge of spar cap/left edge of shear web)
    xb = xa + w_sw_biax  # int_biax-foam boundary (right edge of interior biax layer/left edge of foam in shear web)
    xc = xb + w_sw_foam  # foam-ext_biax boundary (right edge of foam/left edge of exterior biax layer in shear web)
    xd = xc + w_sw_biax  # ext_biax boundary (right edge of exterior biax layer in shear web)
    return (xa, xb, xc, xd)


## define y-coordinate boundary between spar cap and root buildup
##    input: h_sw <double>, height of the shear web
##           h_rb <double>, height of the root buildup
##    output: ya <double>, y-coordinate of boundary between spar cap and root buildup
def defineSparCapRootBuildupBoundary(h_sw, h_rb):
    ya = h_sw/2.0 - h_rb
    return ya


## define the thickness of each layer in a particular laminate
##    input: thick_laminate <double>, thickness of the entire laminate
##           nlayer_laminate <int>, the number of layers in the entire laminate
##    output: thick_layer <double>, thickness of each layer in the laminate
def defineLayerThickness(thick_laminate, nlayer_laminate):
    thick_layer = thick_laminate/nlayer_laminate
    return thick_layer


## calculate layer thicknesses for all laminates
def calcLayerThicknessesForAllLaminates(t_uniax,      t_biax,      t_triax,
                                        nlayer_uniax, nlayer_biax, nlayer_triax):
    t_uniax_layer = defineLayerThickness(t_uniax, nlayer_uniax)
    t_biax_layer  = defineLayerThickness(t_biax,  nlayer_biax )
    t_triax_layer = defineLayerThickness(t_triax, nlayer_triax)
    return (t_uniax_layer, t_biax_layer, t_triax_layer)


## find out if all four coordinates are within two bounds
##    ...coordinates are either x or y-coordinates, NOT coordinate pairs
##    input: c1 <double>, first coordinate
##           c2 <double>, second coordinate
##           c3 <double>, third coordinate
##           c4 <double>, fourth coordinate
##           c_lower <double>, lower bound coordinate
##           c_upper <double>, upper boundh coordinate
##    output: flag <logical>, true if all four coordinates are within bounds, false otherwise
def allFourCoordsAreWithinBounds(c1, c2, c3, c4, c_lower, c_upper):
    if c_upper < c_lower:
        temp = c_upper
        c_upper = c_lower
        c_lower = temp
        print "WARNING: c_upper < c_lower ... values have been automatically switched!"
    
    if ((c_lower <= c1 and c1 <= c_upper) and (c_lower <= c2 and c2 <= c_upper) and (c_lower <= c3 and c3 <= c_upper) and (c_lower <= c4 and c4 <= c_upper)):
        # all four coordinates ARE within the two bounds
        flag = True
    else:
        # all four coordinates are NOT within the two bounds
        flag = False
    return flag


## find out if one coordinate is within two bounds
##    ...coordinate is either x or y-coordinate, NOT a coordinate pair
##    input: c <double>, coordinate to test
##           c_lower <double>, lower bound coordinate
##           c_upper <double>, upper boundh coordinate
##    output: flag <logical>, true if coordinate is within bounds, false otherwise
def coordIsWithinBounds(c, c_lower, c_upper):
    if c_upper < c_lower:
        temp = c_upper
        c_upper = c_lower
        c_lower = temp
        print "WARNING: c_upper < c_lower ... values have been automatically switched!"
    
    if (c_lower <= c and c <= c_upper):
        # all four coordinates ARE within the two bounds
        flag = True
    else:
        # all four coordinates are NOT within the two bounds
        flag = False
    return flag


## find out if the middle coordinate of an element is within two bounds
##    ...coordinate is either x or y-coordinate, NOT a coordinate pair
##    input: single_element <object>, one element in the grid
##           lower_bound <double>, lower bound coordinate
##           upper_bound <double>, upper boundh coordinate
##           x_flag <logical>, true if lower_bound and upper_bound are x-coordinates, false if they are y-coordinates
##    output: result_flag <logical>, true if coordinate is within bounds, false otherwise
def middleCoordIsWithinBounds(single_element, lower_bound, upper_bound, x_flag):
    (x_m, y_m) = findMiddleCoordinatesOfElement(single_element)
    if x_flag:
        if coordIsWithinBounds(x_m, lower_bound, upper_bound):
            result_flag = True
        else:
            result_flag = False
    else:
        if coordIsWithinBounds(y_m, lower_bound, upper_bound):
            result_flag = True
        else:
            result_flag = False
    return result_flag


## determine which elements are made of which materials
##    input: w_sc <double>, width of the spar cap
##           w_sw_biax <double>, width of the biaxial laminate of the shear web
##           w_sw_foam <double>, width of the foam region of the shear web
##           h_sw <double>, height of the shear web
##           h_rb <double>, height of the root buildup
##           nelem <int>, number of elements in this grid
##    output: <none>
def defineLayerForEachElement(w_sc, w_sw_biax, w_sw_foam, h_sw, h_rb, nelem, elem, t_uniax, t_biax, t_triax, layer_list):
    (xa, xb, xc, xd) = defineSparCapShearWebBoundaries(w_sc, w_sw_biax, w_sw_foam)
    ya = defineSparCapRootBuildupBoundary(h_sw, h_rb)

    for j in range(1,nelem+1):  # traverse the array of element objects
        x1 = elem[j].node1.x2
        y1 = elem[j].node1.x3
        x2 = elem[j].node2.x2
        y2 = elem[j].node2.x3
        x3 = elem[j].node3.x2
        y3 = elem[j].node3.x3
        x4 = elem[j].node4.x2
        y4 = elem[j].node4.x3

        # uniaxial/triaxial GFRP
        if middleCoordIsWithinBounds(elem[j], -xa, xa, True):
            if middleCoordIsWithinBounds(elem[j], -ya, ya, False):
                # spar cap, uniaxial GFRP
                elem[j].layer = layer_list[1]  # layer_no = 1
                if ( (y1 >= 0) and (y2 >= 0) and (y3 >= 0) and (y4 >= 0) ):
                    # top spar cap
                    elem[j].theta1 = 0.0
                else:
                    # bottom spar cap
                    elem[j].theta1 = 180.0
            else:
                # root buildup, triaxial GFRP
                if ( (y1 >= 0) and (y2 >= 0) and (y3 >= 0) and (y4 >= 0) ):
                    # top root buildup
                    elem[j].theta1 = 0.0
                    if middleCoordIsWithinBounds(elem[j], ya+0.0*t_triax, ya+1.0*t_triax, False):
                        elem[j].layer = layer_list[4]  # layer_no = 4
                    elif middleCoordIsWithinBounds(elem[j], ya+1.0*t_triax, ya+2.0*t_triax, False):
                        elem[j].layer = layer_list[5]  # layer_no = 5
                    elif middleCoordIsWithinBounds(elem[j], ya+2.0*t_triax, ya+3.0*t_triax, False):
                        elem[j].layer = layer_list[4]  # layer_no = 4
                    elif middleCoordIsWithinBounds(elem[j], ya+3.0*t_triax, ya+4.0*t_triax, False):
                        elem[j].layer = layer_list[5]  # layer_no = 5
                    else:  # all y-coords >= ya+4.0*t_triax
                        elem[j].layer = layer_list[6]  # layer_no = 6
                        if not middleCoordIsWithinBounds(elem[j], ya+4.0*t_triax, h_sw/2.0, False):
                            print "WARNING: element # " + str(elem[j].elem_no) + " may have been assigned incorrect layer"
                else:
                    # bottom root buildup
                    elem[j].theta1 = 180.0
                    if middleCoordIsWithinBounds(elem[j], -ya-1.0*t_triax, -ya-0.0*t_triax, False):
                        elem[j].layer = layer_list[4]  # layer_no = 4
                    elif middleCoordIsWithinBounds(elem[j], -ya-2.0*t_triax, -ya-1.0*t_triax, False):
                        elem[j].layer = layer_list[5]  # layer_no = 5
                    elif middleCoordIsWithinBounds(elem[j], -ya-3.0*t_triax, -ya-2.0*t_triax, False):
                        elem[j].layer = layer_list[4]  # layer_no = 4
                    elif middleCoordIsWithinBounds(elem[j], -ya-4.0*t_triax, -ya-3.0*t_triax, False):
                        elem[j].layer = layer_list[5]  # layer_no = 5
                    else:  # all y-coords <= -ya-4.0*t_triax
                        elem[j].layer = layer_list[6]  # layer_no = 6
                        if not middleCoordIsWithinBounds(elem[j], -h_sw/2.0, -ya-4.0*t_triax, False):
                            print "WARNING: element # " + str(elem[j].elem_no) + " may have been assigned incorrect layer"
        
        # biaxial GFRP
        if middleCoordIsWithinBounds(elem[j], xa, xb, True):
            # right shear web, internal biaxial laminate
            elem[j].theta1 = 270.0
            if middleCoordIsWithinBounds(elem[j], xa+0.0*t_biax, xa+1.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], xa+1.0*t_biax, xa+2.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            elif middleCoordIsWithinBounds(elem[j], xa+2.0*t_biax, xa+3.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], xa+3.0*t_biax, xa+4.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            elif middleCoordIsWithinBounds(elem[j], xa+4.0*t_biax, xa+5.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], xa+5.0*t_biax, xa+6.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            elif middleCoordIsWithinBounds(elem[j], xa+6.0*t_biax, xa+7.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], xa+7.0*t_biax, xb, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            else:
                print "WARNING: element # " + str(elem[j].elem_no) + " may have been assigned incorrect layer"
        elif middleCoordIsWithinBounds(elem[j], xc, xd, True):
            # right shear web, external biaxial laminate
            elem[j].theta1 = 270.0
            if middleCoordIsWithinBounds(elem[j], xc+0.0*t_biax, xc+1.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], xc+1.0*t_biax, xc+2.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            elif middleCoordIsWithinBounds(elem[j], xc+2.0*t_biax, xc+3.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], xc+3.0*t_biax, xc+4.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            elif middleCoordIsWithinBounds(elem[j], xc+4.0*t_biax, xc+5.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], xc+5.0*t_biax, xc+6.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            elif middleCoordIsWithinBounds(elem[j], xc+6.0*t_biax, xc+7.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], xc+7.0*t_biax, xd, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            else:
                print "WARNING: element # " + str(elem[j].elem_no) + " may have been assigned incorrect layer"
        elif middleCoordIsWithinBounds(elem[j], -xb, -xa, True):
            # left shear web, internal biaxial laminate
            elem[j].theta1 = 90.0   
            if middleCoordIsWithinBounds(elem[j], -xa-1.0*t_biax, -xa-0.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], -xa-2.0*t_biax, -xa-1.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            elif middleCoordIsWithinBounds(elem[j], -xa-3.0*t_biax, -xa-2.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], -xa-4.0*t_biax, -xa-3.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            elif middleCoordIsWithinBounds(elem[j], -xa-5.0*t_biax, -xa-4.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], -xa-6.0*t_biax, -xa-5.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            elif middleCoordIsWithinBounds(elem[j], -xa-7.0*t_biax, -xa-6.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], -xb, -xa-7.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            else:
                print "WARNING: element # " + str(elem[j].elem_no) + " may have been assigned incorrect layer"
        elif middleCoordIsWithinBounds(elem[j], -xd, -xc, True):
            # left shear web, external biaxial laminate
            elem[j].theta1 = 90.0
            if middleCoordIsWithinBounds(elem[j], -xc-1.0*t_biax, -xc-0.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], -xc-2.0*t_biax, -xc-1.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            elif middleCoordIsWithinBounds(elem[j], -xc-3.0*t_biax, -xc-2.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], -xc-4.0*t_biax, -xc-3.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            elif middleCoordIsWithinBounds(elem[j], -xc-5.0*t_biax, -xc-4.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], -xc-6.0*t_biax, -xc-5.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            elif middleCoordIsWithinBounds(elem[j], -xc-7.0*t_biax, -xc-6.0*t_biax, True):
                elem[j].layer = layer_list[2]  # layer_no = 2
            elif middleCoordIsWithinBounds(elem[j], -xd, -xc-7.0*t_biax, True):
                elem[j].layer = layer_list[3]  # layer_no = 3
            else:
                print "WARNING: element # " + str(elem[j].elem_no) + " may have been assigned incorrect layer"
        
        # foam
        if middleCoordIsWithinBounds(elem[j], xb, xc, True):
            # right shear web
            elem[j].layer = layer_list[7]  # layer_no = 7
            elem[j].theta1 = 270.0
        elif middleCoordIsWithinBounds(elem[j], -xc, -xb, True):
            # left shear web
            elem[j].layer = layer_list[7]  # layer_no = 7
            elem[j].theta1 = 90.0
        
    return