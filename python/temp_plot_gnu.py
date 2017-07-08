#!/usr/bin/env python
#!/usr/local/lib/python3 

import os
from os.path import basename 
from numpy import *
import Gnuplot
from Gnuplot import *
import Tkinter,tkFileDialog , tkMessageBox
root = Tkinter.Tk()
root.withdraw()
filename = tkFileDialog.askopenfile(title = '@@@@@@@@ FUEL PLOTS @@@@@@@@@' , mode='r')
name = os.path.splitext(os.path.basename(filename.name))[0]

######## Convert string data read from file to float for plotting #########

A = [map(float,num.split()) for num in filename.readlines()[15:]]
  
######### Plot utility using Gnuplot ######## 

g=Gnuplot.Gnuplot(persist=1)
#g=Gnuplot.Gnuplot()
g.title('Fuel Temperature Variation')
g.xlabel('Distance(mm)')
g.ylabel('Temperature(Deg-Celsius)')
g('set grid')
data = Gnuplot.Data(A,with_ ='line',title="Fuel Temperature")
g.plot(data)
g('set term png')
g.hardcopy(
  filename=name,
  terminal = 'png',
  )
#g.replot
#g.hardcopy(
#  filename=name,
#  terminal='pdf'
#  )


