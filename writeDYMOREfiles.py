import truegrid.read_layup as rl
import DYMORE.DYMOREutilities as du


def writeBeamPropertyDefinition(fName, spar_stn_list, beam_property_name, property_definition_type, coordinate_type, comments, print_flag=False):
    """
    Write the DYMORE-formatted @BEAM_PROPERTY_DEFINITION code block to a file.

    Parameters
    ----------
    fName : <string>
        A filename. The beam property definition code block will be saved here.
    spar_stn_list : <list of ints>
        A list of stations whose properties will be included in this code block.
    beam_property_name : <string>
        The label associated with this beam property definition.
    property_definition_type : <string>
        The format of the properties.
        Acceptable values are: 'SECTIONAL_PROPERTIES',
                               '6X6_MATRICES', or
                               'PROPERTY_TABLES' 
    coordinate_type : <string>
        The format of coordinates along the span of the beam.
        Acceptable values are: 'ETA_COORDINATE',
                               'CURVILINEAR_COORDINATE', or
                               'AXIAL_COORDINATE'
    comments : <string>
        The user-defined comment associated with this code block.
    print_flag : <logical>
        Set to True to print debugging information to the screen.

    Returns
    -------
    <none> (However, a file is written to hard disk.)
    """

    dymoreMKfile = du.makeFile(dymore_MKblock_filename)

    tab = '  '

    # write the header for the beam property definition
    dymoreMKfile.write('@BEAM_PROPERTY_DEFINITION {\n')
    dymoreMKfile.write(tab*1 + '@BEAM_PROPERTY_NAME {' + beam_property_name + '} {\n')
    dymoreMKfile.write(tab*2 +   '@PROPERTY_DEFINITION_TYPE {' + property_definition_type + '}\n')
    dymoreMKfile.write(tab*2 +   '@COORDINATE_TYPE {' + coordinate_type + '}\n')
    dymoreMKfile.write(tab*2 +   '\n')

    # write the mass and stiffness matrices for the beam property definition
    for n in range(len(spar_stn_list)):
        spar_station = spar_stn_list[n]
        if spar_station < 10:
            basefilestr = 'spar_station_0' + str(spar_station)
        else:
            basefilestr = 'spar_station_' + str(spar_station)

        if print_flag:
            print ''
            print '***************'
            print basefilestr
            print '***************'

        # ----------------------------------------------------------------------------------

        stationData = rl.extractStationData(data,spar_station)
        if stationData['spar station'] < 10:
            sparstnstr = '0' + str(stationData['spar station'])
        else:
            sparstnstr = str(stationData['spar station'])
        vabsMK = 'VABS/M_and_K_matrices/spar_station_' + sparstnstr + '.dat.K'
        du.writeMKmatrices(dymoreMKfile, vabsMK, stationData, CoordType=coordinate_type, debug_flag=False)

    # write the footer for the beam property definition
    dymoreMKfile.write(tab*2 + '@COMMENTS {' + comments + '}\n')
    dymoreMKfile.write(tab*1 + '}\n')
    dymoreMKfile.write('}\n')

    # close the file, which now contains the complete beam property defintion
    dymoreMKfile.close()

    return


if __name__ == '__main__':  #run this code if called directly from the command line (good for debugging)
    print_flag = False

    data = rl.readLayupFile('truegrid/monoplane_spar_layup.txt')

    spar_stn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]  # generate a DYMORE code block for these spar stations
    # spar_stn_list = [10]  # generate a DYMORE code block for these spar stations

    # ----------------------------------------------------------------------------------
    # BEAM PROPERTY DEFINITION
    # ------------------------

    # the beam property definition code block will be saved to this filename:
    dymore_MKblock_filename = 'dymoreMKblock.dat'

    # define settings for the beam property definition
    beam_property_name = 'propSpar'
    property_definition_type = '6X6_MATRICES'
    coordinate_type = 'AXIAL_COORDINATE'
    comments = du.formatComments('beam properties are from dymoreMKblock.dat')

    writeBeamPropertyDefinition(dymore_MKblock_filename, spar_stn_list, beam_property_name, property_definition_type, coordinate_type, comments)

    # ----------------------------------------------------------------------------------
    # ORIENTATION DISTRIBUTION DEFINITION
    # -----------------------------------

    # the orientation distribution definition code block will be saved to this filename:
    dymore_orientationblock_filename = 'dymoreOrientationBlock.dat'
    dymoreOrientationFile = du.makeFile(dymore_orientationblock_filename)

    # define settings for the orientation distribution definition
    orientation_distribution_name = 'orientationSpar'
    orientation_definition_type = 'TWIST_ANGLE'
    # coordinate_type = 'AXIAL_COORDINATE'   ## this is already defined above by the beam property definition ##
    untwisted = True

    CoordType = coordinate_type

    # @ORIENTATION_DISTRIBUTION_DEFINITION {
    #   @ORIENTATION_DISTRIBUTION_NAME { orientationSpar } {
    #     @ORIENTATION_DEFINITION_TYPE { TWIST_ANGLE }
    #     @COORDINATE_TYPE { ETA_COORDINATE }
    #     @ETA_COORDINATE {0.00000e+00} 
    #     @TWIST_ANGLE {0.0}

    #     @ETA_COORDINATE {2.17628e-03}
    #     @TWIST_ANGLE {0.0}


    tab = '  '

    # write the header for the orientation distribution definition
    dymoreOrientationFile.write('@ORIENTATION_DISTRIBUTION_DEFINITION {\n')
    dymoreOrientationFile.write(tab*1 + '@ORIENTATION_DISTRIBUTION_NAME {' + orientation_distribution_name + '} {\n')
    dymoreOrientationFile.write(tab*2 +   '@ORIENTATION_DEFINITION_TYPE {' + orientation_definition_type + '}\n')
    dymoreOrientationFile.write(tab*2 +   '@COORDINATE_TYPE {' + coordinate_type + '}\n')
    # dymoreOrientationFile.write(tab*2 +   '\n')


    # write the mass and stiffness matrices for the beam property definition
    for n in range(len(spar_stn_list)):
        spar_station = spar_stn_list[n]
        if spar_station < 10:
            basefilestr = 'spar_station_0' + str(spar_station)
        else:
            basefilestr = 'spar_station_' + str(spar_station)

        if print_flag:
            print ''
            print '***************'
            print basefilestr
            print '***************'

        # ----------------------------------------------------------------------------------

        stationData = rl.extractStationData(data,spar_station)
        if stationData['spar station'] < 10:
            sparstnstr = '0' + str(stationData['spar station'])
        else:
            sparstnstr = str(stationData['spar station'])

        if CoordType == 'ETA_COORDINATE':
            dymoreOrientationFile.write(tab*2 + '@ETA_COORDINATE {' + ('%11.5e' % stationData['eta']) + '}\n')
        elif CoordType == 'CURVILINEAR_COORDINATE':
            # f.write(tab*2 + '@CURVILINEAR_COORDINATE {' + ('%11.5e' % coord) + '}\n')
            print "***WARNING*** CURVILINEAR_COORDINATE feature is not yet supported."
        elif CoordType == 'AXIAL_COORDINATE':
            dymoreOrientationFile.write(tab*2 + '@AXIAL_COORDINATE {' + ('%11.5e' % stationData['x1']) + '}\n')

        if untwisted:
            tw = 0.0
        else:
            tw = stationData['twist degrees']
        dymoreOrientationFile.write(tab*2 + '@TWIST_ANGLE {' + ('%11.5e' % tw) + '}\n')
        dymoreOrientationFile.write(tab*2 + '\n')

    # write the footer for the orientation distribution definition
    # dymoreOrientationFile.write(tab*2 + '@COMMENTS {' + comments + '}\n')
    dymoreOrientationFile.write(tab*1 + '}\n')
    dymoreOrientationFile.write('}\n')

    # close the file, which now contains the complete orientation distribution defintion
    dymoreOrientationFile.close()