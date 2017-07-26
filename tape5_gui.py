#! /usr/bin/env python
#! /usr/bin/python3
#! /usr/local/lib/python3

import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, askopenfile
import string
from string import *
import random
import time
import os
from os import *
import sys
import subprocess
import io

############################### GUI SPECIFICATIONS START HERE ###########
class Window(Frame):
    def _init_(self, parent,**kwargs):
        Frame._init_(self, parent)

root = Tk()
root.configure(background='powder blue')

########################### BANNER DISP ################################
image = PhotoImage(file = 'npcil_logo.gif')
label = Label(image=image,bg='powder blue')
label.grid(row=0, column=0)
label = Label(text='TAPS-3&4 CORE FOLLOWUP',font=('arial',14),bg='powder blue',fg='red',anchor='w')
label.grid(row=1, column=0)
label= Label(text='CORE FOLLOWUP WITH AUTO REFUELING OPTION (CFWARO)',font=('arial',14),bg='powder blue',fg='red',
             anchor='w')
label.grid(row=2, column=0)
##################### tkinter window name ###########################
root.title("CORE FOLLOWUP WITH AUTO REFUELING OPTION")
########################## Time Display #############################
localtime = time.asctime(time.localtime(time.time()))
############################# FRAME GENERATION ######################
f1 = Frame(root, width = 1600, height = 4000, bg="powder blue", relief=SUNKEN)
f1.grid()
##################### buttons ########################

operator = ""
opentape5 = StringVar()
savetape5 = StringVar()
runtape5 = StringVar()
btnadd = StringVar()

def btnClick(string):
    global operator
    operator = ""
    # txt_Input1.set(operator)

def opentape5():
    with open('tape5','r') as f:
        text = f.read()
    first_line = text.split()[1]
    date = [str(first_line[5:15])]
    txtpow1.grid(row=0, column=1)
    txtpow1.insert(0,date)

    first_line = text.split()[4]
    unit =[int(first_line[0])]
    txtpow.grid(row=0, column=3)
    txtpow.insert(0,unit)

    first_line = text.split()[5]
    icase = [int(first_line[0:4])]
    txticase1.grid(row=8, column=0)
    txticase1.insert(0,icase)

    first_line = text.split()[6]
    isnap =[int(first_line[0])]
    txtisnap1.grid(row=8, column=1)
    txtisnap1.insert(0,isnap)

    first_line = text.split()[7]
    ndir =[int(first_line[0])]
    txtndir1.grid(row=8, column=2)
    txtndir1.insert(0,ndir)

    first_line = text.split()[8]
    noftyp =[int(first_line[0])]
    txtnoftyp1.grid(row=8, column=3)
    txtnoftyp1.insert(0,noftyp)

    first_line = text.split()[9]
    powercoeff =[int(first_line[0])]
    txtpowercoeff1.grid(row=8, column=4)
    txtpowercoeff1.insert(0,powercoeff)

    first_line = text.split()[10]
    xenon =[int(first_line[0])]
    txtxenon1.grid(row=8, column=5)
    txtxenon1.insert(0,xenon)

    first_line = text.split()[11]
    rhodium =[int(first_line[0])]
    txtrhodium1.grid(row=8, column=6)
    txtrhodium1.insert(0,rhodium)

    first_line = text.split()[95]
    modh =[float(first_line[0:6])]
    txtmodh1.grid(row=8, column=7)
    txtmodh1.insert(0,modh)

    first_line = text.split()[96]
    pfp =[float(first_line[0:6])]
    txtpfp1.grid(row=8, column=8)
    txtpfp1.insert(0,pfp)

    first_line = text.split()[97]
    guesstf =[float(first_line[0:5])]
    txtguesstf1.grid(row=6, column=6)
    txtguesstf1.insert(0,guesstf)

    first_line = text.split()[98]
    boron =[float(first_line[0:2])]
    txtboron1.grid(row=8, column=9)
    txtboron1.insert(0,boron)

    first_line = text.split()[99]
    xmu =[float(first_line[0:6])]
    txtxmu1.grid(row=6, column=7)
    txtxmu1.insert(0,xmu)

    first_line = text.split()[101]
    fpd =[str(first_line[0:5])]
    txtfpd1.grid(row=6, column=8)
    txtfpd1.insert(0,fpd)

    first_line = text.split()[44]
    ar1 =[float(first_line[0:3])]
    txtar01.grid(row=2, column=0)
    txtar01.insert(0,ar1)

    first_line = text.split()[45]
    ar2 =[float(first_line[0:3])]
    txtar21.grid(row=2, column=1)
    txtar21.insert(0,ar2)

    first_line = text.split()[46]
    ar3 =[float(first_line[0:3])]
    txtar31.grid(row=2, column=2)
    txtar31.insert(0,ar3)

    first_line = text.split()[47]
    ar4 =[float(first_line[0:3])]
    txtar41.grid(row=2, column=3)
    txtar41.insert(0,ar4)

    first_line = text.split()[48]
    ar5 =[float(first_line[0:3])]
    txtar51.grid(row=2, column=4)
    txtar51.insert(0,ar5)

    first_line = text.split()[49]
    ar6 =[float(first_line[0:3])]
    txtar61.grid(row=2, column=5)
    txtar61.insert(0,ar6)

    first_line = text.split()[50]
    ar7 =[float(first_line[0:3])]
    txtar71.grid(row=2, column=6)
    txtar71.insert(0,ar7)

    first_line = text.split()[51]
    ar8 =[float(first_line[0:3])]
    txtar81.grid(row=2, column=7)
    txtar81.insert(0,ar8)

    first_line = text.split()[52]
    ar9 =[float(first_line[0:3])]
    txtar91.grid(row=2, column=8)
    txtar91.insert(0,ar9)

    first_line = text.split()[53]
    ar10 =[float(first_line[0:3])]
    txtar101.grid(row=2, column=9)
    txtar101.insert(0,ar10)

    first_line = text.split()[54]
    ar11 =[float(first_line[0:3])]
    txtar111.grid(row=4, column=0)
    txtar111.insert(0,ar11)

    first_line = text.split()[55]
    ar12 =[float(first_line[0:3])]
    txtar121.grid(row=4, column=1)
    txtar121.insert(0,ar12)

    first_line = text.split()[56]
    ar13 =[float(first_line[0:3])]
    txtar131.grid(row=4, column=2)
    txtar131.insert(0,ar13)

    first_line = text.split()[57]
    ar14 =[float(first_line[0:3])]
    txtar141.grid(row=4, column=3)
    txtar141.insert(0,ar14)

    first_line = text.split()[58]
    ar15 =[float(first_line[0:3])]
    txtar151.grid(row=4, column=4)
    txtar151.insert(0,ar15)

    first_line = text.split()[59]
    ar16 =[float(first_line[0:3])]
    txtar161.grid(row=4, column=5)
    txtar161.insert(0,ar16)

    first_line = text.split()[60]
    ar17 =[float(first_line[0:3])]
    txtar171.grid(row=4, column=6)
    txtar171.insert(0,ar17)

    first_line = text.split()[62]
    cr1 =[float(first_line[0:3])]
    txtcr11.grid(row=6, column=0)
    txtcr11.insert(0,cr1)

    first_line = text.split()[63]
    cr2 =[float(first_line[0:3])]
    txtcr21.grid(row=6, column=1)
    txtcr21.insert(0,cr2)

    first_line = text.split()[64]
    cr3 =[float(first_line[0:3])]
    txtcr31.grid(row=6, column=2)
    txtcr31.insert(0,cr3)

    first_line = text.split()[65]
    cr4 =[float(first_line[0:3])]
    txtcr41.grid(row=6, column=3)
    txtcr41.insert(0,cr4)

    first_line = text.split()[67]
    sr1 =[float(first_line[0:20])]
    txtsr11.grid(row=6, column=4)
    txtsr11.insert(0,sr1)

    first_line = text.split()[81]
    sr2 =[str(first_line[0:20])]
    txtsr21.grid(row=6, column=5)
    txtsr21.insert(0,sr2)

    first_line = text.split()[28]
    zcc1 =[float(first_line[0:4])]
    txtzcc01.grid(row=10, column=0)
    txtzcc01.insert(0,zcc1)

    first_line = text.split()[36]
    zcc2 =[float(first_line[0:4])]
    txtzcc21.grid(row=10, column=1)
    txtzcc21.insert(0,zcc2)

    first_line = text.split()[22]
    zcc3 =[float(first_line[0:4])]
    txtzcc31.grid(row=10, column=2)
    txtzcc31.insert(0,zcc3)

    first_line = text.split()[29]
    zcc4 =[float(first_line[0:4])]
    txtzcc41.grid(row=10, column=3)
    txtzcc41.insert(0,zcc4)

    first_line = text.split()[37]
    zcc5 =[float(first_line[0:4])]
    txtzcc51.grid(row=10, column=4)
    txtzcc51.insert(0,zcc5)

    first_line = text.split()[30]
    zcc6 =[float(first_line[0:4])]
    txtzcc61.grid(row=10, column=5)
    txtzcc61.insert(0,zcc6)

    first_line = text.split()[38]
    zcc7 =[float(first_line[0:4])]
    txtzcc71.grid(row=10, column=6)
    txtzcc71.insert(0,zcc7)

    first_line = text.split()[31]
    zcc8 =[float(first_line[0:4])]
    txtzcc81.grid(row=10, column=7)
    txtzcc81.insert(0,zcc8)

    first_line = text.split()[39]
    zcc9 =[float(first_line[0:7])]
    txtzcc91.grid(row=10, column=8)
    txtzcc91.insert(0,zcc9)

    first_line = text.split()[23]
    zcc10 =[float(first_line[0:4])]
    txtzcc101.grid(row=10, column=9)
    txtzcc101.insert(0,zcc10)

    first_line = text.split()[32]
    zcc11 =[float(first_line[0:4])]
    txtzcc111.grid(row=12, column=0)
    txtzcc111.insert(0,zcc11)

    first_line = text.split()[40]
    zcc12 =[float(first_line[0:4])]
    txtzcc121.grid(row=12, column=1)
    txtzcc121.insert(0,zcc12)

    first_line = text.split()[33]
    zcc13 =[float(first_line[0:4])]
    txtzcc131.grid(row=12, column=2)
    txtzcc131.insert(0,zcc13)

    first_line = text.split()[41]
    zcc14 =[float(first_line[0:4])]
    txtzcc141.grid(row=12, column=3)
    txtzcc141.insert(0,zcc14)

    first_line = text.split()[110]
    ref =[str(first_line[0])]
    txtref1.grid(row=15, column=0)
    txtref1.insert(0,ref)

    first_line = text.split()[111]
    refid =[int(first_line[0:2])]
    txtrefid1.grid(row=15, column=1)
    txtrefid1.insert(0,refid)

    first_line = text.split()[112]
    bss =[int(first_line[0:3])]
    txtbss1.grid(row=15, column=2)
    txtbss1.insert(0,bss)

    first_line = text.split()[113]
    inp1 = [int(first_line[0:3])]
    second_line = text.split()[114]
    inpa1 = [int(second_line[0:3])]
    third_line = text.split()[115]
    inpb1 = [int(third_line[0:3])]
    txtinp01.grid(row=17, column=0)
    txtinp01.insert(0,inpb1)
    txtinp01.insert(0,inpa1)
    txtinp01.insert(0,inp1)

    first_line = text.split()[116]
    inp2 = [int(first_line[0:3])]
    second_line = text.split()[117]
    inpa2 = [int(second_line[0:3])]
    third_line = text.split()[118]
    inpb2 = [int(third_line[0:3])]
    txtinp21.grid(row=17, column=1)
    txtinp21.insert(0,inpb2)
    txtinp21.insert(0,inpa2)
    txtinp21.insert(0,inp2)


    first_line = text.split()[119]
    inp3 = [int(first_line[0:3])]
    second_line = text.split()[120]
    inpa3 = [int(second_line[0:3])]
    third_line = text.split()[121]
    inpb3 = [int(third_line[0:3])]
    txtinp31.grid(row=17, column=2)
    txtinp31.insert(0,inpb3)
    txtinp31.insert(0,inpa3)
    txtinp31.insert(0,inp3)

    first_line = text.split()[122]
    inp4 = [int(first_line[0:3])]
    second_line = text.split()[123]
    inpa4 = [int(second_line[0:3])]
    third_line = text.split()[124]
    inpb4 = [int(third_line[0:3])]
    txtinp41.grid(row=17, column=3)
    txtinp41.insert(0,inpb4)
    txtinp41.insert(0,inpa4)
    txtinp41.insert(0,inp4)

    first_line = text.split()[125]
    inp5 = [int(first_line[0:3])]
    second_line = text.split()[126]
    inpa5 = [int(second_line[0:3])]
    third_line = text.split()[127]
    inpb5 = [int(third_line[0:3])]
    txtinp51.grid(row=17, column=4)
    txtinp51.insert(0,inpb5)
    txtinp51.insert(0,inpa5)
    txtinp51.insert(0,inp5)

    first_line = text.split()[128]
    inp6 = [int(first_line[0:3])]
    second_line = text.split()[129]
    inpa6 = [int(second_line[0:3])]
    third_line = text.split()[130]
    inpb6 = [int(third_line[0:3])]
    txtinp61.grid(row=19, column=0)
    txtinp61.insert(0,inpb6)
    txtinp61.insert(0,inpa6)
    txtinp61.insert(0,inp6)

    first_line = text.split()[131]
    inp7 = [int(first_line[0:3])]
    second_line = text.split()[132]
    inpa7 = [int(second_line[0:3])]
    third_line = text.split()[133]
    inpb7 = [int(third_line[0:3])]
    txtinp71.grid(row=19, column=1)
    txtinp71.insert(0,inpb7)
    txtinp71.insert(0,inpa7)
    txtinp71.insert(0,inp7)

    first_line = text.split()[134]
    inp8 = [int(first_line[0:3])]
    second_line = text.split()[135]
    inpa8 = [int(second_line[0:3])]
    third_line = text.split()[136]
    inpb8 = [int(third_line[0:3])]
    txtinp81.grid(row=19, column=2)
    txtinp81.insert(0,inpb8)
    txtinp81.insert(0,inpa8)
    txtinp81.insert(0,inp8)

    first_line = text.split()[137]
    inp9 = [int(first_line[0:3])]
    second_line = text.split()[138]
    inpa9 = [int(second_line[0:3])]
    third_line = text.split()[139]
    inpb9 = [int(third_line[0:3])]
    txtinp91.grid(row=19, column=3)
    txtinp91.insert(0,inpb9)
    txtinp91.insert(0,inpa9)
    txtinp91.insert(0,inp9)

    first_line = text.split()[140]
    inp10 = [int(first_line[0:3])]
    second_line = text.split()[141]
    inpa10 = [int(second_line[0:3])]
    third_line = text.split()[142]
    inpb10 = [int(third_line[0:3])]
    txtinp101.grid(row=19, column=4)
    txtinp101.insert(0,inpb10)
    txtinp101.insert(0,inpa10)
    txtinp101.insert(0,inp10)

    first_line = text.split()[143]
    inp11 = [int(first_line[0:3])]
    second_line = text.split()[144]
    inpa11 = [int(second_line[0:3])]
    third_line = text.split()[145]
    inpb11 = [int(third_line[0:3])]
    txtinp111.grid(row=19, column=5)
    txtinp111.insert(0,inpb11)
    txtinp111.insert(0,inpa11)
    txtinp111.insert(0,inp11)

    first_line = text.split()[146]
    inp12 = [int(first_line[0:3])]
    second_line = text.split()[147]
    inpa12 = [int(second_line[0:3])]
    third_line = text.split()[148]
    inpb12 = [int(third_line[0:3])]
    txtinp121.grid(row=19, column=6)
    txtinp121.insert(0,inpb12)
    txtinp121.insert(0,inpa12)
    txtinp121.insert(0,inp12)

    first_line = text.split()[149]
    inp13 = [int(first_line[0:3])]
    second_line = text.split()[150]
    inpa13 = [int(second_line[0:3])]
    third_line = text.split()[151]
    inpb13 = [int(third_line[0:3])]
    txtinp131.grid(row=19, column=7)
    txtinp131.insert(0,inpb13)
    txtinp131.insert(0,inpa13)
    txtinp131.insert(0,inp13)

#############################Specify UNIT and DATE######################
unit = int()
#unit = dict(['unit'])
#date = (a(['date']))
date = StringVar()

lblpow = Label(f1, padx=16, bd=4, fg='black', font=('Verdana',12), text='DATE', bg='red', anchor='w')
lblpow.grid(row=0, column=0)
txtpow1 = Entry(f1, font=('Verdana',9), textvariable=unit, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtpow1.grid(row=0, column=1)
#txtpow.insert(0,dict['unit'])

lblpow = Label(f1, padx=16, bd=4, fg='black', font=('Verdana',12), text='UNIT', bg='red', anchor='w')
lblpow.grid(row=0, column=2)
txtpow = Entry(f1, font=('Verdana',9), textvariable=date, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtpow.grid(row=0, column=3)
#txtpow.insert(1,[a])
##################################################
ar1 = StringVar()
ar2 = StringVar()
ar3 = StringVar()
ar4 = StringVar()
ar5 = StringVar()
ar6 = StringVar()
ar7 = StringVar()
ar8 = StringVar()
ar9 = StringVar()
ar10 = StringVar()
ar11 = StringVar()
ar12 = StringVar()
ar13 = StringVar()
ar14 = StringVar()
ar15 = StringVar()
ar16 = StringVar()
ar17 = StringVar()
################## AR INPUT #############
lblar1 = Label(f1, font=('Verdana',9), text='AR-1(BK#4)', bd=4, anchor='w')
lblar1.grid(row=1, column=0)
txtar1 = Entry(f1, font=('Verdana',9), textvariable=ar1, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar01 = Entry(f1, font=('Verdana',9), textvariable=ar1, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar1.grid(row=2, column=0)

lblar2 = Label(f1, font=('Verdana',9), text='AR-2(BK#7)', bd=4, anchor='w')
lblar2.grid(row=1, column=1)
txtar2 = Entry(f1, font=('Verdana',9), textvariable=ar2, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar21 = Entry(f1, font=('Verdana',9), textvariable=ar2, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar2.grid(row=2, column=1)

lblar3 = Label(f1, font=('Verdana',9), text='AR-3(BK#5)', bd=4, anchor='w')
lblar3.grid(row=1, column=2)
txtar3 = Entry(f1, font=('Verdana',9), textvariable=ar3, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar31 = Entry(f1, font=('Verdana',9), textvariable=ar3, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar3.grid(row=2, column=2)

lblar4 = Label(f1, font=('Verdana',9), text='AR-4(BK#8)', bd=4, anchor='w')
lblar4.grid(row=1, column=3)
txtar4 = Entry(f1, font=('Verdana',9), textvariable=ar4, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar41 = Entry(f1, font=('Verdana',9), textvariable=ar4, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar4.grid(row=2, column=3)

lblar5 = Label(f1, font=('Verdana',9), text='AR-5(BK#4)', bd=4, anchor='w')
lblar5.grid(row=1, column=4)
txtar5 = Entry(f1, font=('Verdana',9), textvariable=ar5, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar51 = Entry(f1, font=('Verdana',9), textvariable=ar5, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar5.grid(row=2, column=4)

lblar6 = Label(f1, font=('Verdana',9), text='AR-6(BK#2)', bd=4, anchor='w')
lblar6.grid(row=1, column=5)
txtar6 = Entry(f1, font=('Verdana',9), textvariable=ar6, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar61 = Entry(f1, font=('Verdana',9), textvariable=ar6, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar6.grid(row=2, column=5)

lblar7 = Label(f1, font=('Verdana',9), text='AR-7(BK#6)', bd=4, anchor='w')
lblar7.grid(row=1, column=6)
txtar7 = Entry(f1, font=('Verdana',9), textvariable=ar7, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar71 = Entry(f1, font=('Verdana',9), textvariable=ar7, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar7.grid(row=2, column=6)

lblar8 = Label(f1, font=('Verdana',9), text='AR-8(BK#3)', bd=4, anchor='w')
lblar8.grid(row=1, column=7)
txtar8 = Entry(f1, font=('Verdana',9), textvariable=ar8, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar81 = Entry(f1, font=('Verdana',9), textvariable=ar8, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar8.grid(row=2, column=7)

lblar9 = Label(f1, font=('Verdana',9), text='AR-9(BK#1)', bd=4, anchor='w')
lblar9.grid(row=1, column=8)
txtar9 = Entry(f1, font=('Verdana',9), textvariable=ar9, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar91 = Entry(f1, font=('Verdana',9), textvariable=ar9, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtar9.grid(row=2, column=8)

lblar10 = Label(f1, font=('Verdana',9), text='AR-10(BK#3)', bd=4, anchor='w')
lblar10.grid(row=1, column=9)
txtar10 = Entry(f1, font=('Verdana',9), textvariable=ar10, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar101 = Entry(f1, font=('Verdana',9), textvariable=ar10, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar10.grid(row=2, column=9)

lblar11 = Label(f1, font=('Verdana',9), text='AR-11(BK#6)', bd=4, anchor='w')
lblar11.grid(row=3, column=0)
txtar11 = Entry(f1, font=('Verdana',9), textvariable=ar11, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar111 = Entry(f1, font=('Verdana',9), textvariable=ar11, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar11.grid(row=4, column=0)

lblar12 = Label(f1, font=('Verdana',9), text='AR-12(BK#2)', bd=4, anchor='w')
lblar12.grid(row=3, column=1)
txtar12 = Entry(f1, font=('Verdana',9), textvariable=ar12, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar121 = Entry(f1, font=('Verdana',9), textvariable=ar12, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar12.grid(row=4, column=1)

lblar13 = Label(f1, font=('Verdana',9), text='AR-13(BK#4)', bd=4, anchor='w')
lblar13.grid(row=3, column=2)
txtar13 = Entry(f1, font=('Verdana',9), textvariable=ar13, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar131 = Entry(f1, font=('Verdana',9), textvariable=ar13, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar13.grid(row=4, column=2)

lblar14 = Label(f1, font=('Verdana',9), text='AR-14(BK#8)', bd=4, anchor='w')
lblar14.grid(row=3, column=3)
txtar14 = Entry(f1, font=('Verdana',9), textvariable=ar14, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar141 = Entry(f1, font=('Verdana',9), textvariable=ar14, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar14.grid(row=4, column=3)

lblar15 = Label(f1, font=('Verdana',9), text='AR-15(BK#5)', bd=4, anchor='w')
lblar15.grid(row=3, column=4)
txtar15 = Entry(f1, font=('Verdana',9), textvariable=ar15, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar151 = Entry(f1, font=('Verdana',9), textvariable=ar15, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar15.grid(row=4, column=4)

lblar16 = Label(f1, font=('Verdana',9), text='AR-16(BK#7)', bd=4, anchor='w')
lblar16.grid(row=3, column=5)
txtar16 = Entry(f1, font=('Verdana',9), textvariable=ar16, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar161 = Entry(f1, font=('Verdana',9), textvariable=ar16, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar16.grid(row=4, column=5)

lblar17 = Label(f1, font=('Verdana',9), text='AR-17(BK#4)', bd=4, anchor='w')
lblar17.grid(row=3, column=6)
txtar17 = Entry(f1, font=('Verdana',9), textvariable=ar17, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar171 = Entry(f1, font=('Verdana',9), textvariable=ar17, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtar17.grid(row=4, column=6)

################ CR INPUT###################
cr1 = StringVar()
cr2 = StringVar()
cr3 = StringVar()
cr4 = StringVar()

lblcr1 = Label(f1, fg = 'blue', font=('Verdana',9), text='CR-1', bd=4, anchor='w')
lblcr1.grid(row=5, column=0)
txtcr1 = Entry(f1, font=('Verdana',9), textvariable=cr1, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtcr11 = Entry(f1, font=('Verdana',9), textvariable=cr1, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtcr1.grid(row=6, column=0)

lblcr2 = Label(f1, fg = 'blue', font=('Verdana',9), text='CR-2', bd=4, anchor='w')
lblcr2.grid(row=5, column=1)
txtcr2 = Entry(f1, font=('Verdana',9), textvariable=cr2, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtcr21 = Entry(f1, font=('Verdana',9), textvariable=cr2, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtcr2.grid(row=6, column=1)

lblcr3 = Label(f1, fg = 'blue', font=('Verdana',9), text='CR-3', bd=4, anchor='w')
lblcr3.grid(row=5, column=2)
txtcr3 = Entry(f1, font=('Verdana',9), textvariable=cr3, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtcr31 = Entry(f1, font=('Verdana',9), textvariable=cr3, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtcr3.grid(row=6, column=2)

lblcr4 = Label(f1, fg = 'blue', font=('Verdana',9), text='CR-4', bd=4, anchor='w')
lblcr4.grid(row=5, column=3)
txtcr4 = Entry(f1, font=('Verdana',9), textvariable=cr4, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtcr41 = Entry(f1, font=('Verdana',9), textvariable=cr4, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtcr4.grid(row=6, column=3)

###################### SR INPUT #################
sr1 = StringVar()
sr2 = StringVar()

lblsr1 = Label(f1, fg='red',font=('Verdana',9), text='SR-BK-1', bd=4, anchor='w')
lblsr1.grid(row=5, column=4)
txtsr1 = Entry(f1, font=('Verdana',9), textvariable=sr1, bd=4, insertwidth=20,
               bg='powder blue', justify='right')
txtsr11 = Entry(f1, font=('Verdana',9), textvariable=sr1, bd=4, insertwidth=20,
               bg='powder blue', justify='right')
txtsr1.grid(row=6, column=4)

lblsr2 = Label(f1, fg='red',font=('Verdana',9), text='SR-BK-2', bd=4, anchor='w')
lblsr2.grid(row=5, column=5)
txtsr2 = Entry(f1, font=('Verdana',9), textvariable=sr2, bd=4, insertwidth=20,
               bg='powder blue', justify='right')
txtsr21 = Entry(f1, font=('Verdana',9), textvariable=sr2, bd=4, insertwidth=20,
               bg='powder blue', justify='right')
txtsr2.grid(row=6, column=5)

#################### ICASE ISNAP NDIR NOFTYP PowerCoef Xenon Rhodium INPUT #######################
icase = StringVar()
isnap = StringVar()
ndir = StringVar()
noftyp = StringVar()
powercoeff = StringVar()
xenon = StringVar()
rhodium = StringVar()

lblicase = Label(f1, font=('Verdana',9), text='ICASE', bd=4, anchor='w')
lblicase.grid(row=7, column=0)
txticase = Entry(f1, font=('Verdana',9), textvariable= icase, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txticase1 = Entry(f1, font=('Verdana',9), textvariable= icase, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txticase.grid(row=8, column=0)

lblisnap = Label(f1, font=('Verdana',9), text='ISNAP', bd=4, anchor='w')
lblisnap.grid(row=7, column=1)
txtisnap = Entry(f1, font=('Verdana',9), textvariable=isnap, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtisnap1 = Entry(f1, font=('Verdana',9), textvariable=isnap, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtisnap.grid(row=8, column=1)

lblndir = Label(f1,font=('Verdana',9),text='NDIR',bd=4,anchor='w')
lblndir.grid(row=7,column=2)
txtndir =Entry(f1,font=('Verdana',9),textvariable=ndir,bd=4,insertwidth=2,
                bg='powder blue',justify='right')
txtndir1 =Entry(f1,font=('Verdana',9),textvariable=ndir,bd=4,insertwidth=2,
                bg='powder blue',justify='right')
txtndir.grid(row=8,column=2)

lblnoftyp = Label(f1,font=('Verdana',9),text='NOFTYP',bd=4,anchor='w')
lblnoftyp.grid(row=7,column=3)
txtnoftyp =Entry(f1,font=('Verdana',9),textvariable=noftyp,bd=4,insertwidth=2,
                bg='powder blue',justify='right')
txtnoftyp1 =Entry(f1,font=('Verdana',9),textvariable=noftyp,bd=4,insertwidth=2,
                bg='powder blue',justify='right')
txtnoftyp.grid(row=8,column=3)

lblpowercoeff = Label(f1, font=('Verdana',9), text='POWER COEFFICIENT', bd=4, anchor='w')
lblpowercoeff.grid(row=7, column=4)
txtpowercoeff = Entry(f1, font=('Verdana',9), textvariable=powercoeff, bd=4, insertwidth=2,
                      bg='powder blue', justify='right')
txtpowercoeff1 = Entry(f1, font=('Verdana',9), textvariable=powercoeff, bd=4, insertwidth=2,
                      bg='powder blue', justify='right')
txtpowercoeff.grid(row=8, column=4)

lblxenon = Label(f1, font=('Verdana',9), text='XENON', bd=4, anchor='w')
lblxenon.grid(row=7, column=5)
txtxenon = Entry(f1, font=('Verdana',9), textvariable=xenon, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtxenon1 = Entry(f1, font=('Verdana',9), textvariable=xenon, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtxenon.grid(row=8, column=5)

lblrhodium = Label(f1, font=('Verdana',9), text='RHODIUM', bd=4, anchor='w')
lblrhodium.grid(row=7, column=6)
txtrhodium = Entry(f1, font=('Verdana',9), textvariable=rhodium, bd=4, insertwidth=2,
                   bg='powder blue', justify='right')
txtrhodium1 = Entry(f1, font=('Verdana',9), textvariable=rhodium, bd=4, insertwidth=2,
                   bg='powder blue', justify='right')
txtrhodium.grid(row=8, column=6)

##################### ModH %FP guesstf Boron xmu ################
modh = StringVar()
pfp = StringVar()
guesstf = StringVar()
boron = StringVar()
xmu = StringVar()
fpd = StringVar()

lblmodh = Label(f1, font=('Verdana',9), text='MODH', bd=4, anchor='w')
lblmodh.grid(row=7, column=7)
txtmodh = Entry(f1, font=('Verdana',9), textvariable=modh, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtmodh1 = Entry(f1, font=('Verdana',9), textvariable=modh, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtmodh.grid(row=8, column=7)

lblpfp = Label(f1, font=('Verdana',9), text='% FP', bd=4, anchor='w')
lblpfp.grid(row=7, column=8)
txtpfp = Entry(f1, font=('Verdana',9), textvariable=pfp, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtpfp1 = Entry(f1, font=('Verdana',9), textvariable=pfp, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtpfp.grid(row=8, column=8)

lblguesstf = Label(f1, font=('Verdana',9), text='GuessTf', bd=4, anchor='w')
lblguesstf.grid(row=5, column=6)
txtguesstf = Entry(f1, font=('Verdana',9), textvariable=guesstf, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtguesstf1 = Entry(f1, font=('Verdana',9), textvariable=guesstf, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtguesstf.grid(row=6, column=6)

lblboron = Label(f1, font=('Verdana',9), text='BORON', bd=4, anchor='w')
lblboron.grid(row=7, column=9)
txtboron = Entry(f1, font=('Verdana',9), textvariable=boron, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtboron1 = Entry(f1, font=('Verdana',9), textvariable=boron, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtboron.grid(row=8, column=9)

lblxmu = Label(f1, font=('Verdana',9), text='XMU', bd=4, anchor='w')
lblxmu.grid(row=5, column=7)
txtxmu = Entry(f1, font=('Verdana',9), textvariable=xmu, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtxmu1 = Entry(f1, font=('Verdana',9), textvariable=xmu, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtxmu.grid(row=6, column=7)

lblfpd = Label(f1, font=('Verdana',9), text='FPD', bd=4, anchor='w')
lblfpd.grid(row=5, column=8)
txtfpd = Entry(f1, font=('Verdana',9), textvariable=fpd, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtfpd1 = Entry(f1, font=('Verdana',9), textvariable=fpd, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtfpd.grid(row=6, column=8)

##################### ZCC INPUT #######################
zcc1 = StringVar()
zcc2 = StringVar()
zcc3 = StringVar()
zcc4 = StringVar()
zcc5 = StringVar()
zcc6 = StringVar()
zcc7 = StringVar()
zcc8 = StringVar()
zcc9 = StringVar()
zcc10 = StringVar()
zcc11 = StringVar()
zcc12 = StringVar()
zcc13 = StringVar()
zcc14 = StringVar()

lblzcc1 = Label(f1, font=('Verdana',9), text='ZCC - 1', bd=4, anchor='w')
lblzcc1.grid(row=9, column=0)
txtzcc1 = Entry(f1, font=('Verdana',9), textvariable=zcc1, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc01 = Entry(f1, font=('Verdana',9), textvariable=zcc1, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc1.grid(row=10, column=0)

lblzcc2 = Label(f1, font=('Verdana',9), text='ZCC - 2', bd=4, anchor='w')
lblzcc2.grid(row=9, column=1)
txtzcc2 = Entry(f1, font=('Verdana',9), textvariable=zcc2, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc21 = Entry(f1, font=('Verdana',9), textvariable=zcc2, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc2.grid(row=10, column=1)

lblzcc3 = Label(f1, font=('Verdana',9), text='ZCC - 3', bd=4, anchor='w')
lblzcc3.grid(row=9, column=2)
txtzcc3 = Entry(f1, font=('Verdana',9), textvariable=zcc3, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc31 = Entry(f1, font=('Verdana',9), textvariable=zcc3, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc3.grid(row=10, column=2)

lblzcc4 = Label(f1, font=('Verdana',9), text='ZCC - 4', bd=4, anchor='w')
lblzcc4.grid(row=9, column=3)
txtzcc4 = Entry(f1, font=('Verdana',9), textvariable=zcc4, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc41 = Entry(f1, font=('Verdana',9), textvariable=zcc4, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc4.grid(row=10, column=3)

lblzcc5 = Label(f1, font=('Verdana',9), text='ZCC - 5', bd=4, anchor='w')
lblzcc5.grid(row=9, column=4)
txtzcc5 = Entry(f1, font=('Verdana',9), textvariable=zcc5, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc51 = Entry(f1, font=('Verdana',9), textvariable=zcc5, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc5.grid(row=10, column=4)

lblzcc6 = Label(f1, font=('Verdana',9), text='ZCC - 6', bd=4, anchor='w')
lblzcc6.grid(row=9, column=5)
txtzcc6 = Entry(f1, font=('Verdana',9), textvariable=zcc6, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc61 = Entry(f1, font=('Verdana',9), textvariable=zcc6, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc6.grid(row=10, column=5)

lblzcc7 = Label(f1, font=('Verdana',9), text='ZCC - 7', bd=4, anchor='w')
lblzcc7.grid(row=9, column=6)
txtzcc7 = Entry(f1, font=('Verdana',9), textvariable=zcc7, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc71 = Entry(f1, font=('Verdana',9), textvariable=zcc7, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc7.grid(row=10, column=6)

lblzcc8 = Label(f1, font=('Verdana',9), text='ZCC - 8', bd=4, anchor='w')
lblzcc8.grid(row=9, column=7)
txtzcc8 = Entry(f1, font=('Verdana',9), textvariable=zcc8, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc81 = Entry(f1, font=('Verdana',9), textvariable=zcc8, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc8.grid(row=10, column=7)

lblzcc9 = Label(f1, font=('Verdana',9), text='ZCC - 9', bd=4, anchor='w')
lblzcc9.grid(row=9, column=8)
txtzcc9 = Entry(f1, font=('Verdana',9), textvariable=zcc9, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc91 = Entry(f1, font=('Verdana',9), textvariable=zcc9, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtzcc9.grid(row=10, column=8)

lblzcc10 = Label(f1, font=('Verdana',9), text='ZCC - 10', bd=4, anchor='w')
lblzcc10.grid(row=9, column=9)
txtzcc10 = Entry(f1, font=('Verdana',9), textvariable=zcc10, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtzcc101 = Entry(f1, font=('Verdana',9), textvariable=zcc10, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtzcc10.grid(row=10, column=9)

lblzcc11 = Label(f1, font=('Verdana',9), text='ZCC - 11', bd=4, anchor='w')
lblzcc11.grid(row=11, column=0)
txtzcc11 = Entry(f1, font=('Verdana',9), textvariable=zcc11, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtzcc111 = Entry(f1, font=('Verdana',9), textvariable=zcc11, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtzcc11.grid(row=12, column=0)

lblzcc12 = Label(f1, font=('Verdana',9), text='ZCC - 12', bd=4, anchor='w')
lblzcc12.grid(row=11, column=1)
txtzcc12 = Entry(f1, font=('Verdana',9), textvariable=zcc12, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtzcc121 = Entry(f1, font=('Verdana',9), textvariable=zcc12, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtzcc12.grid(row=12, column=1)

lblzcc13 = Label(f1, font=('Verdana',9), text='ZCC - 13', bd=4, anchor='w')
lblzcc13.grid(row=11, column=2)
txtzcc13 = Entry(f1, font=('Verdana',9), textvariable=zcc13, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtzcc131 = Entry(f1, font=('Verdana',9), textvariable=zcc13, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtzcc13.grid(row=12, column=2)

lblzcc14 = Label(f1, font=('Verdana',9), text='ZCC - 14', bd=4, anchor='w')
lblzcc14.grid(row=11, column=3)
txtzcc14 = Entry(f1, font=('Verdana',9), textvariable=zcc14, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtzcc141 = Entry(f1, font=('Verdana',9), textvariable=zcc14, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtzcc14.grid(row=12, column=3)

############### REFUELLING CHANNEL DETAIL INPUT ##############################
ref = StringVar()
refid = StringVar()
bss = StringVar()
inp1 = StringVar()
inp2 = StringVar()
inp3 = StringVar()
inp4 = StringVar()
inp5 = StringVar()
inp6 = StringVar()
inp7 = StringVar()
inp8 = StringVar()
inp9 = StringVar()
inp10 = StringVar()
inp11 = StringVar()
inp12 = StringVar()
inp13 = StringVar()

lblref = Label(f1, font=('Verdana',9), text='CH NAME', bd=4, anchor='w')
lblref.grid(row=14, column=0)
txtref = Entry(f1, font=('Verdana',9), textvariable=ref, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtref1 = Entry(f1, font=('Verdana',9), textvariable=ref, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtref.grid(row=15, column=0)

lblrefid = Label(f1, font=('Verdana',9), text='CH NUMBER', bd=4, anchor='w')
lblrefid.grid(row=14, column=1)
txtrefid = Entry(f1, font=('Verdana',9), textvariable=refid, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtrefid1 = Entry(f1, font=('Verdana',9), textvariable=refid, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtrefid.grid(row=15, column=1)

lblbss = Label(f1, font=('Verdana',9), text='BSS', bd=4, anchor='w')
lblbss.grid(row=14, column=2)
txtbss = Entry(f1, font=('Verdana',9), textvariable=bss, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtbss1 = Entry(f1, font=('Verdana',9), textvariable=bss, bd=4, insertwidth=2,
               bg='powder blue', justify='right')
txtbss.grid(row=15, column=2)

lblinp1 = Label(f1, font=('Verdana',9), text='STRING POSITION - 1', bd=4, anchor='w')
lblinp1.grid(row=16, column=0)
lblinp1.columnconfigure(6,weight=1)
txtinp1 = Entry(f1, font=('Verdana',9), textvariable=inp1, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp01 = Entry(f1, font=('Verdana',9), textvariable=inp1, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp1.grid(row=17, column=0)

lblinp2 = Label(f1, font=('Verdana',9), text='STRING POSITION - 2', bd=4, anchor='w')
lblinp2.grid(row=16, column=1)
txtinp2 = Entry(f1, font=('Verdana',9), textvariable=inp2, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp21 = Entry(f1, font=('Verdana',9), textvariable=inp2, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp2.grid(row=17, column=1)

lblinp3 = Label(f1, font=('Verdana',9), text='STRING POSITION - 3', bd=4, anchor='w')
lblinp3.grid(row=16, column=2)
txtinp3 = Entry(f1, font=('Verdana',9), textvariable=inp3, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp31 = Entry(f1, font=('Verdana',9), textvariable=inp3, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp3.grid(row=17, column=2)

lblinp4 = Label(f1, font=('Verdana',9), text='STRING POSITION - 4', bd=4, anchor='w')
lblinp4.grid(row=16, column=3)
txtinp4 = Entry(f1, font=('Verdana',9), textvariable=inp4, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp41 = Entry(f1, font=('Verdana',9), textvariable=inp4, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp4.grid(row=17, column=3)

lblinp5 = Label(f1, font=('Verdana',9), text='STRING POSITION - 5', bd=4, anchor='w')
lblinp5.grid(row=16, column=4)
txtinp5 = Entry(f1, font=('Verdana',9), textvariable=inp5, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp51 = Entry(f1, font=('Verdana',9), textvariable=inp5, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp5.grid(row=17, column=4)

lblinp6 = Label(f1, font=('Verdana',9), text='STRING POSITION - 6', bd=4, anchor='w')
lblinp6.grid(row=18, column=0)
txtinp6 = Entry(f1, font=('Verdana',9), textvariable=inp6, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp61 = Entry(f1, font=('Verdana',9), textvariable=inp6, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp6.grid(row=19, column=0)

lblinp7 = Label(f1, font=('Verdana',9), text='STRING POSITION - 7', bd=4, anchor='w')
lblinp7.grid(row=18, column=1)
txtinp7 = Entry(f1, font=('Verdana',9), textvariable=inp7, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp71 = Entry(f1, font=('Verdana',9), textvariable=inp7, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp7.grid(row=19, column=1)

lblinp8 = Label(f1, font=('Verdana',9), text='STRING POSITION - 8', bd=4, anchor='w')
lblinp8.grid(row=18, column=2)
txtinp8 = Entry(f1, font=('Verdana',9), textvariable=inp8, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp81 = Entry(f1, font=('Verdana',9), textvariable=inp8, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp8.grid(row=19, column=2)

lblinp9 = Label(f1, font=('Verdana',9), text='STRING POSITION - 9', bd=4, anchor='w')
lblinp9.grid(row=18, column=3)
txtinp9 = Entry(f1, font=('Verdana',9), textvariable=inp9, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp91 = Entry(f1, font=('Verdana',9), textvariable=inp9, bd=4, insertwidth=2,
                bg='powder blue', justify='right')
txtinp9.grid(row=19, column=3)

lblinp10 = Label(f1, font=('Verdana',9), text='STRING POSITION - 10', bd=4, anchor='w')
lblinp10.grid(row=18, column=4)
txtinp10 = Entry(f1, font=('Verdana',9), textvariable=inp10, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtinp101 = Entry(f1, font=('Verdana',9), textvariable=inp10, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtinp10.grid(row=19, column=4)

lblinp11 = Label(f1, font=('Verdana',9), text='STRING POSITION - 11', bd=4, anchor='w')
lblinp11.grid(row=18, column=5)
txtinp11 = Entry(f1, font=('Verdana',9), textvariable=inp11, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtinp111 = Entry(f1, font=('Verdana',9), textvariable=inp11, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtinp11.grid(row=19, column=5)

lblinp12 = Label(f1, font=('Verdana',9), text='STRING POSITION - 12', bd=4, anchor='w')
lblinp12.grid(row=18, column=6)
txtinp12 = Entry(f1, font=('Verdana',9), textvariable=inp12, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtinp121 = Entry(f1, font=('Verdana',9), textvariable=inp12, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtinp12.grid(row=19, column=6)

lblinp13 = Label(f1, font=('Verdana',9), text='STRING POSITION - 13', bd=4, anchor='w')
lblinp13.grid(row=18, column=7)
txtinp13 = Entry(f1, font=('Verdana',9), textvariable=inp13, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtinp131 = Entry(f1, font=('Verdana',9), textvariable=inp13, bd=4, insertwidth=2,
                 bg='powder blue', justify='right')
txtinp13.grid(row=19, column=7)

##################### buttons ########################
def seetape5():
    with open('tape5','r') as f:
        text = f.read()
        popup = Tk()
        popup.wm_title('TAPE-5')
        label = Label(popup,text = text, bg= 'white',fg='black',justify='left',font =('arial',15))
        label.grid()
        B1 = Button(popup,text='OK',font=('Verdana',12),bg='red',command=popup.destroy)
        B1.grid()
        popup.mainloop()

#def savetape5():
    #with open('tape5','w') as f:
        #f.seek(0)
        #f.write(f)

def runtape5():
    subprocess.call(['/home/user01/cfwaro_T3/./cfwaro_t3'])
    #subprocess.call(['D:\sm-follow\cfwaro.exe'])

btntape5 = Button(f1, padx=16, bd=4, fg='black', font=('Verdana',9), text="SEE TAPE-5",
                  bg="DarkOliveGreen", command=seetape5).grid(row=15, column=9)
btnadd = Button(f1, padx=16, bd=4, fg='black', font=('Verdana',9), text="ADD CHANNEL",
                  bg='green', command=btnadd).grid(row=14, column=6)
btntape5 = Button(f1, padx=16, bd=4, fg='black', font=('Verdana',9), text="OPEN TAPE5",
                  bg="Olive", command=opentape5).grid(row=14, column=9)
btntape5 = Button(f1, padx=16, bd=4, fg='black', font=('Verdana',9), text="SAVE TAPE-5",
                  bg="Yellow", command=savetape5).grid(row=16, column=9)
btntape5 = Button(f1, padx=16, bd=4, fg='black', font=('Verdana',9), text="RUN-CFWARO",
                  bg="OrangeRed", command=runtape5).grid(row=17, column=9)
btnok = Button(f1,text='OK',font=('Verdana',12),bg='white',command=root.destroy).grid(row=19, column=9)

root.mainloop()