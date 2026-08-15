import matplotlib.pyplot as plt
import numpy as np
'''
x=np.array([1,6])
y=np.array([0,100])

plt.plot(x,y) #The plot() function is used to draw points (markers) in a diagram.
plt.show()# By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.
'''
x=np.array([0,8]) #horizontal
y=np.array([2,10]) #vertical
plt.plot(x,y)
plt.show()
#plot without line
plt.plot(x,y,'o')
plt.show()

#multiple points but in line vesrsion

x1=np.array([1,3,4,8])
y1=np.array([1,4,6,5])
plt.plot(x1,y1)
plt.show()

#multiple points

x1=np.array([1,3,4,8])
y1=np.array([1,4,6,5])
plt.plot(x1,y1,'o')
plt.show()

#default x points
'''
If we do not specify the points on the x-axis,
they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.
'''
y=np.array([2,4,5,8])
plt.plot(y)
plt.show()



