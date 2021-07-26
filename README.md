## ChatBot Pizza 
### UTPL - Sistemas Basados en Conocimientos

Nombre: Jorge Alcivar Hurtado Duarte

![](https://github.com/jahurtadod/demo-chatbot-telegram/blob/main/images/imagen2.png)

El ChatBot "Geo" Permite realizar consultas y recuperar información de pizzas de DBpedia y ontología George's Pizza

Para el uso del proyecto, cambiamos el token del bot (keys.API_KEY)

```python
updater = Updater(token=keys.API_KEY, use_context=True)
``` 

### Características del bot

1. Nos muestra el análisis del mensaje ingresado por el usuario, captura los verbos e infiere la intención del usuario.

![](https://github.com/jahurtadod/demo-chatbot-telegram/blob/main/images/imagen1.png)

> Cuando se detecta la intención de comprar una pizza se realiza una búsqueda del pedido de la información de DBpedia, para el caso del ejemplo la entrada que se dio fue: "dame una pizza de tomate
"

![](https://github.com/jahurtadod/demo-chatbot-telegram/blob/main/images/imagen4.png)

1. Permite realizar consultas a DBpedia y a la ontología creada para el proyecto.
```python
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
``` 

> Para la ontologia del proyecto recopilamos la informacion de forma local con el uso de Apache Fuseki
```python
    sparql.setQuery('''
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX pizza: <http://www.semanticweb.org/jorge/ontologies/2021/5/PizzaTutorial#>
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf pizza:NamedPizza .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }
    ''')
``` 

3. Facilitar al navegacion y uso del bot mediante un menu
```python
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Descarga la app de George\'s Pizza',
                                      url='https://github.com/jahurtadod/sematic-app-demo')],
                [InlineKeyboardButton(
                    'Solicitar una pizza', callback_data='m1')],
                [InlineKeyboardButton('Crear una pizza', callback_data='m2')],
                [InlineKeyboardButton('Solicitar una bebida', callback_data='m2')]
                ]
    return InlineKeyboardMarkup(keyboard)
``` 

![](https://github.com/jahurtadod/demo-chatbot-telegram/blob/main/images/imagen3.png)

