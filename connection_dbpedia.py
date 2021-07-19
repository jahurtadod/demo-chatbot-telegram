from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('https://dbpedia.org/sparql')


def get_response_dbpedia(item):
    sparql.setQuery(f'''
        SELECT ?name ?comment
        WHERE {{
            dbr:{item} rdfs:label ?name .
            dbr:{item} rdfs:comment ?comment .
            FILTER (lang(?name) = 'es')
            FILTER (lang(?comment) = 'es')
        }}
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()

    if len(qres['results']['bindings']) == 0:
        # print("---------------------")
        return "Información no encontrada"

    else:
        result = qres['results']['bindings'][0]
        comment = result['comment']['value']
        # print("---------------------me lleva")
        return comment

def get_response_dbpedia_food(item):
    sparql.setQuery(f'''
        SELECT distinct ?label
        WHERE {{
            ?s rdfs:label ?label .
            ?s rdf:type dbo:Food .
            ?s dbo:ingredient ?ingredient .
            ?ingredient rdfs:label ?ingredientLabel .
            FILTER regex(?ingredientLabel , "{item}", "i") 
            FILTER regex(?label, "pizza", "i") 
            FILTER (lang(?label) = "es") 
            FILTER (lang(?ingredientLabel) = "es") 
        }}
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres

def get_response_dbpedia_ingredients(item):
    sparql.setQuery(f'''
        SELECT ?ingredientName
        WHERE {{ 
            dbr:{item} dbo:ingredientName ?ingredientName .
        }}
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()

    if len(qres['results']['bindings']) == 0:
        # print("---------------------")
        return "Información no encontrada"

    else:
        result = qres['results']['bindings'][0]
        ingredient = result['ingredientName']['value']
        # print("---------------------me lleva")
        return ingredient


def get_response_dbpedia_pizzas():
    sparql.setQuery(f'''
        SELECT ?name ?comment ?image
        WHERE {{
            ?object dbo:type dbr:Pizza .
            ?object rdfs:label ?name .
            ?object rdfs:comment ?comment .
            ?object dbo:thumbnail ?image .

            FILTER (lang(?name) = 'es')
            FILTER (lang(?comment) = 'es')
        }}
    ''')

    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()

    return qres


def get_response_dbpedia_pizzasname():
    sparql.setQuery(f'''
        SELECT ?name ?comment ?image
        WHERE {{
            ?object dbo:type dbr:Pizza .
            ?object rdfs:label ?name .
            ?object rdfs:comment ?comment .
            ?object dbo:thumbnail ?image .

            FILTER (lang(?name) = 'es')
            FILTER (lang(?comment) = 'es')
        }}
    ''')

    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()

    return qres


if __name__ == '__main__':

    result = get_response_dbpedia_pizzas()
    for item in result:
        name, comment, image_url = result['name']['value'], result['comment']['value'], result['image']['value']
        # print ('Nombre de la pizza : ' + name + "\n Descripción : " + comment + "\n" + image_url)
    # print(get_response_dbpedia(item))
    # print_response_dbpedia(qres)
