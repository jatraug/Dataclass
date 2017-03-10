import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.style.use('ggplot') # Look Pretty

#
# INFO: This dataset has call records for 10 users tracked over the course of 3 years.
# Your job is to find out where the users likely live at!


def showandtell(title=None):
  if title != None: plt.savefig(title + ".png", bbox_inches='tight', dpi=300)
  plt.show()
  # exit()

def clusterInfo(model):
  print "Cluster Analysis Inertia: ", model.inertia_
  print '------------------------------------------'
  for i in range(len(model.cluster_centers_)):
    print "\n  Cluster ", i
    print "    Centroid ", model.cluster_centers_[i]
    print "    #Samples ", (model.labels_==i).sum() # NumPy Power

# Find the cluster with the least # attached nodes
def clusterWithFewestSamples(model):
  # Ensure there's at least on cluster...
  minSamples = len(model.labels_)
  minCluster = 0
  for i in range(len(model.cluster_centers_)):
    if minSamples > (model.labels_==i).sum():
      minCluster = i
      minSamples = (model.labels_==i).sum()
  print "\n  Cluster With Fewest Samples: ", minCluster
  return (model.labels_==minCluster)

def clusterWithMostSamples(model):   
 maxCluster = 0   
 maxSamples = (model.labels_==0).sum()  
 for i in range(len(model.cluster_centers_)):
     if maxSamples < (model.labels_==i).sum():
       maxCluster = i
       maxSamples = (model.labels_==i).sum()   
 print "\n  Cluster With Most Samples: ", maxCluster   
 return (model.labels_==maxCluster)

def doKMeans(data, clusters=0):
  import sklearn
  from sklearn.cluster import KMeans

  #
  # TODO: Be sure to only feed in Lat and Lon coordinates to the KMeans algo, since none of the other
  # data is suitable for your purposes. Since both Lat and Lon are (approximately) on the same scale,
  # no feature scaling is required. Print out the centroid locations and add them onto your scatter
  # plot. Use a distinguishable marker and color.
  #
  # Hint: Make sure you fit ONLY the coordinates, and in the CORRECT order (lat first). This is part
  # of your domain expertise. Also, *YOU* need to instantiate (and return) the variable named `model`
  # here, which will be a SKLearn K-Means model for this to work.
  #
  # .. your code here ..
  data = [data['TowerLon'], data['TowerLat']]
  data = np.array(data)
  data = np.transpose(data)
  model = KMeans(n_clusters=clusters, random_state=0).fit(data)
  return model



#
# TODO: Load up the dataset and take a peek at its head and dtypes.
# Convert the date using pd.to_datetime, and the time using pd.to_timedelta
#
# .. your code here ..

df = pd.read_csv('Datasets/CDR.csv' )
#print (df.head())
#print df.describe()
#print df.dtypes

df['CallDate'] = pd.to_datetime(df.loc[:, 'CallDate'])
df['CallTime'] = pd.to_timedelta(df.loc[:, 'CallTime'])

#print df.dtypes#



#
# TODO: Create a unique list of of the phone-number values (users) stored in the
# "In" column of the dataset, and save it to a variable called `unique_numbers`.
# Manually check through unique_numbers to ensure the order the numbers appear is
# the same order they appear (uniquely) in your dataset:
#




# .. your code here ..

uninums = df['In'].unique()
print uninums
#stophere
#
# INFO: The locations map above should be too "busy" to really wrap your head around. This
# is where domain expertise comes into play. Your intuition tells you that people are likely
# to behave differently on weekends:
#
# On Weekdays:
#   1. People probably don't go into work
#   2. They probably sleep in late on Saturday
#   3. They probably run a bunch of random errands, since they couldn't during the week
#   4. They should be home, at least during the very late hours, e.g. 1-4 AM
#
# On Weekdays:
#   1. People probably are at work during normal working hours
#   2. They probably are at home in the early morning and during the late night
#   3. They probably spend time commuting between work and home everyday




print "\n\nExamining person: ", 0
# 
# TODO: Create a slice called user1 that filters to only include dataset records where the
# "In" feature (user phone number) is equal to the first number on your unique list above
#
# .. your code here ..
#3688089071  96.87, 32.81] 
# 1559410755] 96.93, 32.69 
#2894365987] 96,89, 32.72 XXX
#2068627935 96.83, 32.72
#4638472273 96.909, 32.900
user1 = df[df['In'] == df.loc[0,'In']]


#
# TODO: Alter your slice so that it includes only Weekday (Mon-Fri) values.
#
# .. your code here ..
user1 =  user1[user1.DOW == ('Mon'or 'Tue' or 'Wed' or 'Thu' or 'Fri')]
print user1
print 'TowerLat == 32.90020978'
###print user1[user1['TowerLat' == df.loc[0,'In']]] # == 32.90020978]
#df[df['In'] == df.loc[0,'In']]
#
# TODO: The idea is that the call was placed before 5pm. From Midnight-730a, the user is
# probably sleeping and won't call / wake up to take a call. There should be a brief time
# in the morning during their commute to work, then they'll spend the entire day at work.
# So the assumption is that most of the time is spent either at work, or in 2nd, at home.
#
# .. your code here ..
u1 =  user1[user1.CallTime > '05:30:00']
u2 =  user1[user1.CallTime < '17:00:00']
user1 = pd.concat([u1, u2])
#
# TODO: Plot the Cell Towers the user connected to
#
# .. your code here ..
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(user1.TowerLon,user1.TowerLat, c='g', marker='o', alpha=0.2)
ax.set_title('Weekeday Calls (> 5:30 to 17:00)')

usertst = df[df.In == 3688089071] # 1559410755]  #2894365987]
print '&&&&&&&usertst[TowerLat]'
print usertst['TowerLat'].unique()
#
# INFO: Run K-Means with K=3 or K=4. There really should only be a two areas of concentration. If you
# notice multiple areas that are "hot" (multiple areas the usr spends a lot of time at that are FAR
# apart from one another), then increase K=5, with the goal being that all centroids except two will
# sweep up the annoying outliers and not-home, not-work travel occasions. the other two will zero in
# on the user's approximate home location and work locations. Or rather the location of the cell
# tower closest to them.....
model = doKMeans(user1, 3)
centroids = model.cluster_centers_
ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
clusterInfo(model)
showandtell()
clusterWithMostSamples(model)
#
# INFO: Print out the mean CallTime value for the samples belonging to the cluster with the LEAST
# samples attached to it. If our logic is correct, the cluster with the MOST samples will be work.
# The cluster with the 2nd most samples will be home. And the K=3 cluster with the least samples
# should be somewhere in between the two. What time, on average, is the user in between home and
# work, between the midnight and 5pm?
midWayClusterIndices = clusterWithFewestSamples(model)
midWaySamples = user1[midWayClusterIndices]
print "    Its Waypoint Time: ", midWaySamples.CallTime.mean()
print midWaySamples.CallTime

#
# Let's visualize the results!
# First draw the X's for the clusters:
ax.scatter(model.cluster_centers_[:,1], model.cluster_centers_[:,0], s=169, c='r', marker='x', alpha=0.8, linewidths=2)
#
# Then save the results:
#showandtell('Weekday Calls Centroids')  # Comment this line out when you're ready to proceed


## -96.90930273, 32.90020978 most samples
## -96.70959385, 32.7339405 2ns
