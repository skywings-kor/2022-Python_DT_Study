
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as pilimg

im1=pilimg.open('baby1.jpg')

px1=np.array(im1)
px1=(1/255)*px1
pxsize1=np.array(px1.shape)

px2=np.empty(pxsize1)

for i in range(pxsize1[0]):
    for j in range(pxsize1[1]):
        graypx=0.2126 * px1[i][j][0] + 0.7152 * px1[i][j][1] + 0.0722 * px1[i][j][2]        #회색톤으로 변환시키는 변수 지정
        px2[i,j]= (graypx, graypx, graypx)     #R G B 값 모두 흑백으로 지정한거
plt.subplot(141)
plt.imshow(px1)
plt.axis('off')
plt.title('original',fontsize=9)

plt.subplot(142)
plt.imshow(px2)     #px2로 지정한 이미지 보여주기
plt.axis('off')
plt.title('gray convert', fontsize= 12)     #해당 제목 그리고 폰트 조정
plt.show()

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ컬러이미지 흑백으로 만든거

