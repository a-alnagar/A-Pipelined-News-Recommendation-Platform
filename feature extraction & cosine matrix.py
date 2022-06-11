from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import cosine_similarity
from matplotlib import pyplot as plt
from psuedo_users_creation import logs
from datetime import date

import json
import requests
import pandas as pd

#d = "http://localhost:8000/articles/20{}".format(today.strftime("%y-%m-%d"))
#req = requests.get(d)

#Get users with all the articles read
features = pd.read_csv('/media/alnaggar/F47C61617C611F9A/PBL Data/features.csv', low_memory=False)

cvec = TfidfVectorizer(stop_words = "english")

#Extract Features
count_matrix = cvec.fit_transform(features["feature"])

#Cmoputing Cosine similarity socre
cosine_sim = cosine_similarity(count_matrix)

#creating groups of similar users using hierarichal clustering
cluster = AgglomerativeClustering()

y = cluster.fit_predict(cosine_sim)

#Return a data frame with each user group
users_group = pd.DataFrame({'user':features.user_id, 'group': y, 'feature':features.feature, 'history': logs})
print(users_group)
users_group.to_csv('/media/alnaggar/F47C61617C611F9A/PBL Data/users-history.csv', index = False)

plt.scatter(x= cosine_sim[:,0], y = cosine_sim[:,1], c= y, cmap='rainbow' )
plt.show()


