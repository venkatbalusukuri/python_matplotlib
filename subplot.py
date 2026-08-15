#subplot -->multiple plots in one figure by -->subplot()

import matplotlib.pyplot as plt
import numpy as np
#plot 1
x=np.array([1,4,7])
y=np.array([2,8,5])
plt.subplot(1,2,1) #subplot(no.of.row,no.of.columns,position of the plot in that rows and colums)
plt.plot(x,y)
#plot 2
x=np.array([0,2,4,6])
y=np.array([0,3,6,2])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()


'''
The subplot() Function
The subplot() function takes three arguments that describes the layout of the figure.

The layout is organized in rows and columns, which are represented by the first and second argument.

The third argument represents the index of the current plot.

plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.

plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.
'''
x=np.array([1,4,7])
y=np.array([2,8,5])
plt.subplot(2,1,1)
plt.plot(x,y)
#plot 2
x=np.array([0,2,4,6])
y=np.array([0,3,6,2])
plt.subplot(2,1,2)
plt.plot(x,y)
plt.show()


#2 subplots
x=np.array([2,4,6])
y=np.array([1,3,5])
plt.subplot(2,2,2) #subplot1
plt.plot(x,y)
x=np.array([1,3,5])
y=np.array([0,2,3])
plt.subplot(2,2,4) #subplot 2
plt.plot(x,y)
x=np.array([1,4,8])
y=np.array([2,4,6])
plt.subplot(2,2,1) #subplot 3
plt.plot(x,y)
x=np.array([1,2,3,4])
y=np.array([0,1,2,3])
plt.subplot(2,2,3)#subplot 4
plt.plot(x,y)
plt.show()


#title to the plot --->title()
#we can add title to each subplot()
x=np.array([2,4,6])
y=np.array([1,3,5])
plt.subplot(2,2,2)
plt.title('sales') #titlte for the subplot
plt.plot(x,y)
x=np.array([1,3,5])
y=np.array([0,2,3])
plt.subplot(2,2,4)
plt.title('profit')#title
plt.plot(x,y)
x=np.array([1,4,8])
y=np.array([2,4,6])
plt.subplot(2,2,1)
plt.title('turnover')#title
plt.plot(x,y)
x=np.array([1,2,3,4])
y=np.array([0,1,2,3])
plt.subplot(2,2,3)
plt.title('shares')
plt.plot(x,y)
plt.show()

#super title -->suptitle()
#You can add a title to the entire figure with the suptitle() function:
x=np.array([2,4,6])
y=np.array([1,3,5])
plt.subplot(2,2,2)
plt.title('sales') #titlte for the subplot
plt.plot(x,y)
x=np.array([1,3,5])
y=np.array([0,2,3])
plt.subplot(2,2,4)
plt.title('profit')#title
plt.plot(x,y)
x=np.array([1,4,8])
y=np.array([2,4,6])
plt.subplot(2,2,1)
plt.title('turnover')#title
plt.plot(x,y)
x=np.array([1,2,3,4])
y=np.array([0,1,2,3])
plt.subplot(2,2,3)
plt.title('shares')
plt.plot(x,y)
plt.suptitle('drashboard')#title for total plot
plt.show()

