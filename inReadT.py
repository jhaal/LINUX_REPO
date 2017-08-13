import os
import subprocess
from subprocess import call

'''Change Directory and enter cfwaro folder'''
os.chdir('/home/user01/OpenFOAM/OpenFOAM-4.1/applications/solvers/mySolvers/icoFoamTemp/cavityTemp/channelPHWR540/0/cfwaro/')
subprocess.call(['./CFWARO_t4'])
'''Open file FuelTempICMS created from cfwaro for reading '''
f = open('FuelTempICMS', 'r')
line = f.readline().rstrip()[3 - 8:]
line1 = float(line)
# print(line)
line11 = f.readline().rstrip()[3 - 8:]
line11a = float(line11)
# print(line1)
line21 = f.readline().rstrip()[3 - 8:]
line21a = float(line21)
# print(line2)
line31 = f.readline().rstrip()[3 - 8:]
line31a = float(line31)
# print(line)
line41 = f.readline().rstrip()[3 - 8:]
line41a = float(line41)
# print(line)
line51 = f.readline().rstrip()[3 - 8:]
line51a = float(line51)
# print(line)
line61 = f.readline().rstrip()[3 - 8:]
line61a = float(line61)
# print(line)
line71 = f.readline().rstrip()[3 - 8:]
line71a = float(line71)
# print(line)
line81 = f.readline().rstrip()[3 - 8:]
line81a = float(line81)
# print(line)
line91 = f.readline().rstrip()[3 - 8:]
line91a = float(line91)
# print(line)
line101 = f.readline().rstrip()[3 - 8:]
line101a = float(line101)
# print(line)
line111 = f.readline().rstrip()[3 - 8:]
line111a = float(line111)
# print(line)
line121 = f.readline().rstrip()[3 - 8:]
line121a = float(line121)
# print(line)
line131 = f.readline().rstrip()[3 - 8:]
line131a = float(line131)
# print(line131a)
f.close()
''' Change directory and enter the folder 0/ for creating the "T" file for OpenFOAM'''
os.chdir('/home/user01/OpenFOAM/OpenFOAM-4.1/applications/solvers/mySolvers/icoFoamTemp/cavityTemp/channelPHWR540/0/')
infile = open('T', 'w+')
''' Open "T" to write and Formatting of "T" file starts here'''
infile.write('/*--------------------------------*- C++ -*------------------------------------------*\\\
\n| ========|                                                                           |\n\
| \\      /  F ield              | OpenFOAM: The Open Source CFD Toolbox               |\n\
|  \\    /   O peration          | Version:  4.x                                       |\n\
|   \\  /    A nd                | Web:      www.OpenFOAM.org                          |\n\
|    \\/     M anipulation       |                                                     |\n\
\*-----------------------------------------------------------------------------------*/\n')
infile.write('FoamFile')
infile.write('\n{')
infile.write('\n\tversion\t\t\t2.0;')
infile.write('\n\tformat\t\t\tascii;')
infile.write('\n\tclass\t\t\tvolScalarField;')
infile.write('\n\tobject\t\t\tT;')
infile.write('\n}\n')
infile.write(
    '// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n')
infile.write('\n')
infile.write('dimensions      [0 0 0 1 0 0 0];\n')
infile.write('\n')
infile.write('internalField   uniform %3.1f;\n' % 260)
infile.write('\n')
infile.write('boundaryField\n')
infile.write('{\n')
infile.write('\toutlet\n')
infile.write('\t{\n')
infile.write('\ttype')
infile.write('\t\t zeroGradient ;\n')
infile.write('\t}\n')
infile.write('\tinlet\n')
infile.write('\t{\n')
infile.write('\ttype')
infile.write('\t\t fixedValue ;\n')
infile.write('\tvalue')
infile.write('\t\t uniform %3.1f;\n' % 260)
infile.write('\t}\n')
infile.write('\tring_1\n')
infile.write('\t{\n')
infile.write('\ttype')
infile.write('\t\t fixedValue ;\n')
infile.write('\tvalue')
infile.write('\t\t uniform %3.1f;\n' % line1)
infile.write('\t}\n')
infile.write('\tring_2\n')
infile.write('\t{\n')
infile.write('\ttype')
infile.write('\t\t fixedValue ;\n')
infile.write('\tvalue')
infile.write('\t\t uniform %3.1f;\n' % line1)
infile.write('\t}\n')
infile.write('\tring_3\n')
infile.write('\t{\n')
infile.write('\ttype')
infile.write('\t\t fixedValue ;\n')
infile.write('\tvalue')
infile.write('\t\t uniform %3.1f;\n' % line1)
infile.write('\t}\n')
infile.write('\tring_4\n')
infile.write('\t{\n')
infile.write('\ttype')
infile.write('\t\t fixedValue ;\n')
infile.write('\tvalue')
infile.write('\t\t uniform %3.1f;\n' % line1)
infile.write('\t}\n')
infile.write('\tpt\n')
infile.write('\t{\n')
infile.write('\ttype')
infile.write('\t\t fixedValue ;\n')
infile.write('\tvalue')
infile.write('\t\t uniform %3.1f;\n' % 260)
infile.write('\t}\n')
infile.write('\twalls\n')
infile.write('\t{\n')
infile.write('\ttype')
infile.write('\t\t empty ;\n')
infile.write('\t}\n')
infile.write('}\n')
infile.write(
    '//* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *// \n')
infile.close()
os.chdir('/home/user01/OpenFOAM/OpenFOAM-4.1/applications/solvers/mySolvers/icoFoamTemp/cavityTemp/channelPHWR540/')
subprocess.call('./FoamRun')
