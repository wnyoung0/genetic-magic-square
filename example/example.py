import magicArray as ma
import random
from copy import deepcopy
ma.config('config.json')#실제 파일 이름으로 대체해야함

mm=ma.ArrayManager()


for i in range(0,100):
    mm.addArray(ma.MagicArray())
    mm.getArray(i).setArray(ma.genArray())

def f():
    mm.sortList()
    for i in range(0,100):
        print(f"{i+1} {mm.getArray(i).getScore()}\n{mm.getArray(i).getArray()[0:3]}\n{mm.getArray(i).getArray()[3:6]}\n{mm.getArray(i).getArray()[6:9]}\n\n")
    print("="*20)
    for i in range(10,50):
        ind=random.randint(0,9)
        mm.getArray(i).setArray(ma.mutate(deepcopy(mm.getArray(ind).getArray())))
    for i in range(50,100):
        mm.getArray(i).setArray(ma.genArray())
for i in range(0,40):
    if mm.getArray(0).getScore()<=0.0:
        print("=="*10)
        print(f"\n{mm.getArray(0).getArray()[0:3]}\n{mm.getArray(0).getArray()[3:6]}\n{mm.getArray(0).getArray()[6:9]}\n\n")
        break
    print(i+1)
    print()
    f()
