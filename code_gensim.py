# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:10:31 2017

@author: Home
"""
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
# Importing Gensim
import gensim
from gensim import corpora

#doc1 = "Police have arrested 1,000 people suspected of being part of a movement blamed for the failed 2016 coup. Another 2,200 were being sought as authorities targeted what they said was a secret structure within Turkey's police force.Turkey says a movement loyal to US-based Islamic cleric Fethullah Gulen organised the July 2016 plot to bring down President Recep Tayyip Erdogan.Earlier this month the president won a referendum on boosting his powers.As a result of the narrow victory Mr Erdogan can become head of the executive, beefing up the largely ceremonial role of Turkey's president."

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

# compile documents
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

def get_topic_model(doc1):
    doc_complete = [doc1]

    doc_clean = [clean(doc).split() for doc in doc_complete]

    # Creating the term dictionary of our courpus, where every unique term is assigned an index. dictionary = corpora.Dictionary(doc_clean)
    dictionary = corpora.Dictionary(doc_clean)
    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

    # Creating the object for LDA model using gensim library
    Lda = gensim.models.ldamodel.LdaModel

    # Running and Trainign LDA model on the document term matrix.
    ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

    return (ldamodel.print_topics(num_topics=3, num_words=3))

