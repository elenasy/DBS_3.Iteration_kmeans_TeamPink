import csv
import numpy as np
from scipy.cluster.vq import kmeans, kmeans2, whiten
import matplotlib.pyplot as plt

#read .csv file into a list 
#Each element of this list is one row in the csv file

with open('hashtagTime.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    hashtag_list = []
    for row in reader:
        #print ', '.join(row)
        print row
        hashtag_list.append(row)



#Extract the epoch time and put them into a list for K-means clustering.

data = np.ndarray(shape=(len(hashtag_list),1), dtype=float, order='F')
for i in range(len(hashtag_list)):
    data[i] = hashtag_list[i][1]

print data



#Use k-means algorithm with given number of cluster centers

centers,idx = kmeans2(data,10)
print centers


#Plot

zz = np.zeros((len(hashtag_list),1))
nn = np.ones((len(centers),1))
plt.figure(figsize=(10, 6), dpi=100)
plt.scatter(data, zz, c=idx, s=20)
plt.scatter(centers[:,0], nn, marker='v', s=80)
plt.show()
