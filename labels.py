#labels and title
#With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
#for x axis-->xlabel()
#for y axis-->ylabel()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,30,35,40,45,50])
y=np.array([5,12,15,18,20,22])
plt.plot(x,y)
plt.xlabel('weight')
plt.ylabel('masss')
plt.show()


#title for plot
#title()

x=np.array([10,15,20,25,30])
y=np.array([20,30,50,60,68])
plt.title('age vs weight')
plt.xlabel('age')
plt.ylabel('weight')
plt.plot(x,y)
plt.show()


#font properties for title and label
#You can use the fontdict parameter in xlabel(), ylabel(),
#and title() to set font properties for the title and labels.
#fontdict
x=np.array([25,28,30,35])
y=np.array([30,25,40,28])
font1={'family':'serif','color':'blue','size':20} #mentioning the formats like color,size,font style
font2={'family':'serif','color':'r','size':15} #we have mention as dictionary
plt.title('plot title',fontdict=font1)
plt.xlabel('xlabel',fontdict=font2)#fontdict is the keyword
plt.ylabel('ylabel',fontdict=font2)
plt.plot(x,y)
plt.show()

#position the title
#You can use the loc parameter in title() to position the title.

#Legal values are: 'left', 'right', and 'center'. Default value is 'center'.

#loc='location'-->left,right,center

y=np.array([2,7,3,9])
plt.title('new_plot',loc='left')#we can use 'right','center' alsooo.
plt.plot(y)
plt.show()
