#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import andrews_curves

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
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# Also get rid of the 'area' and 'perimeter' features
# 
# .. your code here ..
df = df.drop('id', 1)
#df = df.drop('area', 1)
#df = df.drop('perimeter', 1)

print(df.head())

#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..
#df['target_names'] = list(df) ##['compactness', 'length', 'width', 'asymmetry', 'groove', 'wheat_type']
plt.figure()
print(list(df))
#df['target_names'] =   list(df)
andrews_curves(df, 'wheat_type', alpha=0.4)



plt.show()


