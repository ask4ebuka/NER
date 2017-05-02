from NER2 import get_named_entities
from SA import get_sentiment
from code_gensim import get_topic_model
from soie import get_all_relations
from soie import get_relation
from InsertRDF import insert
import multiprocessing as mp
from nltk.stem.wordnet import WordNetLemmatizer
from testDBpeadia import dbpedia
import json

news= "Police have arrested 1,000 people suspected of being part of a movement blamed for the failed 2016 coup. Another 2,200 were being sought as authorities targeted what they said was a secret structure within Turkey's police force. Turkey says a movement loyal to US-based Islamic cleric Fethullah Gulen organised the July 2016 plot to bring down President Recep Tayyip Erdogan. Earlier this month the president won a referendum on boosting his powers. As a result of the narrow victory Mr Erdogan can become head of the executive, beefing up the largely ceremonial role of Turkey's president."
#print (get_named_entities(news))
#print (get_sentiment(news))
#print (get_topic_model(news))
##print (get_all_relations(news))
d= get_all_relations(news)
#get_relation(news)
#print (get_relation(news))
#print (type(get_all_relations(news)))

#insert("have arrested","police","1000 people")

for a in d :
    if a is not None:
        #print(a[0])
        verbs=WordNetLemmatizer().lemmatize(a[1],'v')
        #print (dbpedia(verbs)["URI"])
        #dbpedia(verbs)
        print (type(dbpedia(verbs)))