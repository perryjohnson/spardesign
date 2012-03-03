## read a file into memory
##    input: filestr <string>, the filename of the file to be read into memory
##    output: fileLines <list of strings>, a list of strings, each of which represents one line in the file
def readFile(filestr):
    f = open(filestr, 'r')  # read the file
    fileLines = f.readlines()  # parse all characters in file into one long string
    return fileLines


## define regular expressions to search for mass and stiffness matrices in VABS-formatted output file
##    input: <none>
##    output: nnPat <object>, regex pattern for 'nn'
def defineRegularExpressions():
    import re
    cm_x2_pat = re.compile(r'\s\sXm2 =.+')
    cm_x3_pat = re.compile(r'\s\sXm3 =.+')
    mpus_pat = re.compile(r'\sMass Per Unit Span\s+=.+')
    i1_pat = re.compile(r'\sMass Moments of Intertia about x1 axis\s+=.+')
    i2_pat = re.compile(r'\sMass Moments of Intertia about x2 axis\s+=.+')
    i3_pat = re.compile(r'\sMass Moments of Intertia about x3 axis\s+=.+')
    K_head_pat = re.compile(r'\sTimoshenko Stiffness Matrix.+')
    
    return (cm_x2_pat, cm_x3_pat, mpus_pat, i1_pat, i2_pat, i3_pat, K_head_pat)


if __name__ == '__main__':
    vabsMK = '../VABS/M_and_K_matrices/spar_station_01.dat.K'
    MKlines = readFile(vabsMK)
    (cm_x2_pat, cm_x3_pat, mpus_pat, i1_pat, i2_pat, i3_pat, K_head_pat) = defineRegularExpressions()

    for i in range(len(MKlines)):
        cm_x2_match = cm_x2_pat.match(MKlines[i])
        cm_x3_match = cm_x3_pat.match(MKlines[i])
        mpus_match = mpus_pat.match(MKlines[i])
        i1_match = i1_pat.match(MKlines[i])
        i2_match = i2_pat.match(MKlines[i])
        i3_match = i3_pat.match(MKlines[i])
        K_head_match = K_head_pat.match(MKlines[i])

        if cm_x2_match:
            cm_x2 = MKlines[i].replace('Xm2 =','')
        elif cm_x3_match:
            cm_x3 = MKlines[i].replace('Xm3 =','')
        elif mpus_match:
            mpus = MKlines[i].replace('Mass Per Unit Span                     =','')
        elif i1_match:
            i1 = MKlines[i].replace('Mass Moments of Intertia about x1 axis =','')
        elif i2_match:
            i2 = MKlines[i].replace('Mass Moments of Intertia about x2 axis =','')
        elif i3_match:
            i3 = MKlines[i].replace('Mass Moments of Intertia about x3 axis =','')
        elif K_head_match:
            K_head_line = i

    print cm_x2
    print cm_x3
    print mpus
    print i1
    print i2
    print i3
    print MKlines[K_head_line+3:K_head_line+9]