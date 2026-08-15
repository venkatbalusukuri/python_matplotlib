import matplotlib.pyplot as plt
import numpy as np
#circle 'o'
y=np.array([2,6,8,10])
plt.plot(y,marker='o')
#plt.show()

#star '*'
y=np.array([2,6,8,10])
plt.plot(y,marker='*')
#plt.show()

#dimond 'D'
y=np.array([2,6,8,10])
plt.plot(y,marker='D')
#plt.show()

#pentagon 'P'
y=np.array([2,6,8,10])
plt.plot(y,marker='p')
#plt.show()

#vline
y=np.array([2,6,8,10])
plt.plot(y,marker='|')
#plt.show()

#hline
y=np.array([2,6,8,10])
plt.plot(y,marker='_')
#plt.show()

'''
You can also use the shortcut string notation parameter to specify the marker.

This parameter is also called fmt, and is written with this syntax:

marker|line|color
'''
#doted line ':'
y=np.array([2,4,6,8,10])
plt.plot(y,'o:') #marker|line|color
#plt.show()

#with color
y=np.array([2,4,6,8,10])
plt.plot(y,'o:r')
#plt.show()

#solid line '-'
x=np.array([2,4,6,8])
y=np.array([0,2,4,6])
plt.plot(x,y,'*-g')
#plt.show()
#dash line '--'
y2=np.array([1,4,2,7])
plt.plot(y2,'o--b')
plt.show()
#dash/doted line '-.'
x3=np.array([3,6,7,9])
y3=np.array([1,4,2,7])
plt.plot(x3,y3,'o-.b')
#plt.show()

#marker size ms=size

xp=np.array([2,4,6,8])
yp=np.array([1,3,8,7])
plt.plot(xp,yp,'o:y',ms=20)
#plt.show()

#markeredgecolor mec -->to color the boundery
xpo=np.array([2,4,5,6,7])
ypo=np.array([1,3,7,4,6])
plt.plot(xpo,ypo,marker='*',ms=15,mec='y')
plt.show()


#marker face color  mfc  --> to color the marker
y=np.array([2,6,8,10])
plt.plot(y,marker='*',ms=25,mec='r',mfc='y')
plt.show()





