import pandas as pd
import random as r

articles = pd.read_csv('/home/alnaggar/PBL/data-1653249353296.csv')
articles.columns = ['sk', 'url', 'title', 'text', 'tags', 'count', 'date', 'summary']

#print(articles.head())

#Create Hundred 100 users. Each user read 20 articles already
articles_id = articles['sk'].to_list()

#A function which assigns 20 random articles to each user

u =[]
a =[]
#a list for each user browsed articles ids
logs = []
for x in range(1, 101):
    ele = []
    for y in range(0, 20): 
        u.append(x)
        n = r.choice(tuple(articles_id))
        a.append(n)
        ele.append(n)
    
    logs.append(ele)


users = pd.DataFrame({'user_id':u, 'article_id':a})
users.to_csv('/media/alnaggar/F47C61617C611F9A/PBL Data/temp-users.csv', index = False)