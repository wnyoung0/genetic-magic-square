import random
from numpy import *
from copy import deepcopy
import json
size=0
sums=[]
def config(file):
    cF=open(file,'r')
    cfs=json.load(cF)
    global size
    size=cfs['size']
    global sums
    sums=cfs['sums']
def score(array):
    d=[]
    S=0
    for i in sums:
        for j in i:
            S+=array[j]
        d.append(S)
        S=0
    return var(d)
def genArray():
    global size
    L=[i for i in range(1,size+1)]
    random.shuffle(L)
    return L
def mutate(array):
    global size
    a_f_gm = random.randint(0,size)
    b_f_gm = random.randint(0,size)
    while(a_f_gm==b_f_gm):
        b_f_gm = random.randint(0,size)
        #print("%d %d"%(a_f_gm,c_f_gm))
    cfd0 = array[a_f_gm]
    array[a_f_gm]=array[b_f_gm]
    array[b_f_gm]=cfd0
    return array
class MagicArray():
    def __init__(self):
        global size
        self.array=[]
        self.size=size
    def getArray(self):
        return deepcopy(self.array)
    def setArray(self,array):
        self.array=array
    def getScore(self):
        return score(self.array)
class ArrayManager():
    ArrayList=[]
    def addArray(self,array):
        self.ArrayList.append(array)
    def getArray(self,index):
        return (self.ArrayList)[index]
    def arrayLen(self):
        return len(self.ArrayList)
    def sortList(self):
        self.ArrayList.sort(key=lambda x: x.getScore())
