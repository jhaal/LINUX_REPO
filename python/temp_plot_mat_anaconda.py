#!/usr/local/lib/python3.4

import os
import sys
import io
from os.path import basename
import matplotlib.pyplot as plt
import tkinter
from tkinter import *
from tkinter import filedialog
import numpy
from numpy import *

#root = Tk()
#root.withdraw()
#filename = filedialog.askopenfile(title = '@@@@@@@@ FUEL PLOTS @@@@@@@@@' , mode='r')
#name = os.path.splitext(os.path.basename(filename.name))[0]
with open('iter.txt','r') as f:
    for line in f.readlines()[15:]:
        print(line)
        plt.plot(lines,'r-*')
        #a = array([line])
        #print  (a)
        #a = line.replace('\n','')
        #rad = a.split('\t\t')
        #rad = data[0:]
        #temp = data[1:]
        #print(rad,temp)
#for lines in line:
#plt.plot(lines,'r-*')
  
#plt.ylabel('Temparature')
#plt.xlabel('Radius')
#plt.legend('Fuel Plot')
#plt.savefig(filename = name)
#plt.show()





'''
g.hardcopy(
  filename=name,
  terminal='pdf'
  )
'''


