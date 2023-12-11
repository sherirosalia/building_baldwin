'''NOTES: next steps... putting in addresses in, measuring tightness of clusters, cluster centers into 3d graph to help make sense of PCA, maybe put back in random state parameter'''
'''third script'''
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
# from matplotlib import colormaps
# import matplotlib.pyplot as plt
''' next step principal component analysis'''
permit_info = pd.read_csv('permits_by_address.csv')

# print(permit_info.head())
# print(len(permit_info))



X=permit_info.drop('Address', axis=1)
# print(X.columns.to_list())
column_names = X.columns.to_list()
print(column_names)
# print(X.head())
'''pca component in this case is grouping related data and attempting to keep the distance between them the same'''
pca = PCA(n_components=3, random_state=0)
data_2_d = pca.fit_transform(X)
x_2d=[point[0] for point in data_2_d]
y_2d=[point[1] for point in data_2_d]
z_2d=[point[2] for point in data_2_d]
# plt.scatter(x_2d, y_2d, marker="o", color="red")
# plt.show()
# print(pca.fit_transform(X))
# print('pca components:::::::')
# print(pca.components_)

# print(pca.explained_variance_ratio_)
'''kmeans is just trying to find 8 groups of groups. kmeans creates the clusters'''
# kmeans = KMeans(random_state=0).fit(X)
kmeans = KMeans(n_clusters=20).fit(X)

# print(kmeans.predict(X))

# permit_info['ML Cluster'] = kmeans.predict(X)
''' using color in plot below to illustrate clusters'''
cluster = kmeans.predict(X)
# print('kmeans cluster::::::')
# print(kmeans.cluster_centers_)

for cluster_i, cluster_data in enumerate(kmeans.cluster_centers_):
    print(f'cluster index: {cluster_i}')
    for permit_i, permit_importance in enumerate(cluster_data):
        column_names[permit_i]
        if permit_importance > 0.5:
            print(f'permit index {column_names[permit_i]} permit importance: {permit_importance}')

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')
'''using accent for cmap below to create distinct colors for qualitative data which in essence is what our clusters are. not used, things like light, medum and dark green might appear in the char which makes it difficult for the viewer to be clear as to whether or not greens  are more relational than lets say for example purple. (not to mention discerning the differnce between greens in this example. )'''
ax.scatter(x_2d, y_2d, z_2d, c=cluster, marker="o",cmap="Accent")

fig.savefig('3d_cluster.png')
# plt.show()

# permit_info.to_csv('ml_column_permits.csv')
# print(kmeans.cluster_centers_)