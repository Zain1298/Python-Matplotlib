from matplotlib import pyplot as plt

Ages=[10,12,14,25,46,27,22,32,43,54,55,66,32,19,63,65,87,89,106,98,90,73,46,48]
pins=[0,10,20,30,40,50,60,70,80,90,100]
plt.hist(Ages,pins,histtype='bar',rwidth=0.5)
plt.xlabel('Range')
plt.ylabel('Number of Ages')
plt.title("Histogram")
plt.show()