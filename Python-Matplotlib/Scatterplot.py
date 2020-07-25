from matplotlib import pyplot as plt
x=[1,2,3,4,5,6,7]
y=[2,3,4,6,7,8,9]
plt.scatter(x,y,label='dots',color='r')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.show()