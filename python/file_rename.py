import os
import string
import itertools

os.chdir('/media/user01/1386EB730F43FD42/MIT_6.046J/')

for f in os.listdir():
    #print(f)
    #a = f.strip()
    #print(a)
    fname,fext = os.path.splitext(f)
    #a1,a2,a3,a4,a5,a6,a7,a8,a9 = fname.split('.')
    a1 =  fname.split('-')
    #print(a1)
    a2 = a1[0:2]
    #print(a2)
    a3 = ''.join(a2)
    #print(a3)
    #print(fext)
    #b = str(fname).ljust(70,'-')
    #print(b)
    #c = b.strip('-')
    #print(c)
    #d = c[0:52]
    #print('{} {} {} {} {} {} {}.{}'.format(a2.zfill(2),a1,a6,a7,a8,a9,fext))
    #print('{}{}'.format(a3,fext))
    renamed = '{}{}'.format(a3,fext)
    #renamed = '{}{}'.format(c,fext)
    #print(renamed)
    os.rename(f,renamed)

