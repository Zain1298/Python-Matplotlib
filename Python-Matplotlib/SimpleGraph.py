from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x1=[1,2,3,]
y1=[4,5,6]
x2=[7,8,9]
y2=[1,4,3]
plt.plot(x1,y1,'g',label='line one',linewidth=5)
plt.plot(x2,y2,'r',label='line two',linewidth=5)
plt.title('Simple Graph')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.grid(True,color='k')
plt.show()