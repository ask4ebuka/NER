from rdflib import Graph
from rdflib import URIRef, BNode, Literal
from rdflib.namespace import RDF, FOAF,RDFS,OWL
from rdflib import Namespace

#dbpedia = Namespace("http://dbpedia.org/ontology/")
dbp = Namespace ("http://dbpedia.org/resource/") #namespace declaration
news = Namespace ("http://news.com/")
g = Graph()     #graph initiailized
def sem_graph(triples):
    count =0
    for res in triples:
        news = URIRef("http://news.com/new"+str(count))
        if res[0]  == 0:    #0 is returned if entity not found in dbpedia
            pred = BNode()   #predicate = blank node
        else:
            pred = URIRef(res[0]) #predicate = dbpedia resource
        if res[1] == 0:   #0 is returned if entity not found in dbpedia
            sub = BNode()   #subject = blank node
        else:
            sub = URIRef(res[1]) #subject = dbpedia resource
        if res[0] == 0:    #0 is returned if entity not found in dbpedia
            obj = BNode()  #object = blank node
        else:
            obj = URIRef(res[2]) #object = dbpedia resource
       
        #graph generation
        g.add((sub,pred,obj))
        g.add((news,RDF.subject,sub))
        g.add((news,RDF.predicate,pred))
        g.add((news,RDF.object,obj))
        g.add((sub,RDF.type,news))
        g.add((pred,RDF.type,news))
        g.add((obj,RDF.type,news))
        #g.add((news.news1,dbp.sentiment,Literal("0.34")))
        # g.add((URIRef(res[1]),RDFS.label,Literal(res[4])))
        # g.add((URIRef(res[0]),RDFS.label,Literal(res[3])))
        # g.add((URIRef(res[2]),RDFS.label,Literal(res[5])))
        count +=1;
    g.serialize(destination='output.rdf', format='xml') #graph output and format












# from rdflib import Graph
# from rdflib import resRef, BNode, Literal
# from rdflib.namespace import RDF, FOAF,RDFS,OWL
# g = Graph()
# def insert(pred,sub,obj):
#     subject=sub
#     predicate=pred
#     object = obj
#     res = resRef("http://www.bbc.com")
#     g.add((res,RDF.type,FOAF.person))
#     g.add( (res,RDF.type,Literal(sub)) )
#     g.serialize(destination='output2.rdf', format='xml')

# from rdflib import Graph
# from rdflib import resRef, BNode, Literal
# from rdflib.namespace import RDF, FOAF,RDFS,OWL
# from rdflib import Namespace
# dpb = Namespace("http://www.dbpedia.org/ontology/")
# dc = Namespace("http://purl.org/dc/elements/1.1/")
# ex = Namespace("http://www.exmp.com/ontology/")
# g = Graph()
#
#    # res = resRef("http://www.bbc.com")
# g.add((ex.Cricket,RDF.resource,ex.Gryllidae))
# g.add ((ex.Gryllidae,RDFS.subClassOf,dpb.insect))
# g.add ((ex.Gryllidae,ex.has_body_part,Literal("head")))
# g.add ((ex.Gryllidae,ex.has_body_part,Literal("Antennae")))
# g.serialize(destination='output3.rdf', format='xml')

# from rdflib import Graph
# from rdflib import resRef, BNode, Literal
# from rdflib.namespace import RDF, FOAF,RDFS,OWL
# from rdflib import Namespace
# 
# dbpedia = Namespace("http://dbpedia.org/ontology/")
# dbp = Namespace ("http://dbpedia.org/resource/")
# news = Namespace ("http://news.com/")
# g = Graph()
# 
# g.add((URIRef(res[1]),URIRef(res[0]),URIRef(res[2])))
# g.add((news.news1,RDF.subject,URIRef(res[1])))
# g.add((news.news1,RDF.predicate,URIRef(res[0])))
# g.add((news.news1,RDF.object,URIRef(res[2])))
# g.add((URIRef(res[1]),RDF.type,news.news1))
# g.add((URIRef(res[0]),RDF.type,news.news1))
# g.add((URIRef(res[2]),RDF.type,news.news1))
# g.add((news.news1,dbp.sentiment,Literal("0.34")))
# g.add((URIRef(res[1]),RDFS.label,Literal("Police")))
# g.add((URIRef(res[0]),RDFS.label,Literal("has arrested")))
# g.add((URIRef(res[2]),RDFS.label,Literal("terrorist")))
# g.add((news.news1,URIRef(res[1]),Literal("Police")))
# g.add((news.news1,URIRef(res[0]),Literal("has arrested")))
# g.add((news.news1,URIRef(res[2]),Literal("terrorist")))
# g.add((news.news1,RDF.subject,Literal("Police")))
# g.add((news.news1,RDF.predicate,Literal("has arrested")))
# g.add((news.news1,RDF.object,Literal("terrorist")))
# g.serialize(destination='output4.rdf', format='xml')