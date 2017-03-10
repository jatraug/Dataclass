import pandas as pd
import matplotlib.pyplot as plt


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
# 
# .. your code here ..
df = df.drop('id', 1)

#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
cf = df.corr()
print(cf)
#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
plt.matshow(cf)

plt.show()


