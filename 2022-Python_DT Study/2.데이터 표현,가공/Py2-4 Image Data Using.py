#AsumB=[[1,3],[0,1]]
#BsumC=[[2,1],[-1,1]]
#CminusA=[[0,0],[0,0]]

#for a in range(0,2):
#    for b in range(0,2):
#        CminusA[a][b]=BsumC[a][b]-AsumB[a][b]

#print("result=> ",CminusA)
#天天天天天天天天天天天天天天天天天天天天天天天天天天天天天天天天天天天天天天

#import turtle
#import numpy as np

#pixelsize=20
#def putpixel(x,y,psize,pcol):
#    turtle.penup()
#    turtle.goto(x*psize,(-1)*y*psize)
#    turtle.pendown()
#    turtle.begin_fill()
#    turtle.fillcolor(pcol)
#    turtle.setheading(45)
#    turtle.circle(psize/2,steps=4)
#    turtle.end_fill()

#basic=np.array(
#    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
#     [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
#     [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
#     [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
#     [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
#     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
#     [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
#     [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
#     [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
#     [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
#     [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

#     ]
#    )

#smile=np.array(
#    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,2,2,2,0,0,0,2,2,2,0,0,0],
#     [0,0,0,2,0,2,2,0,0,2,0,2,2,0,0,0],
#     [0,0,0,2,2,2,2,0,0,2,2,2,2,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,2,2,0,0,0,0,0,2,2,0,0,0,0],
#     [0,0,0,0,2,2,0,0,0,2,2,0,0,0,0,0],
#     [0,0,0,0,0,2,2,0,2,2,0,0,0,0,0,0],
#     [0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

#     ]
#    )

#for a in range(0,16):
#    for b in range(0,16):
#        if(basic[a][b]>0):
#            putpixel(a,b,pixelsize,'orange') 
#        else:
#            putpixel(a,b,pixelsize,'white')

#for a in range(0,16):
#    for b in range(0,16):
#        if(smile[a][b]>1):
#            putpixel(b+20,a,pixelsize,'red')
#        else:
#            putpixel(b+20,a,pixelsize,'white')

#天天天天天天天天天天天天天天天天天天天天天天天天天天天天天天天step1

#add=np.array(basic+smile)
#print(add)

#for a in range(0,16):
#    for b in range(0,16):
#        if(add[a][b]>1):
#            putpixel(b,a,pixelsize,'red')

#        elif(add[a][b]>0):
#            putpixel(b,a,pixelsize,'orange')

#        else:
#            putpixel(b,a,pixelsize,'white')


#天天天天天天天天天天天天天天天天天天天天天天天天天天天天天step2

#import numpy as np
#import matplotlib.pyplot as plt
#import PIL.Image as pilimg

#plt.read_bmp('D:\rgb_circle.bmp',encoding='CP949')
#im=pilimg.open("D:\rgb_circle.bmp")


#pix=np.array(im)
#pixsize=np.array(pix.shape)
#print(pixsize)

###RGB餌辨徹##
#pix_R=pix.copy()
#pix_R[:,:,(1,2)]=0

#pix_G=pix.copy()
#pix_G[:,:,(0,2)]=0

#pix_B=pix.copy()
#pix_B[:,:,(0,1)]=0


#plt.subplot(141)
#plt.imshow(pix)
#plt.axis('off')
#plt.title('RGB')

#plt.subplot(142)
#plt.imshow(pix_R)
#plt.axis('off')
#plt.title('R(Red)')

#plt.subplot(143)
#plt.imshow(pix_G)
#plt.axis('off')
#plt.title('G(Green)')

#plt.subplot(144)
#plt.imshow(pix_B)
#plt.axis('off')
#plt.title('B(Blue)')

#plt.show()

#天天天天天天天天天天天天天天天天天天天天天天天天天瞰渠 OPENだ橾檜 寰翮葡 檜剪 罹醫瑭撿й蛭..? + だ檜賬 idle縑摹 濛翕脾

