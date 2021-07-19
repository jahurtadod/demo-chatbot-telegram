import re


def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())
    # print(list_message)

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Custom responses
    response_list = [
        # process_message(
        #     message, ['hola', 'buenos dias', 'hey', 'holi'], 'Hola 😃, quieres comprar una pizza ?'),
        # process_message(message, ['adios', 'salir', 'cuidate', 'gracias'],
        #                 'Adiós!, espero que vuelvas pronto\nQuieres validar tu experiencia de compra'),
        # process_message(message, ['llamas', 'nombre'],
        #                 'Mi nombre is Geo, encantada de conocerte!'),
        # process_message(message, ['help', 'ayuda', 'informacion', 'información'],
        #                 'Haré todo lo posible para ayudarte\n\nSi tienes dudas podemos puedes usar el comando /start'),
        # process_message(message, ['pedir', 'ordenar', 'comprar', 'si'],
        #                 'Indicame que pizza deseas'),
        # process_message(message, ['especial', 'george', 'mariscos'],
        #                 'Listo, te informare cuando este la pizza, esperame\n\n /pagar Proceder a pagar'),
        # process_message(message, ['cancelar', 'ya no quiero'],
        #                 'Nooo, que pena cancelare tu pedido'),
        process_message(message, ['querer', 'dar', "ordenar", "damar", "pedir", "comer", "servir", "desear", "apetecer"], "si")
    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = False
    else:
        bot_response = True

    print('Bot response:', bot_response)
    return bot_response
