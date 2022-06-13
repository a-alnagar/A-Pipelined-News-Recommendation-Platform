from click import group
from gensim.models import CoherenceModel
from gensim.utils import simple_preprocess
from gensim.test.utils import datapath
from nltk.stem import WordNetLemmatizer
from pprint import pprint
from nltk.corpus import stopwords
from reco_group import users_group
from gensim.matutils import cossim

import gensim.corpora as corpora
import os
import pandas as pd
import re
import gensim
import nltk
import requests
import json
#nltk.download('stopwords')

lem = WordNetLemmatizer()
stop_words = stopwords.words('english')
stop_words.extend(['knows','well', 'know','every','still', 'from', 'subject', 're', 'time','years', 'city', 'going','back', 'make', 'made', 'use', 'ms','s', "can't",'say','even','last','get', 'would', 'could', 'us','year', 'also','said', 'new','people','may', 'might', 'shall', 'should', 'first', 'like', 'many', 'much', 'mr', 'says', 'think', 'one', 'two', 'three', 'four', 'way', 'day' ])

#simulates articles input
df = pd.read_csv('/home/alnaggar/PBL/data-1653249353296.csv')
lda_model = gensim.models.LdaMulticore.load("/media/alnaggar/F47C61617C611F9A/PBL Data/lda_model.model")

def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))


def remove_stopwords(texts):
    return [[lem.lemmatize(word) for word in simple_preprocess(str(doc)) 
             if word not in stop_words] for doc in texts]


data = df.text.values.tolist()
data_words = list(sent_to_words(data))

# remove stop words
data_words = remove_stopwords(data_words)

# Create Dictionary
id2word = corpora.Dictionary(data_words)
# Create Corpus
texts = data_words
# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]
# View
print(corpus[:1][0][:30])

#a function that creates group features
def group_text(df):
    temp = ''
    group_text = []
    for x in df.group.unique():
        gd = df[df['group'] == x]
        for y in df.feature.values:
            temp = y + ' '
        
        group_text.append(temp)
        temp = ''
    
    return group_text

g = group_text(users_group)

data_g = list(sent_to_words(data))

# remove stop words
data_g = remove_stopwords(data_words)

# Create Dictionary
id2word_g = corpora.Dictionary(data_words)
# Create Corpus
texts_g = data_words
# Term Document Frequency
corpus_g = [id2word.doc2bow(text) for text in texts]

group_vecs = []
for x in corpus_g:
    group_vecs.append(lda_model.get_document_topics(x))

def generate_recommendations(df, corpus, groups):
    scores = []
    art = 0
    for x in corpus:
        art_vec = lda_model.get_document_topics(x)
        for y in group_vecs:
            score = cossim(y, art_vec)
            scores.append(score)
        max_score = max(scores)
        g_ind = scores.index(max_score)
        #send article url with group id
        print(max_score + df['url'].loc[a])
        d = {"cookieid":"", "url":""}
        d
        scores = []
        art += 1
    return

generate_recommendations(df, corpus, group_vecs)
        



            

