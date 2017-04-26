# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:13:13 2017

@author: Home
"""
from rdflib import Graph
from rdflib import URIRef, BNode, Literal
from rdflib.namespace import RDF, FOAF
 
#g = Graph()

#bob = URIRef("http://example.org/people/Bob")
linda = BNode() # a GUID is generated

#name = Literal('Bob') # passing a string
#age = Literal(24) # passing a python int
#height = Literal(76.5) # passing a python float
#             
g.add( (bob, RDF.type, FOAF.Person) )
g.add( (bob, RDF.type, name) )
g.add( (bob, FOAF.knows, linda) )
g.add( (linda, RDF.type, FOAF.Person) )
g.add( (linda, RDF.type, Literal('Linda') ) )

print (g.serialize(format='turtle'))