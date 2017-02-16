import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
df = pd.read_csv('Datasets/servo.data', sep=',', names=['motor', 'screw', 'pgain', 'vgain', 'class'])


print(df)
# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
sl=df.loc[df.vgain == 5]
print(sl)
print('vgain == 5')
print(len(sl.index))

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
sl2 = df.loc[df.screw == 'E'].loc[df.motor == 'E'] ## and df.screw == 'E']

print(sl2)
print('motor + screw == E')
print(len(sl2.index))

# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..

sl3 = df.loc[df.pgain == 4]
print('vgain mean for pgain == 4')
print( sl3.vgain.mean())

# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!



print(df.dtypes)
