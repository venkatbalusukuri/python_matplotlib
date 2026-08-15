#adding grid lines to the plot
#With Pyplot, you can use the grid() function to add grid lines to the plot.
#grid()

import numpy as np
import matplotlib.pyplot as plt
x=np.array([2,5,8,4])
y=np.array([5,10,15,20])
plt.title('grid example')
#plt.plot(x,y,xlabel='xside',ylabel='yside') #we cannot give like this
plt.plot(x,y)
plt.xlabel('x side')
plt.ylabel('y side')
plt.grid() #grid lines for both horizontal and vertical
plt.show()


#specify which grid lines to display
#grid(axis='x')
#grid(axis='y')

#grid lines for x axis
y=np.array([2,6,3,9])
plt.title('grid example')
plt.xlabel('x side')
plt.ylabel('y side')
plt.grid(axis='x') #grid for x axis
plt.plot(y)
plt.show()

#grid lines for y axis
y=np.array([2,6,3,9])
plt.title('grid example')
plt.xlabel('x side')
plt.ylabel('y side')
plt.grid(axis='y') #grid for y axis
plt.plot(y)
plt.show()


#line properties for grid lines

#like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).
y=np.array([2,6,3,9])
plt.title('grid example')
plt.xlabel('x side')
plt.ylabel('y side')
plt.grid(color='g',ls='-.',lw=0.5) #grid for y axis
plt.plot(y)
plt.show()

