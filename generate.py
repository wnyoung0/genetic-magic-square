import magicArray as ma
import random
from copy import deepcopy
import json
import matplotlib.pyplot as plt
ma.config('data/star.json')
mm=ma.ArrayManager()

dataF=open('data/data.json','r')
data=json.load(dataF)
 


def logg(i):
    global mm
    print(f"{mm.getArray(i).getScore()}\n{mm.getArray(i).getArray()}")
def print_33(i):
    global mm
    print(f"{mm.getArray(i).getScore()}\n{mm.getArray(i).getArray()[0:3]}\n{mm.getArray(i).getArray()[3:6]}\n{mm.getArray(i).getArray()[6:9]}\n\n")
def print_star6(i):
    global mm
    plt.figure(figsize=(4, 4))
    plt.plot(data["star6"]["x"],data["star6"]["y"],'ro')
    for _ in range(12):
        plt.text(data["star6"]["x"][_],data["star6"]["y"][_]+0.1,'%d'%(mm.getArray(i).getArray()[_]),ha='center',va='bottom',size=10)
    plt.show()



def f():
    mm.sortList()
    for i in range(0,100):
        print(i+1,end=' ')
        print(mm.getArray(i).getScore(),mm.getArray(i).getArray(),sep='   ')
        print("="*20)
    for i in range(10,50):
        ind=random.randint(0,9)
        mm.getArray(i).setArray(ma.mutate(deepcopy(mm.getArray(ind).getArray())))
    for i in range(50,100):
        mm.getArray(i).setArray(ma.mutate(ma.mutate(deepcopy(mm.getArray(ind).getArray()))))
       
for i in range(0,100):
    mm.addArray(ma.MagicArray())
    mm.getArray(i).setArray(ma.genArray())
for i in range(0,140):
    if mm.getArray(0).getScore()<=0.0:
        print("||"*10+'\n',sep='')
        print_star6(0)
        break
    print(i+1)
    print()
    f()
