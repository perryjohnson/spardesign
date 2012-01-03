import numpy as np
import VABSobjects as vo


def genElementMap(number_of_rows,number_of_columns,number_of_elements,number_of_nodes,element,unique_node):
	# number_of_elements = number_of_rows * number_of_columns
	# number_of_nodes = (number_of_rows+1) * (number_of_columns+1)

	a = np.array( range(1, number_of_nodes+1) )
	b = np.reshape(a, (number_of_rows+1, number_of_columns+1), order='F')
	c = b[ ::-1,:]  # equivalent to MATLAB's "flipud" function

	# print a
	# print ''
	# print c
	# print ''

	n = 1  # initialize counter for element number
	for row in range(number_of_rows):
		for col in range(number_of_columns):
			# print c[row+1,col], c[row+1,col+1], c[row,col+1], c[row,col]
			element[n].elem_no = n
			(node1_no, node2_no, node3_no, node4_no) = (c[row+1,col], c[row+1,col+1], c[row,col+1], c[row,col])
			(element[n].node1, element[n].node2, element[n].node3, element[n].node4) = (unique_node[node1_no], unique_node[node2_no], unique_node[node3_no], unique_node[node4_no])
			# print element[n].node1, element[n].node2, element[n].node3, element[n].node4
			n = n+1
	return element

if __name__ == '__main__':   # if run, not imported
	## initialize number of rows and columns ##
	nrows = 1  # number of element rows
	ncols = 1  # number of element columns

	## calculate the number of elements and nodes for this region ##
	num_elements = nrows * ncols
	num_nodes = (nrows+1) * (ncols+1)

	## initialize objects for the VABSobjects module ##
	unique_node = []  # create an empty list of node objects
	element = []      # create an empty list of element objects

	## call functions from the VABSobjects module ##
	vo.fillNodeObjects(num_nodes, unique_node)
	vo.fillElementObjects(num_elements, element)

	## fill list of node objects ##
	for i in range(1,num_nodes+1):
		unique_node[i].node_no = i
	(unique_node[1].x2, unique_node[1].x3) = (0.0, 0.0)
	(unique_node[2].x2, unique_node[2].x3) = (0.0, 1.0)
	(unique_node[3].x2, unique_node[3].x3) = (1.0, 0.0)
	(unique_node[4].x2, unique_node[4].x3) = (1.0, 1.0)

	## generate the element map, and store it in the list of element objects ##
	element = genElementMap(nrows,ncols,num_elements,num_nodes,element,unique_node)

	## check if the function correctly assigned the element connectivity ##
	for i in range(1,num_elements+1):
		print element[i].node1.node_no, element[i].node2.node_no, element[i].node3.node_no, element[i].node4.node_no
	
	print element[1].node1.x2, element[1].node1.x3