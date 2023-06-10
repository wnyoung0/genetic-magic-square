import magicArray as ma
import random
from copy import deepcopy
import json
import matplotlib.pyplot as plt
ma.config('data/lat2in5.json')
mm=ma.ArrayManager()

dataF=open('data/data.json','r')
data=json.load(dataF)
 
ort=[5, 2, 2, 5, 1, 3, 3, 4, 1, 4, 1, 4, 2, 3, 5, 5, 3, 2, 4, 1, 1, 3, 5, 2, 4]

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
    for i in range(0,10):
        print(i+1,end=' ')
        print(mm.getArray(i).getScore(),mm.getArray(i).getArray(),sep='   ')
        print("="*20)
    for i in range(40,70):
        ind=random.randint(0,10)
        mm.getArray(i).setArray(ma.mutate(ma.mutate(deepcopy(mm.getArray(ind).getArray()))))
    for i in range(70,90):
        ind=random.randint(0,40)
        mm.getArray(i).setArray(ma.mutate(ma.mutate(ma.mutate(deepcopy(mm.getArray(ind).getArray())))))
    for i in range(90,130):
        ind=random.randint(0,40)
        lLLlL=ma.mutate(ma.mutate(deepcopy(mm.getArray(ind).getArray())))
        for i in range(20):
            lLLlL=ma.mutate(lLLlL)
        mm.getArray(i).setArray(lLLlL)
    for i in range(130,180):
        ind=random.randint(0,30)
        mm.getArray(i).setArray(ma.permitate(mm.getArray(ind).getArray(),5))
    for i in range(180,300):
        ind=random.randint(0,5)
        mm.getArray(i).setArray(ma.mutate(ma.mutate(ma.mutate(ma.mutate(ma.mutate(deepcopy(mm.getArray(ind).getArray())))))))
    for i in range(300,390):
        ind=random.randint(0,5)
        mm.getArray(i).setArray(ma.mutate(ma.mutate(deepcopy(mm.getArray(ind).getArray()))))
    for i in range(390,500):
        mm.getArray(i).setArray(deepcopy(ma.defaultArray))
def ff(n):
    for i in range(0,n):
        print("j",end='')
        print()
        print()
        mm.getArray(i).setArray(deepcopy(ma.defaultArray))

for i in range(0,500):
    mm.addArray(ma.MagicArray())
    mm.getArray(i).setArray(deepcopy(ma.defaultArray))
    mm.getArray(i).setOrth(ort)



rec=0
ccc=0
lLlllL=[]
for i in range(0,1000):

    if mm.getArray(0).getScore()<=0.0 and ma.isMagic(mm.getArray(0).getArray(),ort):
        print("||"*10+'\n',sep='')
        print(f"\n{mm.getArray(0).getArray()[0:6]}\n{mm.getArray(0).getArray()[6:12]}\n{mm.getArray(0).getArray()[12:18]}\n{mm.getArray(0).getArray()[18:24]}\n{mm.getArray(0).getArray()[24:30]}\n{mm.getArray(0).getArray()[30:36]}")
        break
    print(f"---{ccc}")
    
    lLlllL=deepcopy(mm.getArray(0).getArray())
    if rec==mm.getArray(0).getArray():
        ccc+=1
    else:
        ccc=0
    if ccc>=100:
        ff(480)
   
    rec=deepcopy(lLlllL)
    print(i+1)
    print()
    f()
