import pandas as pd
from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt
''' next step principal component analysis'''
permit_info = pd.read_csv('permits_by_address.csv')

# print(permit_info.head())
# print(len(permit_info))
X=permit_info.drop('Address', axis=1)
# print(X.head())
kmeans = KMeans().fit(X)


# print(kmeans.predict(X))

permit_info['ML Cluster'] = kmeans.predict(X)
permit_info.to_csv('ml_column_permits.csv')
# print(kmeans.cluster_centers_)