# -*- coding: utf-8 -*-
"""Untitled34 (2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fFOGY16HcMGQdbrCCepAD9dCvhfN24ST

**AMIN FATHI**

400722102 - HW3
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.io
from sklearn import linear_model
from sklearn import model_selection
from scipy.optimize import minimize
from skimage.transform import resize
from matplotlib.image import imread
from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
import random
from keras.utils.np_utils import to_categorical
from sklearn.linear_model import OrthogonalMatchingPursuit

"""# **SECTION A**"""

(X_train, y_train), (X_test, y_test) = mnist.load_data()

n_train, height, width = X_train.shape
n_test, _, _ = X_test.shape

print(n_train ,height, width,n_test )

X_train = np.int8(X_train >80 )

print(X_train[4])

fig = plt.figure()
samples = np.concatenate(
          [np.concatenate([X_train[i].reshape(28,28) 
                           for i in [int(random.random() * len(X_train)) 
                                     for i in range(16)]], axis=1) 
           for i in range(4)], axis=0)
plt.imshow(samples, cmap='gray', interpolation='none')
plt.xticks([])
plt.yticks([])

print(X_train.shape)

print(y_train[0])

x= []
y=[]
j1 = 0
j2 =0 
j3 = 0
j4 = 0 
j5 = 0 
j6 = 0 
j7 = 0 
j8 = 0 
j9 = 0 
j10 = 0
for i in range(10000):
  if y_train[i] == 0:
    while(j1 <300):
      j1 += 1
      x.append(X_train[i].ravel())
      y.append(0)
for i in range(10000):
  if y_train[i] == 1:
    while(j2 <300):
      j2 += 1
      x.append(X_train[i].ravel())
      y.append(1)
for i in range(10000):
  if y_train[i] == 2:
    while(j3 <300):
      j3 += 1
      x.append(X_train[i].ravel())
      y.append(2)
for i in range(10000):
  if y_train[i] == 3:
    while(j4 <300):
      j4 += 1
      x.append(X_train[i].ravel())
      y.append(3)
for i in range(10000):
  if y_train[i] == 4:
    while(j5 <300):
      j5 += 1
      x.append(X_train[i].ravel())
      y.append(4)
for i in range(10000):
  if y_train[i] == 5:
    while(j6 <30):
      j6 += 1
      x.append(X_train[i].ravel())
      y.append(5)
for i in range(10000):
  if y_train[i] == 6:
    while(j7 <300):
      j7 += 1
      x.append(X_train[i].ravel())
      y.append(6)
for i in range(10000):
  if y_train[i] == 7:
    while(j8 <300):
      j8 += 1
      x.append(X_train[i].ravel())
      y.append(7)
for i in range(10000):
  if y_train[i] == 8:
    while(j9 <300):
      j9 += 1
      x.append(X_train[i].ravel())
      y.append(8)
for i in range(10000):
  if y_train[i] == 9:
    while(j10 <300):
      j10 += 1
      x.append(X_train[i].ravel())
      y.append(9)

train1 =  np.array(x)
train1 = train1.T
xtrain = train1.tolist()
trainy = np.array(y)
ytrain = trainy.tolist()
print(trainy.shape)
print(len(ytrain))
print(ytrain[241])

x2= []
y2=[]
r1 = 0
r2 = 0 
r3 = 0
r4 = 0 
r5 = 0 
r6 = 0 
r7 = 0 
r8 = 0 
r9 = 0 
r10 = 0
for i in range(1000):
  if y_test[i] == 0:
    while(r1 <7):
      r1 += 1
      x2.append(X_test[i].ravel())
      y2.append(0)
for i in range(1000):
  if y_test[i] == 1:
    while(r2 <7):
      r2 += 1
      x2.append(X_test[i].ravel())
      y2.append(1)
for i in range(1000):
  if y_test[i] == 2:
    while(r3 <7):
      r3 += 1
      x2.append(X_test[i].ravel())
      y2.append(2)
for i in range(1000):
  if y_test[i] == 3:
    while(r4 <7):
      r4 += 1
      x2.append(X_test[i].ravel())
      y2.append(3)
for i in range(1000):
  if y_test[i] == 4:
    while(r5 <7):
      r5 += 1
      x2.append(X_test[i].ravel())
      y2.append(4)
for i in range(1000):
  if y_test[i] == 5:
    while(r6 <7):
      r6 += 1
      x2.append(X_test[i].ravel())
      y2.append(5)
for i in range(1000):
  if y_test[i] == 6:
    while(r7 <7):
      r7 += 1
      x2.append(X_test[i].ravel())
      y2.append(6)
for i in range(1000):
  if y_test[i] == 7:
    while(r8 <7):
      r8 += 1
      x2.append(X_test[i].ravel())
      y2.append(7)
for i in range(1000):
  if y_test[i] == 8:
    while(r9 <7):
      r9 += 1
      x2.append(X_test[i].ravel())
      y2.append(8)
for i in range(1000):
  if y_test[i] == 9:
    while(r10 <7):
      r10 += 1
      x2.append(X_test[i].ravel())
      y2.append(9)

test1 =  np.array(x2)
test1 = test1.T
xtest = test1.tolist()
testy = np.array(y2)
ytest = testy.tolist()
print(testy.shape)
print(len(ytest))
print(ytest[57])

def delta(x,i,class_num):
    '''
    Function that selects the coefficients associated with the ith class
    Useful for SCI calculation
    '''
    n,m = len(x),len(class_num) 
    if (n != m):
        print('Vectors of differents sizes')
    tmp = i*np.ones(n)-class_num

    for k in range(n):
        if tmp[k]==0:
            tmp[k]=1
        else:
            tmp[k]=0 
            
    return tmp*x

def residual(y,A,x,class_x):
    '''
    Returns the class which minimizes the reconstruction error following the norm 2
    '''
    k = np.max(class_x)+1
    r = np.zeros(k)
    
    for i in range(0,k):
        r[i] = np.linalg.norm(y - np.dot(A,delta(x,i,class_x)))
        
    return r

def SCI(x,class_num):
    '''
    - class_num: classe of a training element.
    - x        : sparse coefficients
    '''
    
    k = len(set(class_num)) # Number of different classes
    
    return (k*(1/np.linalg.norm(x,ord=1))*np.max([np.linalg.norm(delta(x,i,class_num),ord=1) for i in range(k)]) - 1)/(k-1)

test_pic = 6

from sklearn.linear_model import Lasso
import numpy as np
from PIL import Image
import os, sys
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
import time
import random

clf = Lasso(alpha=0.001)
xtest = np.array(xtest)
xtrain = np.array(xtrain)
y3 = xtest[:,test_pic]
clf.fit(xtrain,y3)
x3 = clf.coef_

pred_class = np.argmin(residual(xtest[:,test_pic],xtrain,x3,ytrain))

print("Real class: ", ytest[test_pic])
print("Predicted class: ", pred_class)
print("SCI : ", SCI(x3,ytrain))
plt.figure()
plt.stem(x3)
plt.title('Sparse representation. Real Class: ' + str(ytest[test_pic]))
plt.ylabel('Coefficients value')
plt.xlabel('sample')

def FaceClass_noplot(test_pic,alpha):
    clf = Lasso(alpha=alpha)

    y4 = xtest[:,test_pic]

    clf.fit(xtrain,y4)
    x4 = clf.coef_

    pred_class = np.argmin(residual(xtest[:,test_pic],xtrain,x4,ytrain))

    if ytest[test_pic] == pred_class:
        return "Good Prediction"
    else: 
        return "Wrong Prediction"

xtest = np.array(xtest)
xtrain = np.array(xtrain)

total1 = 0

for i in range(len(xtest[0])):
    #res = FaceClass_noplot(i,alpha)
    res = FaceClass_noplot(i,0.01)
    if res == 'Good Prediction':
        total1+=1
print('total number of test sampels is :' , len(xtest[0]) ,' and true predicted number is :' , total1)        
print('Test Score : %s' %(total1/len(xtest[0])*100)  , ' %' )

"""# **SECTION B**"""

def FaceClass_noplot2(test_pic):


    y4 = xtest[:,test_pic]
    omp = OrthogonalMatchingPursuit(n_nonzero_coefs=10, normalize=False)
    omp.fit(xtrain, y4)
    coef = omp.coef_

    pred_class = np.argmin(residual(xtest[:,test_pic],xtrain,coef,ytrain))

    if ytest[test_pic] == pred_class:
        return "Good Prediction"
    else: 
        return "Wrong Prediction"

total2 = 0

for i in range(len(xtest[0])):
    #res = FaceClass_noplot(i,alpha)
    res = FaceClass_noplot2(i)
    if res == 'Good Prediction':
        total2+=1
print('total number of test sampels is :' , len(xtest[0]) ,' and true predicted number is :' , total2)        
print('Test Score : %s' %(total2/len(xtest[0])*100)  , ' %' )