#!/usr/local/lib/python3.4

import os
import sys
import io
from os.path import basename
import matplotlib.pyplot as plt
import tkinter
from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()
filename = filedialog.askopenfile(title = '@@@@@@@@ FUEL PLOTS @@@@@@@@@' , mode='r')
#name = os.path.splitext(os.path.basename(filename.name))[0]
for line in filename.readlines()[15:]:
    line2 = line.split()
    #print(line2)
    plt.plot(line2,'ro')
    #for lines in data:
    #    print(lines )

  #a = line.replace('\n','')
  #data = a.split('\t\t')
  #rad = data[0:]
  #temp = data[1:]
  #print(rad)
  #plt.plot(rad,'r-*')
  
plt.ylabel('Temparature')
plt.xlabel('Radius')
#plt.legend('Fuel Plot')
#plt.savefig(filename = name)
plt.show()





'''
g.hardcopy(
  filename=name,
  terminal='pdf'
  )
'''


