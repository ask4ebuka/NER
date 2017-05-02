from rdflib import Graph
from rdflib import URIRef, BNode, Literal
from rdflib.namespace import RDF, FOAF,RDFS
g = Graph()
def insert(pred,sub,obj):
    subject=sub
    predicate=pred
    object = obj
    URI = URIRef("http://www.bbc.com")
    g.add((URI,RDF.type,FOAF.person))
    g.add( (URI,RDF.type,Literal(sub)) )
    g.serialize(destination='output2.rdf', format='xml')