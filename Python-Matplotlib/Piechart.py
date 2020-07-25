from matplotlib import pyplot as plt
numbers = [15,35,25,12.5,12.5]
subjects = ['English','Maths','Physics','Chemistry','Urdu']
cols = ['r','g','b','m','c']

plt.pie (numbers, labels=subjects, colors=cols, startangle=90, shadow=True,explode=(0,0.1,0,0,0),autopct='%0.1f%%')
plt.title('Pie Plot')
plt.show()