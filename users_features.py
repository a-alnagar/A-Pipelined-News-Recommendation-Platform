import pandas as pd

users = pd.read_csv('/media/alnaggar/F47C61617C611F9A/PBL Data/users.csv', low_memory= False)
articles = pd.read_csv('/home/alnaggar/PBL/data-1653249353296.csv')
articles.columns = ['sk', 'url', 'title', 'text', 'tags', 'count', 'date', 'summary']

u  = users.groupby('user_id')

#Create a string contains all the user's articles to extract features
features = []
for x in range(1, 101):
    temp = ''
    y = 0
    a = u.get_group(x)
    for c in a['article_id']:
        if y < 20:    
            temp += str(articles.loc[articles.sk == c , 'text'].values[0]) + ' '
            y += 1
    features.append(temp)
    
#Extract Features to a dataframe
features_table = pd.DataFrame({'user_id':[x for x in range(1, 101)], 'feature':features})
features_table.to_csv('/media/alnaggar/F47C61617C611F9A/PBL Data/features.csv', index = False)

        