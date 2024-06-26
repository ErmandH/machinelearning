import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('musteriler.csv')

x = veriler.iloc[:, 3:].values # 4 sutundan itibaren al

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters= 3, init= 'k-means++')

kmeans.fit(x)

print(kmeans.cluster_centers_)

sonuclar = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++')
    kmeans.fit(x)
    