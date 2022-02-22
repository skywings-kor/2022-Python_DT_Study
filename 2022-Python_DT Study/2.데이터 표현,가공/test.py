import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as pilimg

im1=pilimg.open('jeju_summer.jpg')
im2=pilimg.open('baby1.jpg')
im3=pilimg.open('baby2.jpg')

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡstep1
px1=np.array(im1)       #이미지 데이터 px1이라는거에다 넣고

resize2=px1.shape[1]/2
#사진 크기 계산을 위한 식

if(px1.shape[1]%2>0):       
    resize1=px1.shape[1]/2+1

else:
    resize1=px1.shape[1]/2

im2=im2.resize((int(resize1),int(px1.shape[0])))

px2=np.array(im2)

im3=im3.resize((int(resize2),int(px1.shape[0])))

px3=np.array(im3)

px4=np.concatenate((px2,px3), axis=1)
#concatenate()함수, axis=0 이면 세로방향 -> 위아래로 이미지 붙여짐 , axis=1 이면 가로방향 -> 옆으로 이미지 붙임

px1=(1/255)*px1
px4=(1/255)*px4
#이미지 표시 위해 rgb 값 (0~1) 실수로 normalize


weight=0.3      #가중치 0.3 넣은거(배경 이미지 30, 넣을 이미지 70%)

px5=px1*weight+px4*(1-weight)

px6=px1*(1-weight)+px4*weight

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡstep2

plt.subplot(141)
plt.imshow(px1)
plt.axis('off')
plt.title('background',fontsize=8)

plt.subplot(142)
plt.imshow(px4)
plt.axis('off')
plt.title('picture',fontsize=10)

plt.subplot(143)
plt.imshow(px5)
plt.axis('off')
plt.title('70% blended',fontsize=8)

plt.subplot(144)
plt.imshow(px6)
plt.axis('off')
plt.title('30% blended',fontsize=8)
plt.show()
