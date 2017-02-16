import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

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

#
# TODO: Create a 2d scatter plot that graphs the
# area and perimeter features
# 
# .. your code here ..
s1 = df.loc[:,'area':'perimeter']
print('s1:')
print(s1.head())
s1.plot.scatter('area', 'perimeter' )
#
# TODO: Create a 2d scatter plot that graphs the
# groove and asymmetry features
# 
# .. your code here ..
s2 = df.loc[:,'asymmetry':'groove']
print('s2:')
print(s2.head())
s2.plot.scatter('asymmetry','groove')
#
# TODO: Create a 2d scatter plot that graphs the
# compactness and width features
# 
# .. your code here ..
s3 = df.loc[:,'compactness':'width']
print('s3:')
print(s3.head())
s3.plot.scatter('compactness','width')
#

plt.show()
# BONUS TODO:
# After completing the above, go ahead and run your program
# Check out the results, and see what happens when you add
# in the optional display parameter marker with values of
# either '^', '.', or 'o'.


plt.show()


