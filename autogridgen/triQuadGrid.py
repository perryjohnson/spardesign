import numpy as np
import VABSobjects as vo

### helps keep track of a region's location (e.g. shear web biax, spar cap, etc.)
class regionObj():
    region_no = np.nan
    H_cells = np.nan            # number of cells distributed along horizontal axis
    V_cells = np.nan            # number of cells distributed along vertical axis
    cornerNode1 = vo.nodeObj()
    cornerNode2 = vo.nodeObj()
    cornerNode3 = vo.nodeObj()
    cornerNode4 = vo.nodeObj()
    edgeB = []
    edgeR = []
    edgeT = []
    edgeL = []


### prints the list of nodes (node number, x2, x3) to screen
###     input:  number_of_nodes <int>, number of nodes in the list `node`
###             node <object>, list of node objects
###     output: printed list of nodes to the screen
def printNodeList(number_of_nodes, node):
    print "NODES:"
    for i in range(1,number_of_nodes+1):
        print '#' + str(node[i].node_no) + '  (' + str(node[i].x2) + ', ' + str(node[i].x3) + ')'

if __name__ == '__main__':
    node = []
    element = []
    region = []
    number_of_nodes = 0
    number_of_elements = 0
    number_of_regions = 0

    # fill index 0 of node, element, and region lists (index 0 is unused)
    node.append(vo.nodeObj())
    element.append(vo.elementObj())
    region.append(regionObj())

    # fill in nodes at 8 corners
    for i in range(1,9):
        node.append(vo.nodeObj())
        node[i].node_no = i
        number_of_nodes += 1
    # assign coordinates at 8 corners
    (node[1].x2, node[1].x3) = (0.0, 0.0)
    (node[2].x2, node[2].x3) = (3.0, 0.0)
    (node[3].x2, node[3].x3) = (3.0, 5.0)
    (node[4].x2, node[4].x3) = (0.0, 5.0)
    (node[5].x2, node[5].x3) = (11.0, 0.0)
    (node[6].x2, node[6].x3) = (14.0, 0.0)
    (node[7].x2, node[7].x3) = (14.0, 5.0)
    (node[8].x2, node[8].x3) = (11.0, 5.0)
    # verify that input was saved correctly
    printNodeList(number_of_nodes, node)


    # fill in 3 regions
    for i in range(1,4):
        region.append(regionObj())
        region[i].region_no = i
        number_of_regions += 1
    # assign number of cells distributed along horizontal axis
    region[1].H_cells = 3
    region[2].H_cells = 4
    region[3].H_cells = 3
    # assign number of cells distributed along vertical axis
    #       this will be autofilled by maxAR method (later)
    region[1].V_cells = 5
    # region[2].V_cells = ?
    region[3].V_cells = 5
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
    # bottom edge of region 1
    region[1].edgeB.append(region[1].cornerNode1)    # add bottom left corner node to list for bottom edge
    tempEdge = np.linspace(region[1].cornerNode1.x2, region[1].cornerNode2.x2, region[1].H_cells+1)
    for i in range(1,len(tempEdge)-1):  # exclude first and last entries of tempEdge (so we don't double-count nodes)
        node.append(vo.nodeObj())
        number_of_nodes += 1
        node[number_of_nodes].node_no = number_of_nodes
        node[number_of_nodes].x2 = tempEdge[i]
        node[number_of_nodes].x3 = region[1].cornerNode1.x3
        region[1].edgeB.append(node[number_of_nodes])           # add node to list for bottom edge
    region[1].edgeB.append(region[1].cornerNode2)    # add bottom right corner node to list for bottom edge

    print "BOTTOM EDGE, x2:"
    print region[1].edgeB[0].node_no, region[1].edgeB[1].node_no, region[1].edgeB[2].node_no, region[1].edgeB[3].node_no
    # verify that input was saved correctly
    printNodeList(number_of_nodes, node)
