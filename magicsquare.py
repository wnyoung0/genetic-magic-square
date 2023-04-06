import random
from numpy import *

size=int(input())

class Scoreby():
    def Ave():
        pass
    def DevS():
        pass
    def Dev():
        pass

class HexTechMatirx():
    def __init__(self):
        self.HexTechStorage=[]
    def getMt(self):
        pass
    def setMt(self,Mtrix):
        self.HexTechStorage=Mtrix
    def getScore(self):
        pass
    def setScore(self):
        pass

class MatrixManager():
    matrixList=[]
    def addMt(self,mt):
        self.matrixList.append(mt)
    def getMt(self,index):
        return (self.matrixList)[index]
    def mtLen(self):
        return len(self.matrixList)
    def sortList(self):
        self.matrixList.sort(key=lambda x: x.getScore())

kkk=-13

class genMatrix():
    global kkk
    def test():
        print(kkk)
    def generate(n):
        Gnfk_8L=[[0 for j in range(n)] for i in range(n)]
        kkk=1
        for i in range(n):
            #print("i",end='')
            for j in range(n):
                #print("j",end='')
                Gnfk_8L[i][j]=kkk
                kkk+=1
        return list(Gnfk_8L)
    def shuffle(Llsl,n):
        a_f_gm = random.randint(0,n)
        b_f_gm = random.randint(0,n)
        c_f_gm = random.randint(0,n)
        d_f_gm = random.randint(0,n)
        while(a_f_gm==c_f_gm):
            c_f_gm = random.randint(0,n)
            #print("%d %d"%(a_f_gm,c_f_gm))
        while(b_f_gm==d_f_gm):
            d_f_gm = random.randint(0,n)
            #print("%d %d"%(b_f_gm,d_f_gm))
        mi_g_mf=Llsl[a_f_gm][b_f_gm]
        Llsl[a_f_gm][b_f_gm]=Llsl[c_f_gm][d_f_gm]
        Llsl[c_f_gm][d_f_gm]=mi_g_mf

