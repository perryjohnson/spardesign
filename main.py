import truegrid.ABAQUSutilities as au

outputfile = 'truegrid/spar_station_04_output.txt'
(nodeArray, elemArray, nnode, nelem) = au.parseABAQUS(outputfile, debug_flag=True)