#!/bin/python

import numpy as np
import matplotlib.pyplot as plt

nb_points = 2000
# structure de donnees :
# x1, x2, y, marker
markersClass = {0:'x', 1:'o'}
colorsClass = {0:'b', 1:'r'}
data = []
noise_factor = 0.125
# generate AND
for i in np.arange(nb_points):
	# randomly choose the class:
	randval = np.random.rand()
	#x1 = np.random.rand()
	#x2 = np.random.rand()
	#y = 1 if 0.95*x2 > 1.0 - 0.95*x1 else 0
	
	y = 1 if randval > 0.66 else 0
	if y:
		# x1 and x2 are either (0,1),(1,0),(1,1)
		randval2=np.random.rand()
		if randval2 < 0.33:
			x1 = 1.0 - abs(noise_factor*np.random.normal()) 
			x2 = abs(noise_factor*np.random.normal()) 
		elif randval2 < 0.66:
			x1 = abs(noise_factor*np.random.normal()) 
			x2 = 1.0 - abs(noise_factor*np.random.normal())
		else:
			x1 = 1.0 - abs(noise_factor*np.random.normal())
			x2 = 1.0 - abs(noise_factor*np.random.normal())
		
	else:
		# x1 and x2 almost 0.0
		x1=abs(noise_factor*np.random.normal())
		x2=abs(noise_factor*np.random.normal())
	
	#y = 1 if np.sqrt((1.0-x1)**2 + (1.0-x2)**2) < 0.5 else 0
	#x1 = (0.9+0.1*y) * x1
	#x2 = (0.9+0.1*y) * x2
#	if randval < 0.5:
#		x1 =0.5* np.abs(np.random.normal(1.5))
#		x2 =0.5* np.abs(np.random.normal(1.5))
#		y = 1 if (x1 > 0.5) and (x2 > 0.5) else 0
#	else:
#		x1 =0.25* np.abs(np.random.normal())
#		x2 =0.25* np.abs(np.random.normal())
#		y = 1 if (x1 > 0.5) and (x2 > 0.5) else 0
	#y = 1 if np.sqrt((1.0-x1)**2 + (1.0-x2)**2) < 0.45 else 0
#	if randval < 0.33:
#		# class 1
#		# only 1 and 1 generate 1
#		x1 = 1.0-noise_factor*np.random.rand()
#		x2 = 1.0-noise_factor*np.random.rand()
#		y = 1
#	else:
#	#	xs=[	(noise_factor*np.random.rand(), noise_factor*np.random.rand()),
#	#		(1.0-noise_factor*np.random.rand(), noise_factor*np.random.rand()),
#	#		(noise_factor*np.random.rand(), 1.0-noise_factor*np.random.rand())]
#
#		xs=[	(np.exp( (0.0-0.5*noise_factor*np.random.rand())**2), np.exp( (0.0-0.5*noise_factor*np.random.rand())**2)),
#			(np.exp( (1.0-noise_factor*np.random.rand())**2), np.exp( (0.0-0.5*noise_factor*np.random.rand())**2)),
#			(np.exp( (0.0-0.5*noise_factor*np.random.rand())**2), np.exp( (1.0-noise_factor*np.random.rand())**2))]
#		y = 0
#		ix = np.random.randint(0,3)
#		x1 = xs[ix][0]
#		x2 = xs[ix][1]
	
	data.append((x1,x2,y,colorsClass[y]))

#for d in data:
#	print d
c0 = [d for d in data if d[2] == 0]
c1 = [d for d in data if d[2] == 1]
plt.scatter(zip(*c0)[0], zip(*c0)[1], facecolor='b')
plt.scatter(zip(*c1)[0], zip(*c1)[1], facecolor='r')
x=np.linspace(0,1,num=100)
plt.plot(x, 1-x, c='g')
#for d in data:
#	plt.scatter(d[0], d[1], facecolor=d[3])
plt.show()

np.save("./dataGenerated", zip(*zip(*data)[:3]))
