# -*- coding: utf-8 -*-

from rdflib import Graph
import hydra.tpf # ensures that the TPFStore plugin is registered
import time, sys

def print_sparql_result(res):    
    for i in res:
        print (i)
    
def data(URL, query):
    g = Graph('TPFStore')    
    g.open(URL)
    print ('Total records - ', len(g))
    results = g.query(query)
    return results


query = "SELECT * WHERE {?s ?p ?o}"
query = "SELECT ?o WHERE {?s <http://www.w3.org/ns/lemon/ontolex#writtenRep> ?o FILTER (lang(?o) = 'ru')}"

if len(sys.argv) > 1:
        query = sys.argv[1]
        
URL = 'http://172.17.4.101:3001/click'
if len(sys.argv) > 2:
        URL = sys.argv[2]
start = time.monotonic()
res = data(URL, query)
#print ('len', len(res))
res_time = time.monotonic() - start
print("Program time (click): {:>.3f}".format(res_time) + " seconds.")

URL = 'http://172.17.4.101:3001/hdt'
if len(sys.argv) > 3:
        URL = sys.argv[3]
start = time.monotonic()
res = data(URL, query)
res_time = time.monotonic() - start
print("Program time (HDT): {:>.3f}".format(res_time) + " seconds.")
