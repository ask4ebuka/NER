#This uses Dbpedia web service
import spotlight
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from spotlight import SpotlightException
import inflect

p= inflect.engine()
ps = PorterStemmer()

def clean(triples):
    list = []

    for word in triples:
        if word is not None:
            #print(word[0])
            a = WordNetLemmatizer().lemmatize(word[0], 'v')
            a = a.replace("have"," ")
            a = a.replace("has", " ")
            a = a.replace("had", " ")
            a = a.replace("was", " ")
            a = a.replace("were", " ")
            a = ''.join([i for i in a if not i.isdigit()])
            a = ''.join([i for i in a if i not in (',')])
            a = a.lstrip()
            a = ps.stem(a)
            #print (a)
            b = WordNetLemmatizer().lemmatize(word[1], 'v')
            b = ''.join([i for i in b if not i.isdigit()])
            b = ''.join([i for i in b if i not in (',')])
            b = b.lstrip()
            #b = p.singular_noun(b)
            #print(b)
            c = WordNetLemmatizer().lemmatize(word[2], 'v')
            c = ''.join([i for i in c if not i.isdigit() ])
            c = ''.join([i for i in c if i not in (',')])
            c = c.lstrip()
            c = p.singular_noun(c)
            #print(c)
            list += [(a,b,c)]
            tup = tuple(list)

            #print (tup)
    result = dbp_parser(tup)
    return result
            # print (dbpedia(verbs)["URI"])
            # dbpedia(verbs)
           # print(type(dbpedia(verbs)))

def dbp_parser(triples):
    list = []
    for word in triples:
        if word is not None:
            # print(word[0])
            a = dbpedia(word[0])

            # print (a)
            b = dbpedia(word[1])

            # b = p.singular_noun(b)
            # print(b)
            c = dbpedia(word[2])

            # print(c)
            list += [(a, b, c)]
            tup = tuple(list)

            # print (tup)
    return tup



def dbpedia(text):
    try:

        annotations = spotlight.annotate('http://model.dbpedia-spotlight.org/en/annotate',
                                          text,
                                         confidence=0.0, support=20)
        result1=  annotations[0]
        result2 = result1['URI']
        return result2
    except SpotlightException:
        return 0
#test= (dbpedia("person"))
#print (test[0])
#a = test[0]
#print (a['URI'])
#print (clean([('have arrested', 'Police', '1,000 people'),('have arrested', 'Police', '1,000 people')]))
