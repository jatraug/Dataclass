import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..

df = pd.read_csv('Datasets/wheat.data', sep=',')
print(df.head())

fig = plt.figure()
ax = Axes3D(fig)
print('area')
print(df.loc[:,'area'])


#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
# .. your code here ..

ax.scatter(df.loc[:,'area'], df.loc[:,'perimeter'], df.loc[:,'asymmetry'], c='red')
ax.set_xlabel('area')
ax.set_ylabel('perimeter')
ax.set_zlabel('asymmetry')


fig = plt.figure()
ax2 = Axes3D(fig)
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
# .. your code here ..
ax2.scatter(df.loc[:,'width'], df.loc[:,'groove'], df.loc[:,'length'], c='green')
ax2.set_xlabel('width')
ax2.set_ylabel('groove')
ax2.set_zlabel('length')


plt.show()


