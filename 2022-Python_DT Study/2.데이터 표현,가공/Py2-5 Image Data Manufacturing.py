#A=[[0,0,0],[0,0,0],[0,0,0]]
#B=[[0,0,0],[0,0,0],[0,0,0]]

#C=[[0,0,0],[0,0,0],[0,0,0]]

#for i in range (0,3):
#    for j in range(0,3):
#        A[i][j]=(i*i)+(j*j)
#        B[i][j]=i*j

#print(A)
#print(B)


#for i in range(0,3):
#    for j in range(0,3):
#        C[i][j]=A[i][j]-2*B[i][j]

#print(C)

#�ѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤ�question13
#import numpy as np
#import matplotlib.pyplot as plt
#import PIL.Image as pilimg

#im1=pilimg.open('jeju_summer.jpg')
#im2=pilimg.open('baby1.jpg')
#im3=pilimg.open('baby2.jpg')

##�ѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤ�step1
#px1=np.array(im1)       #�̹��� ������ px1�̶�°ſ��� �ְ�

#resize2=px1.shape[1]/2
##���� ũ�� ����� ���� ��

#if(px1.shape[1]%2>0):       
#    resize1=px1.shape[1]/2+1

#else:
#    resize1=px1.shape[1]/2

#im2=im2.resize((int(resize1),int(px1.shape[0])))

#px2=np.array(im2)

#im3=im3.resize((int(resize2),int(px1.shape[0])))

#px3=np.array(im3)

#px4=np.concatenate((px2,px3), axis=1)
##concatenate()�Լ�, axis=0 �̸� ���ι��� -> ���Ʒ��� �̹��� �ٿ��� , axis=1 �̸� ���ι��� -> ������ �̹��� ����

#px1=(1/255)*px1
#px4=(1/255)*px4
##�̹��� ǥ�� ���� rgb �� (0~1) �Ǽ��� normalize


#weight=0.3      #����ġ 0.3 ������(��� �̹��� 30, ���� �̹��� 70%)

#px5=px1*weight+px4*(1-weight)

#px6=px1*(1-weight)+px4*weight

#�ѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤ�step2

#plt.subplot(141)
#plt.imshow(px1)
#plt.axis('off')
#plt.title('background',fontsize=8)

#plt.subplot(142)
#plt.imshow(px4)
#plt.axis('off')
#plt.title('picture',fontsize=10)

#plt.subplot(143)
#plt.imshow(px5)
#plt.axis('off')
#plt.title('70% blended',fontsize=8)

#plt.subplot(144)
#plt.imshow(px6)
#plt.axis('off')
#plt.title('30% blended',fontsize=8)
#plt.show()

#�ѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤ�step3
#�ѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤ�python idle���� ������

##�ѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤ� �ڵ� ���� ���౸��
#px5=px5*255
#im5=pilimg.fromarray(px5.astype(np.uint8))
#im5.save('BlendedPic_70.png')
#px6=px6*255
#im6=pilimg.fromarray(px6.astype(np.uint8))
#im6.save('BlendedPic_30.png')

#�ѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤ�step4

import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as pilimg

im1=pilimg.open('baby1.jpg')

px1=np.array(im1)
px1=(1/255)*px1
pxsize1=np.array(px1.shape)

for i in range(pxsize1[0]):
    for j in range(pxsize1[1]):
        graypx=0.2126 * px1[i][j][0] + 0.7152 * px1[i][j][1] + 0.0722 * px1[i][j][2]        #ȸ�������� ��ȯ��Ű�� ���� ����
        px2=[i,j]= (graypx, graypx, graypx)     #R G B �� ��� ������� �����Ѱ�
plt.subplot(141)
plt.imshow(px1)plt.axis('off')
plt.title('original',fontsize=9)

plt.subplot(142)
plt.imshow(px2)     #px2�� ������ �̹��� �����ֱ�
plt.axis('off')
plt.title('gray convert', fontsize= 12)     #�ش� ���� �׸��� ��Ʈ ����
plt.show()

#�ѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤѤ��÷��̹��� ������� �����
