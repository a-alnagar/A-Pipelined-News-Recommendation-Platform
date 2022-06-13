
import pandas as pd
import time
import nltk
import requests
import re
import torch
from multiprocessing import Process
from transformers import BartForConditionalGeneration, BartConfig, BartTokenizer

df = pd.read_csv('/home/alnaggar/PBL/data-1653249353296.csv')
news = df.copy()
news.columns = ['sk', 'url', 'title', 'text', 'tags', 'count', 'date', 'summary']

#convert the articles column to a list for summarization
#this was done to avoid using apply as it has a big running time

test = news.loc[1:8]
articles = test['text'].tolist()
nums = test['count'].tolist()
news = news.sort_values(by = ['count'])
print(test.head())

#Intilizing the BART model 
model =  BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

#intializing text tokenizer
tokenizer = BartTokenizer.from_pretrained("facebook/bart-base")


#The following piece of code summarizes the articles
#NOTE: the model accepts a maximum length of 512 words, so large articles
#are summarized iterativley

s = len(articles)

def summer(articles, nums):
  sums = []
  temp = ''
  num = 0
  count = 0
  for article in articles:
    if nums[num] <= 100:
      sums.append(article)
      num += 1
  
    else:
      while(nums[num] > 10):
          inputs = tokenizer([article[count: count +  512]], max_length = 512, return_tensors="pt")
          summary_ids = model.generate(inputs["input_ids"], num_beams=2, min_length=0, max_length=50)
          temp +=  tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
          nums[num] -= 512
          count += 512
      print(temp + '\n')
      num += 1
      count = 0
      sums.append(temp)
      temp = ''
  print(sums)
  return sums

start = time.time()

if __name__ == '__main__':
  p1 = Process(target = summer, args = (articles[0: int((s-1)/2)], nums[0 : int((s- 1)/2)]),)
  p2 = Process(target = summer, args = (articles[int((s - 1)/2):s - 1], nums[int((s - 1)/2): s - 1]),)

  p1.start()
  p2.start()

  p1.join()
  p2.join()

newspaper = {'nytimes':'new york times', 'washingtonpost':'washington post', 'theguardian':'the guardian'}


end = time.time()
#This function creates a sperate column contains the website name
def paper(df):
  col = df['url'].lower()
  for k in newspaper.keys():
    n = re.search(k, col)
    if n != None:
      return re.sub(col,newspaper[k], col)

#This fucntion cleans the title from non-alphanumeric characters and removes
#the website name from the title
def cleaner(df):
  col = df['title'].lower()
  for k in newspaper:
    if k in col:
      col = col - k
  return ''.join(char for char in col if char.isalnum() or char == ' ')


def text_cleaner(df):
  c = df['text'].lower()
  #remove words between brackets
  c = re.sub("[\(\[].*?[\)\]]", '', c)
  #remove all special characters and numbers from main text
  return str(''.join(char for char in c if char.isalpha() or char == ' '))


#Create a paper column
news['paper'] = news.apply(paper, axis = 1)

#Clean title column
news['title_new'] = news.apply(cleaner, axis = 1)
news['title'] = news['title_new']
news = news.drop(['title_new'], axis = 1)

print(end)