# %%
# ! Decision Tree
# import libraries

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# %%
# ! 2. Data Analysis and Visualization

# Data obtained from kaggle 'Spotify Dataset 1921-2020, 160k+ Tracks' by Yamac Eren AY

# https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-1921-2020-160k-tracks

df = pd.read_csv("data.csv")

col = ["danceability", "energy", "liveness", "loudness", "tempo"]

X = df[col]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, init="k-means++", n_init=10)

y_kmeans = kmeans.fit_predict(X_scaled)

df["cluster"] = y_kmeans
