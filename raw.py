import random
from numpy import *
from copy import deepcopy
import json

configFile = open("config.json",'r') #Human Inteligence를 이용해 config파일을 작성하면 된다.
configs=json.load(configFile)
size=configs['size']
sums=configs['sums']

def score(array):
    d=[]
    S=0
    for i in sums:
        for j in i:
            S+=array[j]
        d.append(S)
        S=0
    return var(d)
def genArray(size):
    L=[i for i in range(1,size+1)]
    random.shuffle(L)
    return L
def mutate(array,n=size):
    a_f_gm = random.randint(0,n)
    b_f_gm = random.randint(0,n)
    while(a_f_gm==b_f_gm):
        b_f_gm = random.randint(0,n)
        #print("%d %d"%(a_f_gm,c_f_gm))
    cfd0 = array[a_f_gm]
    array[a_f_gm]=array[b_f_gm]
    array[b_f_gm]=cfd0
    return array
    

class MagicArray():
    def __init__(self,size):
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

mm=ArrayManager()

for i in range(0,100):
    mm.addArray(MagicArray(size))
    mm.getArray(i).setArray(genArray(size))

def f():
    mm.sortList()
    for i in range(0,100):
        print(f"{i+1} {mm.getArray(i).getScore()}\n{mm.getArray(i).getArray()[0:3]}\n{mm.getArray(i).getArray()[3:6]}\n{mm.getArray(i).getArray()[6:9]}\n\n")
    print("="*20)
    for i in range(10,50):
        ind=random.randint(0,9)
        mm.getArray(i).setArray(mutate(deepcopy(mm.getArray(ind).getArray())))
    for i in range(50,100):
        mm.getArray(i).setArray(genArray(size))
        
for i in range(0,40):
    if mm.getArray(0).getScore()<=0.0:
        print("=="*10)
        print(f"\n{mm.getArray(0).getArray()[0:3]}\n{mm.getArray(0).getArray()[3:6]}\n{mm.getArray(0).getArray()[6:9]}\n\n")
        break
    print(i+1)
    print()
    f()

