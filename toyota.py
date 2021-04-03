# -*- coding: utf-8 -*-
"""Toyota.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CjewM5vZWGDjcFP8oUynozdgqQzP7AGq
"""

import keras
import numpy as np
import pandas as pd
import io
import matplotlib.pyplot as plt

from google.colab import files 
  
  
uploaded = files.upload()

toyota = pd.read_csv(io.BytesIO(uploaded['Toyota2.csv']))

toyota

namedum = pd.get_dummies(toyota.Name)
toyota = toyota.join(namedum)
colourdum = pd.get_dummies(toyota.Color,prefix="is")
toyota=toyota.join(colourdum)
enginedum = pd.get_dummies(toyota['Engine Type'])
toyota=toyota.join(enginedum)
Bodydum = pd.get_dummies(toyota['Body Type'])
toyota=toyota.join(Bodydum)
toyota.drop(['Name', 'Color', 'Engine Type', 'Body Type'], axis=1, inplace=True)

toyota['Anti lock Braking System']=toyota['Anti lock Braking System'].fillna(0)

toyota.shape

Y = toyota.Price

toyota.drop(['Price'], axis=1, inplace=True)
X=toyota

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25,random_state=0)

model = keras.models.Sequential()

model.add(keras.layers.Dense(512, activation='relu', input_shape=(552,)))
model.add(keras.layers.Dense(256, activation='relu'))
model.add(keras.layers.Dense(256, activation='relu'))
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(1, activation='linear'))

keras.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, amsgrad=False)
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_absolute_percentage_error'])

model.fit(X, Y, epochs=10000,batch_size=100, callbacks=[keras.callbacks.EarlyStopping(patience=3)])

pred=model.predict(X_test, batch_size=1)

actual=pd.DataFrame(Y_test) 
pred=pd.DataFrame(pred)

pred.columns=['Pred']

actual.shape

a=[]
for i in range (4568):
  a.append(i)
actual.index=a

toyota=pd.concat([pred, actual], axis=1)

toyota

from sklearn import metrics
import sklearn.metrics as sm
print("Mean absolute error =", round(sm.mean_absolute_error(toyota.Pred, toyota.Price))) 
print("Mean squared error =", round(sm.mean_squared_error(toyota.Pred, toyota.Price)))
print("Median absolute error =", round(sm.median_absolute_error(toyota.Pred, toyota.Price))) 
print("Explain variance score =", (sm.explained_variance_score(toyota.Pred, toyota.Price)))
print("R2 score =", (sm.r2_score(toyota.Pred, toyota.Price)))

plt.figure(figsize=(500,400))
fig, ax = plt.subplots()
#ax.set_yscale('log')
#ax.set_xscale('log')
ax.plot(toyota.index,toyota['Pred'],color='blue',marker='o')
ax.plot(toyota.index,toyota['Price'], color='orange',marker='*')

pred=0
act=0
for i in range (4568):
  pred=pred+toyota.Pred[i]
  act=act+toyota.Price[i]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['Actual','Predicted']
students = [act,pred]
ax.bar(langs,students)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import random
a=random.randrange(4568)
b=random.randrange(4568)
c=random.randrange(4568)
d=random.randrange(4568)
e=random.randrange(4568)
f=random.randrange(4568)
g=random.randrange(4568)
h=random.randrange(4568)
i=random.randrange(4568)
j=random.randrange(4568)
data= [[toyota.Pred[a],toyota.Pred[b],toyota.Pred[c],toyota.Pred[d],toyota.Pred[e],toyota.Pred[f],toyota.Pred[g],toyota.Pred[h],toyota.Pred[i],toyota.Pred[j]],
     [toyota.Price[a],toyota.Price[b],toyota.Price[c],toyota.Price[d],toyota.Price[e],toyota.Price[f],toyota.Price[g],toyota.Price[h],toyota.Price[i],toyota.Price[j]]]

data

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
X=np.arange(10)
ax.bar(X + 0.00, data[0], color = 'b', width = 0.25,)
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25,)
ax.legend(labels=['Predicted', 'Actual'])
#bue predicted 
#green actual