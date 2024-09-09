# cython: language_level=3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
cimport numpy as cnp
import os

def load_data(str filename):
    product_descriptions = pd.read_csv(filename)
    product_descriptions = product_descriptions.dropna()
    return product_descriptions.head(500)

def vectorize_data(product_descriptions1):
    vectorizer = TfidfVectorizer(stop_words='english')
    cdef X1 = vectorizer.fit_transform(product_descriptions1["product_description"])
    return X1, vectorizer

def train_kmeans(X, int true_k=10):
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
    model.fit(X)
    return model

def print_cluster(int i, order_centroids, terms):
    d=[]
    for ind in order_centroids[i, :10]:
        d.append(terms[ind])
    return d

def show_recommendations(str product):
    cdef str filename = 'product_descriptions.csv'
    product_descriptions1 = load_data(filename)
    X1, vectorizer = vectorize_data(product_descriptions1)
    model = train_kmeans(X1)

    cdef Y = vectorizer.transform([product])
    cdef prediction = model.predict(Y)
    return print_cluster(prediction[0], model.cluster_centers_.argsort()[:, ::-1], vectorizer.get_feature_names_out())

