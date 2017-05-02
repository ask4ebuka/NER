import nltk
from nltk.tokenize import sent_tokenize
from pycorenlp import *
import collections
nlp=StanfordCoreNLP("http://localhost:9000/")
value =[]


def get_all_relations(text):
    sent_tokenize_list = sent_tokenize(text)
    for sentence in sent_tokenize_list:
        relationSent =get_relation(sentence)
        value.append(relationSent)
    return value
def get_relation(text):
    output = nlp.annotate(text, properties={"annotators": "tokenize,ssplit,pos,lemma,depparse,relation,natlog,openie",
                                            "outputFormat": "json",
                                            "openie.triple.strict": "true"})
    # output = nlp.annotate(text, properties={"annotators":"tokenize,ssplit,pos,depparse,natlog,openie",
    #                                 "outputFormat": "json",
    #                                  "openie.triple.strict":"true"})
    result = [output["sentences"][0]["openie"] for item in output]
    #print (result)
    for i in result:
        for rel in i:
            if rel is not None:
                relationSent=rel['relation'],rel['subject'],rel['object']
            #print(relationSent)
                return relationSent