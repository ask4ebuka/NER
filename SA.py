# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 13:18:30 2017

@author: Home
"""
from textblob import TextBlob
def get_sentiment(text):
    blob = TextBlob(text)
    blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                        #  ('threat', 'NN'), ('of', 'IN'), ...]

    blob.noun_phrases   # WordList(['titular threat', 'blob',
                        #            'ultimate movie monster',
                        #            'amoeba-like mass', ...])

    for sentence in blob.sentences:
        return (sentence.sentiment.polarity)

