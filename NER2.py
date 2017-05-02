# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 13:06:27 2017

@author: Home
"""

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
 
def get_named_entities(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
             if type(i) == Tree:
                     current_chunk.append(" ".join([token for token, pos in i.leaves()]))
             elif current_chunk:
                     named_entity = " ".join(current_chunk)
                     if named_entity not in continuous_chunk:
                             continuous_chunk.append(named_entity)
                             current_chunk = []
             else:
                     continue
    return continuous_chunk
 

