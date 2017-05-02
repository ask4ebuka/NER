# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:13:13 2017

@author: Home
"""
from rdflib import Graph
from rdflib import URIRef, BNode, Literal
from rdflib.namespace import RDF, FOAF

g = Graph()

#bbc = URIRef("http://www.bbc.co.uk/news/0")
#linda = BNode() # a GUID is generated

# g.add( (bbc, RDF.type, FOAF.Person) )
# g.add( (bbc, RDF.type, Literal('bbc') ))
# g.add( (bbc, FOAF.knows, linda) )
# g.add( (linda, RDF.type, FOAF.Person) )
# g.add( (linda, RDF.type, Literal('Linda') ) )
# g.serialize(destination='output.rdf', format='xml')
def output_rdf():
    g.serialize(destination='output.rdf', format='xml')

def add_triple(uri, type, value):
        g.add(uri, type, value)