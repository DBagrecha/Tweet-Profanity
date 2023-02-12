# Importing required libraries 
import pandas as pd
from nltk.tokenize import word_tokenize

# Assuming that all the tweets are in a csv file and the racial slurs are in a .txt file with every word in a new line
df = pd.read_csv('<.csv file path>')
word_list = set()
f = open('<.txt file path>','r')
for w in f:
  word_list.add(w.strip())

# Assuming that the tweets are in the the column "tweets"
# Making a new column "profanity" in DataFrame which will have the profanity values
# Calculating profanity using the formula: racial slurs / total words in tweet

arr=[]
# Looping through each tweet
for tweet in df['tweets']:
  words = 0
  for w in word_tokenize(tweet):
    if w in word_list:
      words+=1
  arr.append(words/len(tweet))

df['profanity']=arr
