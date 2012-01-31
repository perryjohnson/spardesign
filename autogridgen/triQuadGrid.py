import numpy as np
import VABSobjects as vo
from mayavi import mlab

### helps keep track of a region's location (e.g. shear web biax, spar cap, etc.)
class regionObj():
    region_no = np.nan
    H_cells = np.nan            # number of cells distributed along horizontal axis
    V_cells = np.nan            # number of cells distributed along vertical axis
    cornerNode1 = vo.nodeObj()  # bottom left corner of region
    cornerNode2 = vo.nodeObj()  # bottom right corner of region
    cornerNode3 = vo.nodeObj()  # top right corner of region
    cornerNode4 = vo.nodeObj()  # top left corner of region
    edgeB = []                  # list of nodes along bottom edge
    edgeR = []                  # list of nodes along right edge
    edgeT = []                  # list of nodes along top edge
    edgeL = []                  # list of nodes along left edge
    name = ''                   # name of this region


### prints the list of nodes (node number, x2, x3) to screen
###     input:  number_of_nodes <int>, number of nodes in the list `node`
###             node <object>, list of node objects
###     output: printed list of nodes to the screen
def printNodeList(number_of_nodes, node):
    print "NODES:"
    for i in range(1,number_of_nodes+1):
        print '#' + str(node[i].node_no) + '  (' + str(node[i].x2) + ', ' + str(node[i].x3) + ')'


###
def printElementNodes(number_of_elements, element):
    print "ELEMENTS:"
    for i in range(1,number_of_elements+1):
        print ('#' + str(element[i].elem_no) + '  [' + str(element[i].node1.node_no) + ', '
                                                     + str(element[i].node2.node_no) + ', '
                                                     + str(element[i].node3.node_no) + ', '
                                                     + str(element[i].node4.node_no) + ']')


### fill index 0 of node, element, and region lists (index 0 is unused)
def fillUnusedZeroIndex(node, element, region):
    node.append(vo.nodeObj())
    node[0].node_no = 0  # dummy node, assigned to element[i].node4 to tell VABS that element[i] is a triangular element
    element.append(vo.elementObj())
    region.append(regionObj())
    return (node, element, region)


### create a new node
def createNewNode(number_of_nodes, node):
    node.append(vo.nodeObj())
    number_of_nodes += 1
    node[number_of_nodes].node_no = number_of_nodes
    return (number_of_nodes, node)


### create a new element
def createNewElement(number_of_elements, element):
    element.append(vo.elementObj())
    number_of_elements += 1
    element[number_of_elements].elem_no = number_of_elements
    return (number_of_elements, element)


def newMayaviFigure():
    mlab.figure(1, size=(800, 600), bgcolor=(1, 1, 1))
    mlab.clf()


def nice2Dview():
    mlab.view(0, 0, 25, np.array([6.2, 2.5, 0.0]))
    mlab.show()


def buildMayaviDataSource(node,number_of_nodes):
    x = [np.nan]
    y = [np.nan]
    z = [np.nan]
    for i in range(1,number_of_nodes+1):
        x.append(node[i].x2)
        y.append(node[i].x3)
        z.append(0.0)
    src = mlab.pipeline.scalar_scatter(x, y, z)
    return src


def buildConnections(element,number_of_elements):
    connections = np.empty((1,2), dtype=int)  # initialize the array with a dummy row, so we can use np.vstack
    for i in range(1,number_of_elements+1):
        conn1 = np.array([element[i].node1.node_no, element[i].node2.node_no])
        conn2 = np.array([element[i].node2.node_no, element[i].node3.node_no])
        if (element[i].node4.node_no != 0):  # quadrilateral element
            conn3 = np.array([element[i].node3.node_no, element[i].node4.node_no])
            conn4 = np.array([element[i].node4.node_no, element[i].node1.node_no])
            connections = np.vstack((connections,conn1,conn2,conn3,conn4))
        else:  # triangular element
            conn3 = np.array([element[i].node3.node_no, element[i].node1.node_no])
            connections = np.vstack((connections,conn1,conn2,conn3))
    connections = connections[1:,:]  # delete the first row
    return connections


def plotNodes(node,number_of_nodes,line_flag=False,connections=np.array([])):
    newMayaviFigure()
    src = buildMayaviDataSource(node,number_of_nodes)
    mlab.pipeline.glyph(src, color=(0,0,0), mode='2dcircle', scale_factor='0.1')
    if line_flag:
        src.mlab_source.dataset.lines = connections
        mlab.pipeline.surface(src, line_width=1, opacity=1.0, color=(0,0,0))
    nice2Dview()
    showAxes()


def showAxes():
    mlab.axes( color=(0,0,0),
               extent=[0.0, 14.0, 0.0, 14.0, 0.0, 0.0],
               line_width=1.0,
               nb_labels=8,
               x_axis_visibility=True,
               xlabel='x2',
               y_axis_visibility=False,
               ylabel='x3',
               z_axis_visibility=True )
    mlab.orientation_axes()


### make new nodes along the edge of the specified region
###     input:  region <object>, list of region objects (with EMPTY edge lists)
###             region_no <int>, the region number that is under consideration
###             node <object>, list of node objects
###             number_of_nodes <int>, number of nodes in the list `node`
###             edge <string>, the edge that nodes will be created along
###     output: region <object>, list of region objects (with UPDATED edge lists)
###             node <object>, list of node objects (with ADDED nodes along region edges)
###             number_of_nodes <int>, number of nodes in the list `node` (updated to account for new nodes)
def makeEdgeNodes(region, region_no, node, number_of_nodes, edge):
    if (edge == 'bottom' or edge == 'Bottom' or edge == 'BOTTOM' or edge == 'b' or edge == 'B'):
        region[region_no].edgeB = []
        # add bottom left corner node to list for bottom edge
        region[region_no].edgeB.append(region[region_no].cornerNode1)
        tempEdge = np.linspace(region[region_no].cornerNode1.x2,
                               region[region_no].cornerNode2.x2,
                               region[region_no].H_cells+1)
        # create new boundary nodes, but exclude first and last entries of tempEdge
        #   (so we don't double-count nodes)
        for i in range(1,len(tempEdge)-1):
            node.append(vo.nodeObj())
            number_of_nodes += 1
            node[number_of_nodes].node_no = number_of_nodes
            node[number_of_nodes].x2 = tempEdge[i]
            node[number_of_nodes].x3 = region[region_no].cornerNode1.x3
            # add node to list for bottom edge
            region[region_no].edgeB.append(node[number_of_nodes])
        # add bottom right corner node to list for bottom edge
        region[region_no].edgeB.append(region[region_no].cornerNode2)
    
    elif (edge == 'top' or edge == 'Top' or edge == 'TOP' or edge == 't' or edge == 'T'):
        region[region_no].edgeT = []
        # add top left corner node to list for top edge
        region[region_no].edgeT.append(region[region_no].cornerNode4)
        tempEdge = np.linspace(region[region_no].cornerNode4.x2,
                               region[region_no].cornerNode3.x2,
                               region[region_no].H_cells+1)
        # create new boundary nodes, but exclude first and last entries of tempEdge
        #   (so we don't double-count nodes)
        for i in range(1,len(tempEdge)-1):
            node.append(vo.nodeObj())
            number_of_nodes += 1
            node[number_of_nodes].node_no = number_of_nodes
            node[number_of_nodes].x2 = tempEdge[i]
            node[number_of_nodes].x3 = region[region_no].cornerNode4.x3
            # add node to list for bottom edge
            region[region_no].edgeT.append(node[number_of_nodes])
        # add top right corner node to list for top edge
        region[region_no].edgeT.append(region[region_no].cornerNode3)

    elif (edge == 'left' or edge == 'Left' or edge == 'LEFT' or edge == 'l' or edge == 'L'):
        region[region_no].edgeL = []
        # add bottom left corner node to list for left edge
        region[region_no].edgeL.append(region[region_no].cornerNode1)
        tempEdge = np.linspace(region[region_no].cornerNode1.x3,
                               region[region_no].cornerNode4.x3,
                               region[region_no].V_cells+1)
        # create new boundary nodes, but exclude first and last entries of tempEdge
        #   (so we don't double-count nodes)
        for i in range(1,len(tempEdge)-1):
            node.append(vo.nodeObj())
            number_of_nodes += 1
            node[number_of_nodes].node_no = number_of_nodes
            node[number_of_nodes].x3 = tempEdge[i]
            node[number_of_nodes].x2 = region[region_no].cornerNode1.x2
            # add node to list for bottom edge
            region[region_no].edgeL.append(node[number_of_nodes])
        # add top left corner node to list for left edge
        region[region_no].edgeL.append(region[region_no].cornerNode4)

    elif (edge == 'right' or edge == 'Right' or edge == 'RIGHT' or edge == 'r' or edge == 'R'):
        region[region_no].edgeR = []
        # add bottom right corner node to list for right edge
        region[region_no].edgeR.append(region[region_no].cornerNode2)
        tempEdge = np.linspace(region[region_no].cornerNode2.x3,
                               region[region_no].cornerNode3.x3,
                               region[region_no].V_cells+1)
        # create new boundary nodes, but exclude first and last entries of tempEdge
        #   (so we don't double-count nodes)
        for i in range(1,len(tempEdge)-1):
            node.append(vo.nodeObj())
            number_of_nodes += 1
            node[number_of_nodes].node_no = number_of_nodes
            node[number_of_nodes].x3 = tempEdge[i]
            node[number_of_nodes].x2 = region[region_no].cornerNode2.x2
            # add node to list for bottom edge
            region[region_no].edgeR.append(node[number_of_nodes])
        # add top left corner node to list for left edge
        region[region_no].edgeR.append(region[region_no].cornerNode3)
    
    else:
        print "ERROR: edge must be left, right, top, or bottom"
    return (region, node, number_of_nodes)


def genEdgeNodeNumbers(edge):
    edgeList = []
    for i in range(len(edge)):
        edgeList.append(edge[i].node_no)
    return edgeList


def printEdgeNodes(region, region_no):
    print "REGION #" + str(region_no) + "   ********************"
    print "BOTTOM EDGE, node_no:"
    edgeList = genEdgeNodeNumbers(region[region_no].edgeB)
    print edgeList

    print "TOP EDGE, node_no:"
    edgeList = genEdgeNodeNumbers(region[region_no].edgeT)
    print edgeList

    print "LEFT EDGE, node_no:"
    edgeList = genEdgeNodeNumbers(region[region_no].edgeL)
    print edgeList

    print "RIGHT EDGE, node_no:"
    edgeList = genEdgeNodeNumbers(region[region_no].edgeR)
    print edgeList


### fills the boundary of a coarse-resolution region with triangular elements to bridge to an adjacent fine-resolution region
###     input:  coarse_region_no <int>, the identifying number of the coarse-resolution region to be filled
###             fine_region_no <int>, the identifying number of the adjacent, fine-resolution region
###             region <object>, list of region objects
###             number_of_elements <int>, the number of elements created so far
###             element <object>, list of element objects
###             number_of_nodes <int>, the number of nodes created so far
###             node <object>, list of node objects
###     output: number_of_elements <int>, the UPDATED number of elements created, including ones made by this function
###             element <object>, list of UPDATED element objects, including ones made by this function
###             number_of_nodes <int> the UPDATED number of nodes created, including ones made by this function
###             node <object>, list of UPDATED node objects, including ones made by this function
def fillBoundaryTriElements(coarse_region_no, fine_region_no, region, number_of_elements, element, number_of_nodes, node):
    temp_edgeL = region[coarse_region_no].edgeL
    temp_edgeB = region[coarse_region_no].edgeB
    temp_edgeT = region[coarse_region_no].edgeT
    temp_edgeR = region[coarse_region_no].edgeR
    fine_v = region[fine_region_no].V_cells       # number of cells distributed along vertical axis of fine-res region
    coarse_v = region[coarse_region_no].V_cells   # number of cells distributed along vertical axis of coarse-res region
    coarse_dv = (temp_edgeT[1].x3 - temp_edgeB[1].x3)/coarse_v
    print "coarse_dv =", coarse_dv
    new_coarseEdge = []

    temp_node1 = temp_edgeB[0]
    temp_node2 = temp_edgeB[1]
    # temp_node3 = ? # need to assign this
    temp_node4 = node[0]  # dummy node, tells VABS this is a triangular element
    new_coarseEdge.append(temp_node2)

    for j in range(0,fine_v,2):
        temp_node3 = region[coarse_region_no].edgeL[j+1]
        # bottom triangular element ######################################################
        (number_of_elements, element) = createNewElement(number_of_elements,element)
        element[number_of_elements].node1 = temp_node1
        element[number_of_elements].node2 = temp_node2
        element[number_of_elements].node3 = temp_node3
        element[number_of_elements].node4 = temp_node4

        # middle triangular element ######################################################
        temp_node1 = temp_node3
        # temp_node2 = temp_node2 # same, for this element
        # temp_node3 = ? # need to create this
        # temp_node4 = node[0] # same, denotes tri element
        if (j != range(0,fine_v,2)[-1]):  # if we are not at the top edge...
            ## ...create element.node3
            (number_of_nodes, node) = createNewNode(number_of_nodes, node)
            node[number_of_nodes].x2 = temp_node2.x2
            node[number_of_nodes].x3 = temp_node2.x3 + coarse_dv
            temp_node3 = node[number_of_nodes]
        else:  # otherwise...
            #...reuse the top edge node for element.node3
            temp_node3 = region[coarse_region_no].edgeT[1]
        (number_of_elements, element) = createNewElement(number_of_elements,element)
        element[number_of_elements].node1 = temp_node1
        element[number_of_elements].node2 = temp_node2
        element[number_of_elements].node3 = temp_node3
        element[number_of_elements].node4 = temp_node4
        new_coarseEdge.append(temp_node3)

        # top triangular element ######################################################
        # temp_node1 = temp_node1 # same, for this element
        temp_node2 = temp_node3
        temp_node3 = region[coarse_region_no].edgeL[j+2]
        # temp_node4 = node[0] # same, denotes tri element
        (number_of_elements, element) = createNewElement(number_of_elements,element)
        element[number_of_elements].node1 = temp_node1
        element[number_of_elements].node2 = temp_node2
        element[number_of_elements].node3 = temp_node3
        element[number_of_elements].node4 = temp_node4

        # update nodes for next iteration
        temp_node1 = temp_node3
        # temp_node2 = temp_node2 # same, for this element

    return (number_of_elements, element, number_of_nodes, node, new_coarseEdge)


### fills the boundary of a coarse-resolution region with triangular elements to bridge to an adjacent fine-resolution region
### ### VERSION 2 ###
###     input:  coarse_region_no <int>, the identifying number of the coarse-resolution region to be filled
###             fine_region_no <int>, the identifying number of the adjacent, fine-resolution region
###             region <object>, list of region objects
###             number_of_elements <int>, the number of elements created so far
###             element <object>, list of element objects
###             number_of_nodes <int>, the number of nodes created so far
###             node <object>, list of node objects
###     output: number_of_elements <int>, the UPDATED number of elements created, including ones made by this function
###             element <object>, list of UPDATED element objects, including ones made by this function
###             number_of_nodes <int> the UPDATED number of nodes created, including ones made by this function
###             node <object>, list of UPDATED node objects, including ones made by this function
def fillBoundaryTriElements2(coarse_region_no, fine_region_no, region, number_of_elements, element, number_of_nodes, node):
    temp_edgeL = region[coarse_region_no].edgeL
    temp_edgeB = region[coarse_region_no].edgeB
    temp_edgeT = region[coarse_region_no].edgeT
    fine_v = region[fine_region_no].V_cells       # number of cells distributed along vertical axis of fine-res region
    coarse_v = region[coarse_region_no].V_cells   # number of cells distributed along vertical axis of coarse-res region
    coarse_dv = (temp_edgeT[1].x3 - temp_edgeB[1].x3)/coarse_v
    print "coarse_dv =", coarse_dv
    new_coarseEdge = []

    ## make temp_edgeR, based on the coarse-res region spacing
    new_coarseEdge.append(temp_edgeB[1])
    for k in range(1,coarse_v):
        (number_of_nodes, node) = createNewNode(number_of_nodes, node)
        node[number_of_nodes].x2 = temp_edgeB[1].x2
        node[number_of_nodes].x3 = temp_edgeB[1].x3 + k*coarse_dv
        new_coarseEdge.append(node[number_of_nodes])
    new_coarseEdge.append(temp_edgeT[1])
    temp_edgeR = new_coarseEdge

    l = 0
    r = 0
    temp_node4 = node[0]  # dummy node, tells VABS this is a triangular element
    while (l < len(temp_edgeL)-1) and (r < len(temp_edgeR)-1):
        print "l =", l
        print "r =", r
        # check if the RIGHT node is between the two LEFT nodes
        if (temp_edgeL[l].x3 <= temp_edgeR[r].x3) and (temp_edgeR[r].x3 <= temp_edgeL[l+1].x3):
            # make a triangle (which points right)!
            temp_node1 = temp_edgeL[l]
            temp_node2 = temp_edgeR[r]
            temp_node3 = temp_edgeL[l+1]
            l += 1
        # check if the LEFT node is between the two RIGHT nodes
        elif (temp_edgeR[r].x3 <= temp_edgeL[l].x3) and (temp_edgeL[l].x3 <= temp_edgeR[r+1].x3):
            # make a triangle (which points left)!
            temp_node1 = temp_edgeL[l]
            temp_node2 = temp_edgeR[r]
            temp_node3 = temp_edgeR[r+1]
            r += 1
        # check if the RIGHT node is above the two LEFT nodes
        elif (temp_edgeL[l].x3 <= temp_edgeR[r].x3) and (temp_edgeL[l+1].x3 <= temp_edgeR[r].x3):
            # make a triangle (which points right)!
            temp_node1 = temp_edgeL[l]
            temp_node2 = temp_edgeR[r]
            temp_node3 = temp_edgeL[l+1]
            l += 1
        # check if the LEFT node is above the two RIGHT nodes   ... do i need this one?!!??
        elif (temp_edgeR[r].x3 <= temp_edgeL[l].x3) and (temp_edgeR[r+1].x3 <= temp_edgeL[l].x3):
            # make a triangle (which points left)!
            temp_node1 = temp_edgeL[l]
            temp_node2 = temp_edgeR[r]
            temp_node3 = temp_edgeR[r+1]
            r += 1
        else:
            print "ERROR!!! HELP!!!"
            break
        (number_of_elements, element) = createNewElement(number_of_elements, element)
        element[number_of_elements].node1 = temp_node1
        element[number_of_elements].node2 = temp_node2
        element[number_of_elements].node3 = temp_node3
        element[number_of_elements].node4 = temp_node4

    # still need to fill in a few more triangular elements near the top edge
    # temp_node2 = temp_edgeT[1] ... always!
    while (l < len(temp_edgeL)-1):
        temp_node1 = temp_edgeL[l]
        temp_node2 = temp_edgeT[1]
        temp_node3 = temp_edgeL[l+1]
        l += 1
        (number_of_elements, element) = createNewElement(number_of_elements, element)
        element[number_of_elements].node1 = temp_node1
        element[number_of_elements].node2 = temp_node2
        element[number_of_elements].node3 = temp_node3
        element[number_of_elements].node4 = temp_node4

    # # still need to make the last triangular element at the top edge
    # temp_node1 = temp_edgeL[-2]
    # temp_node2 = temp_edgeT[1]
    # temp_node3 = temp_edgeL[-1]
    # (number_of_elements, element) = createNewElement(number_of_elements, element)
    # element[number_of_elements].node1 = temp_node1
    # element[number_of_elements].node2 = temp_node2
    # element[number_of_elements].node3 = temp_node3
    # element[number_of_elements].node4 = temp_node4

    return (number_of_elements, element, number_of_nodes, node, new_coarseEdge)


### fills the interior of a region with quadrilateral elements
###     input:  region_no <int>, the identifying number of the region to be filled
###             region <object>, list of region objects
###             number_of_elements <int>, the number of elements created so far
###             element <object>, list of element objects
###             number_of_nodes <int>, the number of nodes created so far
###             node <object>, list of node objects
###     output: number_of_elements <int>, the UPDATED number of elements created, including ones made by this function
###             element <object>, list of UPDATED element objects, including ones made by this function
###             number_of_nodes <int> the UPDATED number of nodes created, including ones made by this function
###             node <object>, list of UPDATED node objects, including ones made by this function
def fillInteriorQuadElements(region_no, region, number_of_elements, element, number_of_nodes, node):
    temp_edgeL = region[region_no].edgeL
    temp_edgeB = region[region_no].edgeB
    temp_edgeT = region[region_no].edgeT
    temp_edgeR = region[region_no].edgeR
    v = region[region_no].V_cells       # number of cells distributed along vertical axis of region 1
    h = region[region_no].H_cells       # number of cells distributed along horizontal axis of region 1
    new_edgeL = []

    for i in range(h):
        # update temp nodes on bottom edge, as we move right (horizontally)
        temp_node1 = temp_edgeB[i]
        temp_node2 = temp_edgeB[i+1]
        new_edgeL.append(temp_node2)
        for j in range(v):
            # update temp node on left edge, as we move up (vertically)
            temp_node4 = temp_edgeL[j+1]

            (number_of_elements, element) = createNewElement(number_of_elements, element)
            element[number_of_elements].node1 = temp_node1
            element[number_of_elements].node2 = temp_node2
            element[number_of_elements].node4 = temp_node4
            if (i < range(h)[-1]):   # if we haven't reached the right edge yet...
                if (j < range(v)[-1]):   # if we haven't reached the top edge yet...
                    # ...we need to create a new node for element.node3
                    (number_of_nodes, node) = createNewNode(number_of_nodes, node)
                    node[number_of_nodes].x2 = temp_node2.x2
                    node[number_of_nodes].x3 = temp_node4.x3
                    temp_node3 = node[number_of_nodes]
                    # update temp nodes on bottom edge, as we move up (vertically)
                    temp_node1 = temp_node4
                    temp_node2 = temp_node3
                else:   # otherwise...
                    # ...we need to assign element.node3 to a node on the top edge
                    temp_node3 = temp_edgeT[i+1]
            else:  # otherwise...
                # ...we need to assign element.node3 to a node on the right edge
                temp_node3 = temp_edgeR[j+1]
                # update temp nodes on bottom edge, as we move up (vertically)
                temp_node1 = temp_node4
                temp_node2 = temp_node3
            element[number_of_elements].node3 = temp_node3
            new_edgeL.append(temp_node3)
        temp_edgeL = new_edgeL
        new_edgeL = []
    return (number_of_elements, element, number_of_nodes, node)


if __name__ == '__main__':
    node = []
    element = []
    region = []
    number_of_nodes = 0
    number_of_elements = 0
    number_of_regions = 0

    # fill index 0 of node, element, and region lists (index 0 is unused)
    (node, element, region) = fillUnusedZeroIndex(node, element, region)

    # fill in nodes at 8 corners
    for i in range(1,9):
        node.append(vo.nodeObj())
        node[i].node_no = i
        number_of_nodes += 1
    # assign coordinates at 8 corners
    (node[1].x2, node[1].x3) = (0.0, 0.0)
    (node[2].x2, node[2].x3) = (3.0, 0.0)
    (node[3].x2, node[3].x3) = (3.0, 6.0)
    (node[4].x2, node[4].x3) = (0.0, 6.0)
    (node[5].x2, node[5].x3) = (11.0, 0.0)
    (node[6].x2, node[6].x3) = (14.0, 0.0)
    (node[7].x2, node[7].x3) = (14.0, 6.0)
    (node[8].x2, node[8].x3) = (11.0, 6.0)


    # fill in 3 regions
    for i in range(1,4):
        region.append(regionObj())
        region[i].region_no = i
        number_of_regions += 1
    # name regions
    region[1].name = 'left'
    region[2].name = 'middle'
    region[3].name = 'right'
    # assign number of cells distributed along horizontal axis
    region[1].H_cells = 3
    region[2].H_cells = 4
    region[3].H_cells = 3
    # assign number of cells distributed along vertical axis
    #       this will be autofilled by maxAR method (later)
    region[1].V_cells = 16
    region[2].V_cells = 4
    region[3].V_cells = 6
    # assign corner nodes to each region
    (region[1].cornerNode1, region[1].cornerNode2, region[1].cornerNode3, region[1].cornerNode4) = (node[1], node[2], node[3], node[4])
    (region[2].cornerNode1, region[2].cornerNode2, region[2].cornerNode3, region[2].cornerNode4) = (node[2], node[5], node[8], node[3])
    (region[3].cornerNode1, region[3].cornerNode2, region[3].cornerNode3, region[3].cornerNode4) = (node[5], node[6], node[7], node[8])
    # verify that input was saved correctly
    print "REGIONS:"
    for i in range(1,number_of_regions+1):
        print ('#' + str(region[i].region_no) + '  (' + str(region[i].cornerNode1.node_no) + ', '
                                                      + str(region[i].cornerNode2.node_no) + ', '
                                                      + str(region[i].cornerNode3.node_no) + ', '
                                                      + str(region[i].cornerNode4.node_no) + ')' )
    # make control nodes at ply boundaries
    # region 1
    (region, node, number_of_nodes) = makeEdgeNodes(region, 1, node, number_of_nodes, 'bottom')
    (region, node, number_of_nodes) = makeEdgeNodes(region, 1, node, number_of_nodes, 'top')
    (region, node, number_of_nodes) = makeEdgeNodes(region, 1, node, number_of_nodes, 'left')
    (region, node, number_of_nodes) = makeEdgeNodes(region, 1, node, number_of_nodes, 'right')

    # region 3
    (region, node, number_of_nodes) = makeEdgeNodes(region, 3, node, number_of_nodes, 'bottom')
    (region, node, number_of_nodes) = makeEdgeNodes(region, 3, node, number_of_nodes, 'top')
    (region, node, number_of_nodes) = makeEdgeNodes(region, 3, node, number_of_nodes, 'left')
    (region, node, number_of_nodes) = makeEdgeNodes(region, 3, node, number_of_nodes, 'right')

    # region 2
    (region, node, number_of_nodes) = makeEdgeNodes(region, 2, node, number_of_nodes, 'bottom')
    (region, node, number_of_nodes) = makeEdgeNodes(region, 2, node, number_of_nodes, 'top')
    region[2].edgeL = region[1].edgeR
    region[2].edgeR = region[3].edgeL

    printEdgeNodes(region, 1)
    printEdgeNodes(region, 2)
    printEdgeNodes(region, 3)

    (number_of_elements,element,number_of_nodes,node) = fillInteriorQuadElements(1,region,
                                                                                 number_of_elements,element,
                                                                                 number_of_nodes,node)
    # (number_of_elements,element,number_of_nodes,node) = fillInteriorQuadElements(2,region,
    #                                                                              number_of_elements,element,
    #                                                                              number_of_nodes,node)
    # (number_of_elements,element,number_of_nodes,node) = fillInteriorQuadElements(3,region,
    #                                                                              number_of_elements,element,
    #                                                                              number_of_nodes,node)

    # (number_of_elements, element, number_of_nodes, node, coarseEdge) = fillBoundaryTriElements(2, 1, region, number_of_elements, element, number_of_nodes, node)
    # print "COARSE EDGE:"
    # edgeList = genEdgeNodeNumbers(coarseEdge)
    # print edgeList

    (number_of_elements, element, number_of_nodes, node, coarseEdge) = fillBoundaryTriElements2(2, 1, region, number_of_elements, element, number_of_nodes, node)
    print "COARSE EDGE:"
    edgeList = genEdgeNodeNumbers(coarseEdge)
    print edgeList


















    conn = buildConnections(element,number_of_elements)

    # verify that input was saved correctly
    # plotNodes(node,number_of_nodes)
    plotNodes(node,number_of_nodes,line_flag=True,connections=conn)
    # printElementNodes(number_of_elements,element)
