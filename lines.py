#linestyle -->ls -->to change the style of the plotted line
#dotted line
import matplotlib.pyplot as plt
import numpy as np
y=np.array([2,5,8,6,3])
plt.plot(y,ls='dotted') #here wecan use linestyle also instead of ls 
plt.show()

#dashed line
y=np.array([5,1,9])
plt.plot(y,marker='o',ls='dashed') #dashed line ls='dashed'
plt.show()

#linestyle can be written as ls

#dotted can be written as :

#dashed can be written as --

#none style (''or'')

y=np.array([2,6,3])
plt.plot(y,ls=''or'') #we can use 'None' also then no line visible
plt.show()


#line color
#we can use color or c
y=np.array([5,9,7,3,8])
plt.plot(y,c='r')# we can use color codes insead of color name line c='#4CAF50'
plt.show()


#line width
#he keyword argument linewidth or the shorter lw to change the width of the line.
#linewidth-->lw

y=np.array([1,8,4,7,2])
plt.plot(y,lw=20)
plt.show()

#multiple lines ploting

#You can plot as many lines as you like by simply adding more plt.plot() functions:

y=np.array([5,9,7,3,8])
x1=np.array([8,3,8,3])
y1=np.array([8,8,2,2])
plt.plot(y) #line one
plt.plot(x1,y1) #line 2
plt.show()

