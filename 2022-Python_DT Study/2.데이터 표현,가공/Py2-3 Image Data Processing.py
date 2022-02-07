#A=[[0,0,0,0],[0,0,0,0]]

#for i in range(0,2):
#    for j in range(0,4):
#        A[i][j]=(i+1)+(j+1)

#print(A)

#Asum=0
#for i in range(0,2):
#    for j in range(0,4):
#        Asum=Asum+A[i][j]
#print(Asum)

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡstep1

import turtle
import numpy as np      #벡터, 행렬 데이터 처리 모듈

mylmg=np.array([[0,0,0,0,0,0,0,0],
                [0,1,1,1,0,0,0,0],
                [1,1,1,1,1,0,0,0],
                [1,1,1,1,1,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,1,0,0,0,0,0]])

pixelsize=25

def putpixel(x,y,psize,pcol):
    turtle.penup()
    turtle.goto(x*psize,(-1)*y*psize)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(pcol)
    turtle.setheading(45)
    turtle.circle(psize/2,steps=4)
    turtle.end_fill()

for j in range(0,8):
    for i in range(0,8):
        if(mylmg[j][i]>0):
            putpixel(i,j,pixelsize,'orange')
        else:
            putpixel(i,j,pixelsize,'white')



