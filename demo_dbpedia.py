import requests
from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON, N3
from pprint import pprint

sparql = SPARQLWrapper('https://dbpedia.org/sparql')
sparql.setQuery('''
    SELECT ?object
    WHERE { dbr:Barack_Obama rdfs:label ?object .}
    # WHERE { dbr:Barack_Obama dbo:abstract ?object .}
''')
sparql.setReturnFormat(JSON)
qres = sparql.query().convert()

# pprint(qres)
for result in qres['results']['bindings']:
    # print(result['object'])

    lang, value = result['object']['xml:lang'], result['object']['value']
    print(f'Lang: {lang}\tValue: {value}')
    # if lang == 'en':
    # print(value)

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery('''
CONSTRUCT { dbc:Machine_learning skos:broader ?parent .
            dbc:Machine_learning skos:narrower ?child .} 
WHERE {
    { dbc:Machine_learning skos:broader ?parent . }
UNION
    { ?child skos:broader dbc:Machine_learning . }
}''')

sparql.setReturnFormat(N3)
qres = sparql.query().convert()

g = Graph()
g.parse(data=qres, format='n3')
print(g.serialize(format='ttl').decode('u8'))


sparql = SPARQLWrapper('https://dbpedia.org/sparql')

instruments = ['Nadaswaram', 'Trombone', 'Air_horn', 'Kazoo', 'Mandolin',
               'Clavichord', 'Kaval', 'Electronic_keyboard', 'Choghur', 'Zill']

for instrument in instruments:
    print('###########################################')
    sparql.setQuery(f'''
    SELECT ?name ?comment ?image
    WHERE {{ dbr:{instrument} rdfs:label ?name.
             dbr:{instrument} rdfs:comment ?comment.
             dbr:{instrument} dbo:thumbnail ?image.
    
        FILTER (lang(?name) = 'en')
        FILTER (lang(?comment) = 'en')
    }}''')

    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()

    result = qres['results']['bindings'][0]
    name, comment, image_url = result['name']['value'], result['comment']['value'], result['image']['value']

    print(name)
    print(image_url)
    response = requests.get(image_url)
    # display(Image.open(BytesIO(response.content)))
    print(f'{comment}...')
    