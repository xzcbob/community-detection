from sklearn.cluster import OPTICS, cluster_optics_dbscan
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from time import time
from sklearn import metrics

dataset = 'amazon'
labelid = 0
label_index = {}
# #############################################################################
# Generate data
'''
#f = open('deepwalk_emb/'+dataset+'.subgraph2.emb')
f = open('node2vec_emb/'+dataset+'.subgraph.emb')

for topline in open('ground-truth/com-'+dataset+'.top5000.cmty.txt'):
    temp = topline.split()
    for i in temp:
        label_index[i] = labelid
    labelid += 1

'''
f = open('deepwalk_emb/email.emb')
for topline in open('ground-truth/email-Eu-core-department-labels.txt'):
    [a,b] = topline.split()
    label_index[a] = b


y_digits = []
line = f.readline()
line = f.readline()
data = []
while line:
    temp = line.split()
    y_digits.append(label_index[temp[0]])
    i = []
    for x in temp[1:]:
        i.append(float(x))
    data.append(i)
    line = f.readline()

X = np.array(data)
labels_true = np.array(y_digits)

# #############################################################################
# Compute DBSCAN
t0 = time()
db = OPTICS(min_samples=2).fit(X)

labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Fowlkes and Mallows Index: %0.3f"
      % metrics.fowlkes_mallows_score(labels_true,labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))
#print('宏平均F1-score:',metrics.f1_score(labels_true,labels,average='macro'))
print("Time: %0.3f" % (time()-t0))