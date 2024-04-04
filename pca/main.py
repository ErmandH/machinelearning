# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:28:38 2024

@author: x
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits


digits = load_digits()

before_shape = digits.data.shape # boyut sayisi 64

pca = PCA(2)

data_pca = pca.fit_transform(digits.data)
after_shape = data_pca.shape # 2 ye dustu boyut sayisi

pca = PCA().fit(digits.data)

plt.plot(np.cumsum(pca.explained_variance_ratio_))