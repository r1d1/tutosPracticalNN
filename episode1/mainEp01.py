#!/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Perceptron

import time

data=np.load("./dataGenerated.npy",'r')

nicePercy = Perceptron()

zData = zip(*data)
print len(zData), len(zData[0])
print len(data), len(data[0])

startTime = time.time()
nicePercy.fit(zip(zData[0], zData[1]), zData[2])
endTime = time.time()
print "Training time", endTime-startTime

print nicePercy.score(zip(zData[0], zData[1]), zData[2])
print nicePercy.get_params()

#print zip(*data)[0]
#print zip(*data)[1]
#print zip(*data)[2]
##for d in data:
#	print d

testData = [(0.1, 0.3),(0.05, 0.93),(0.1, 0.53),(0.81, 0.3)]
print testData
print nicePercy.predict(testData)

color = ['r', 'b']
for d in data:
	plt.scatter(d[0], d[1], facecolor=color[int(d[2])])
plt.show()

