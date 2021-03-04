import matplotlib.pyplot as plt
import numpy as np
from time import time
import os

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

dataset = 'amazon'

if __name__ == '__main__':
    labelid = 0
    label_index = {}
    
    '''
    f = open('emb/email.emb')
    for topline in open('ground-truth/email-Eu-core-department-labels.txt'):
        [a,b] = topline.split()
        label_index[a] = b
    '''
    
    
    f = open('emb/node2vec128/'+dataset+'.subgraph.emb')
    #f = open('deepwalk_emb/'+dataset+'.subgraph2.emb')

    for topline in open('ground-truth/com-'+dataset+'.top5000.cmty.txt'):
        temp = topline.split()
        if len(temp) >= 3:
            for i in temp:
                label_index[i] = labelid
            labelid += 1
    
    '''
    while line:
        temp = line.split()
        if temp[0] in label_index:
            y_digits.append(label_index[temp[0]])
            i = []
            for x in temp[1:]:
                i.append(float(x))
            data.append(i)
            line = f.readline()
    '''

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

    #print(len(y_digits))
    data = np.array(data)
    n_samples, n_features = data.shape
    n_digits = len(np.unique(y_digits))
    labels = y_digits

    print("n_digits: %d, \t n_samples %d, \t n_features %d"
        % (n_digits, n_samples, n_features))


    print(82 * '_')
    print('init\t\ttime\tinertia\thomo\tcompl\tv-meas\tARI\tAMI\tFMI\tsilhouette')


    def bench_k_means(estimator, name, data):
        t0 = time()
        estimator.fit(data)
        print('%-9s\t%.2fs\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
            % (name, (time() - t0), estimator.inertia_,
                metrics.homogeneity_score(labels, estimator.labels_),
                metrics.completeness_score(labels, estimator.labels_),
                metrics.v_measure_score(labels, estimator.labels_),
                metrics.adjusted_rand_score(labels, estimator.labels_),
                metrics.adjusted_mutual_info_score(labels,  estimator.labels_),
                metrics.fowlkes_mallows_score(labels,estimator.labels_),
                metrics.silhouette_score(data, estimator.labels_,
                                        )))
        #print('宏平均F1-score:',metrics.f1_score(labels,estimator.labels_,average='macro'))

    bench_k_means(KMeans(init='k-means++', n_clusters=n_digits),
                name="k-means++", data=data)

    # in this case the seeding of the centers is deterministic, hence we run the
    # kmeans algorithm only once with n_init=1
    print(82 * '_')