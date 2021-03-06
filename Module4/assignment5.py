import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import os
import numpy as np
# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')

colors = []

#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
samples = []

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 

##from scipy import misc
path = 'Datasets/ALOI/32'
files = os.listdir(path)
for i in range(len(files)):
  print(files[i])
  img = misc.imread(path + '/' + files[i])

  #  img = img.reshape(-1)
  samples.append(  (img[::2, ::2] / 255.0).reshape(-1)  )
  #  samples.append([img[0]])
  colors.append('b')

path = 'Datasets/ALOI/32i'
files = os.listdir(path)
for i in range(len(files)):
  print(files[i])
  img = misc.imread(path + '/' + files[i])

  #  img = img.reshape(-1)
  samples.append(  (img[::2, ::2] / 255.0).reshape(-1)  )
  colors.append('r')
print('img')
print(img)
print(len(samples))
#ar = np.array[img]
#img = img.[:,0:145]
print('img.shape')
print(img.shape)
#print(samples)

#
#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 
#samples = map(float, samples)
##s2 = [float(i) for i in samples]
#samples = np.array(samples) + 0.
#print(samples.dtypes())

#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 

df = pd.DataFrame(samples)
print(df.describe())
print('df')
print(df)
print('shape')
print(df.loc[0].shape)
#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 
#df=df.convert_objects(convert_numeric='force')
#df = df.fillna(0)

#ar= np.array(df.loc[0]) ##,dtype=dtype, order=order, copy=copy)
#stohere
print ('df.loc[0]')
print (df.loc[0])
from sklearn import manifold
tmp = manifold.Isomap(n_neighbors=6, n_components=3, neighbors_algorithm='auto', path_method='auto', tol=0)
iso = tmp.fit_transform(df) ##.loc[1,:]
print(iso.shape)


#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 

#iso.plot.scatter(x='component1', y='component2', marker='o', c=labels, alpha=0.75, ax=ax)
plt.scatter(iso[:,0], iso[:,1], marker = 'o', c=colors)


#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(iso[:,0], iso[:,1], iso[:,2], c=colors)
ax.set_xlabel('area')
ax.set_ylabel('perimeter')
ax.set_zlabel('asymmetry')

plt.show()

