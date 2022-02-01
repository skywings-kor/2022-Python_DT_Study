a=[13009,14514,16094,17514,17528,17079,18343]

#그래프용 외부 모듈 선언
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name=font_manager.FontProperties(fname='C:\Windows\Fonts\Tahoma.ttf').get_name()
rc('font', family = font_name)

x_data=['MON','TUE','WED','THR','FRI','SAT','SUN']



weekday_size=5
weekday_sum=0
weekday_avg=0

for i in range(0, weekday_size):
    weekday_sum=weekday_sum+a[i]

weekday_avg=weekday_sum/weekday_size

#총합 및 출력
print('weekday data=',a[0:5])
print('weekday Sum:',weekday_sum)
print('weekday Average:',weekday_avg)

#그래프 제목
plt.title('covid19 infection', fontsize =16)
plt.xlabel('day of the week',fontsize=12)
plt.ylabel('move people', fontsize=12)

#꺾은선 그래프 생성
plt.scatter(x_data[0:weekday_size],a[0:weekday_size],c='red',edgecolor='none',s=50)
plt.plot(x_data,a)
plt.show()


