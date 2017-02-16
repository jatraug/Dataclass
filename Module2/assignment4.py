import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
df = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2', header=None)[0]




##print(df.dtype)

# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
# .. your code here ..
df.columns= ['RK',	'PLAYER',	'TEAM',	'GP',	'G',	'A',	'PTS',	'+/-',	'PIM',	'PTS/G',	'SOG',	'PCT',	'GWG',	'PPG',	'PPA',	'SHG',	'SHA']
#print(df)
df1 = df.drop(df.index[[0,1]])




print(df1)

# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
# .. your code here ..
df2 = df1.dropna(axis=0, thresh=4)
print(df2)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
print(df2['RK'])
#print(df2.loc['RK'])
#iris.ix[iris['sepal length (cm)'] >= 5]
df3 = df2[df2.RK != 'RK']
print(df3)

df4 = df3.drop(labels=['RK'],axis=1)
print(df4)
# TODO: Get rid of the 'RK' column
#
# .. your code here ..


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df4 = df4.reset_index()
print(df4)

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
# .. your code here ..
print (df4.dtypes)


# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
# .. your code here ..
print(df4.PCT.unique())
