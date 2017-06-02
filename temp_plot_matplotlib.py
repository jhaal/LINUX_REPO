#!/usr/bin/env python
#!/usr/local/lib/python3 

import os
from os.path import basename 
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import Tkinter,tkFileDialog , tkMessageBox
root = Tkinter.Tk()
root.withdraw()
filename = tkFileDialog.askopenfile(title = '@@@@@@@@ FUEL PLOTS @@@@@@@@@' , mode='r')
name = os.path.splitext(os.path.basename(filename.name))[0]

######## Convert string data read from file to float for plotting #########

A = [map(float,num.split()) for num in filename.readlines()[15:]]
  
######### Plot utility using matplotlib ######## 

plt.plot(A)
plt.legend()
plt.show()



