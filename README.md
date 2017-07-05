# DBS_3.Iteration_kmeans_TeamPink
import csv
import numpy as np
from scipy.cluster.vq import kmeans, kmeans2, whiten
import matplotlib.pyplot as plt

with open('hashtagTime.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    hashtag_list = []
    for row in reader:
        #print ', '.join(row)
        print row
        hashtag_list.append(row)

data = np.ndarray(shape=(len(hashtag_list),1), dtype=float, order='F')
for i in range(len(hashtag_list)):
    data[i] = hashtag_list[i][1]

#print data

#use k-means algorithm with given number of cluster centers
centers,idx = kmeans2(data,10)
print centers

zz = np.zeros((len(hashtag_list),1))
nn = np.ones((len(centers),1))
plt.figure(figsize=(10, 6), dpi=100)
plt.scatter(data, zz, c=idx, s=100)
plt.scatter(centers[:,0], nn, c='c', s=100)
plt.show()
