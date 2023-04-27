# -*- coding: utf-8 -*-
"""Customer Segmentation using K-Means Clustering of supermarket.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L9JMyZj8Qzh_XFOHvQitTzmEdHfq7PQ7

**Importing the Dependent Libraries**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt       #matplotlib and seaborn used for plotting i.e data visualisation libraries
import seaborn as sns
from sklearn.cluster import KMeans   #Kmeans is clsutering algo

"""**Data Collection & pre processing analysis**"""

# loading the data from csv file to a pandas DataFrame
customer_data = pd.read_csv('/content/Supermart_Customers.csv')

# Looking first 5 rows for details
customer_data.head(5)

# finding the total no  of rows and columns
customer_data.shape

# checking for missing values
customer_data.isnull()

#summation of all null values per column
customer_data.isnull().sum()

"""**Choosing the required Annual Income Column & Spending Score column**"""

Z = customer_data.iloc[:,[3,4]].values    #iloc i used to take 3rd and 4th index values from customer data and assigned to z

print(Z)

"""**Choosing the number of clusters**

WCSS -> Within Clusters Sum of Squares # used to find optimum no of clsuter
"""

# finding wcss value for different number of clusters

wcss = []   #intialisation of list

for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)  # random state mean splitting values
  kmeans.fit(Z)

  wcss.append(kmeans.inertia_)    #inertia lies in KMeans and give kcss values for each clsuter an append in list

# plotted  an elbow graph or cut off point graph

sns.set()
plt.plot(range(1,11), wcss)
plt.title('The Elbow Point Graph')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

"""Here we got 2 drop 1st at 3 and 2nd at 5 we will choose 5 at after that there is no significant drop in graph

*Optimum Number of Clusters = 5*

**Training the k-Means Clustering Model**
"""

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=0)

# return a label for each data point based on their cluster number
Y = kmeans.fit_predict(Z)

print(Y)

"""5 Clusters we got  - 0, 1, 2, 3, 4

**Visualizing all the Clusters**
"""

# plotting all the clusters and their Centroids here in color cyan

plt.figure(figsize=(8,8))
plt.scatter(Z[Y==0,0], Z[Y==0,1], s=50, c='grey', label='Cluster 1')
plt.scatter(Z[Y==1,0], Z[Y==1,1], s=50, c='yellow', label='Cluster 2')
plt.scatter(Z[Y==2,0], Z[Y==2,1], s=50, c='blue', label='Cluster 3')
plt.scatter(Z[Y==3,0], Z[Y==3,1], s=50, c='orange', label='Cluster 4')
plt.scatter(Z[Y==4,0], Z[Y==4,1], s=50, c='brown', label='Cluster 5')

#here s =size of dot , c means color  and x axis --Z[Y=0,0]--means 0 -1st clsuter and 0-income column index in Z
# and y axis --Z[Y==0,1] --means 0 -1st clsuter and 1 --spending column index in z


# plot the centroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='cyan', label='Centroids')
#[:,0] -- means x axis of centroid and [:,1] means y axis of centroid
plt.title('Customer Groups')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()

"""Conclusion
We have created a customersegmentaion machine learning model based on k- means clsutering method which can suggest the customers spending habits with income  .
Also we have trained our model with data set having 200 rows and 5 columns i.e featured.
We did data cleaning and pre processing

From avoid model we can give offers / membership / discount to customers whose income in more and they are spending less i.e grey color cluster 1.
we can analysis customer behavior and can make our business profitable
"""