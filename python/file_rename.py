import os
import string
import itertools

os.chdir('//media/user01/1386EB730F43FD42/Alok_Files/Programming_Books_&_Algorithm_Design')

for f in os.listdir():
    #print(f)
    a = f.strip()
    #print(a)
    fname,fext = os.path.splitext(f)
    #a = fname.split()
    #print(fname)
    b = str(fname).ljust(70,'-')
    #print(b)
    c = b.strip('-')
    #print(c)
    #d = c[0:52]
    #print('{}{}'.format(c,fext))
    renamed = '{}{}'.format(c,fext)
    #print(renamed)
    os.rename(f,renamed)

