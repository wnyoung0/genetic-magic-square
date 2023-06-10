import random
from numpy import *
from copy import deepcopy
import json
size=0
sums=[]
defaultArray=[]
def isMagic(array,ort):
    L=0
    S=0
    R=0
    lLll=[]
    
    if ort:
        for i in range(len(array)):
            if (array[i],ort[i]) in lLll:
                print("L")
                return False
            else:
                lLll.append((array[i],ort[i]))
        sS=set(lLll)
        if len(sS)!=len(array):
            print(len(sS))
            return False
        print(len(sS))
        
    for _ in sums:
        for i in _:
            S+=array[i]
        #print(S)
        if L!=0:
            if S==R:
                L=1
            else:
                return False
        else:
            L=1
        R=S
        S=0

    return True

def config(file):
    cF=open(file,'r')
    cfs=json.load(cF)
    global size
    size=cfs['size']
    global defaultArray
    defaultArray=cfs['default']
    global sums
    sums=cfs['sums']
def score(array,orthogonal):
    d=[]
    S=0
    for i in sums:
        for j in i:
            S+=array[j]
        d.append(S)
        S=0
    S=0
    
    if orthogonal:
        lLll=[]
        for i in range(len(array)):
            if (array[i],orthogonal[i]) in lLll:
                S+=1
            else:
                lLll.append((array[i],orthogonal[i]))
        S=S/10
        return var(d)+S
    

    return var(d)

def genArray():
    global size
    L=[i for i in range(1,size+1)]
    random.shuffle(L)
    return L

def permitate(array,n):#this is for latin square
    lLl=deepcopy(array)
    a_f_gm = random.randint(1,n+1)
    b_f_gm = random.randint(1,n+1)
    while(a_f_gm==b_f_gm):
        b_f_gm = random.randint(1,n+1)
    for i in range(len(lLl)):
        if lLl[i]==a_f_gm:
            lLl[i]='a'
        elif lLl[i]==b_f_gm:
            lLl[i]='b'
    for i in range(len(lLl)):
        if lLl[i]=='a':
            lLl[i]=a_f_gm
        elif lLl[i]=='b':
            lLl[i]=b_f_gm
    return deepcopy(lLl)

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
        self.orth=[]

    def getArray(self):
        return deepcopy(self.array)
    def setArray(self,array):
        self.array=deepcopy(array)
    def setOrth(self,array):
        self.orth=deepcopy(array)
    def getScore(self):
     
        return score(self.array,self.orth)
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

