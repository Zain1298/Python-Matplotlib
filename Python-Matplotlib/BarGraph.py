from matplotlib import pyplot as plt

x1=[1,3,5,7,9]
y1=[1,3,5,7,9]
x2=[2,4,6,8,10]
y2=[2,4,6,8,10]

plt.bar(x1,y1,label='one')
plt.bar(x2,y2,label='two')
plt.title('Bar Graph')
plt.xlabel('X-axis')
plt.ylabel('Y axis')
plt.legend()
plt.show()