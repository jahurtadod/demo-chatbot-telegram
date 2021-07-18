from os import name
from telegram.ext import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import connection_dbpedia as search
import demo_spacy as analysis
import Constants as keys
import menu

INPUT_TEXT = 0

# Set up the logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

# Message error


def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')

# MENUS


def menu_command(update, context):
    update.message.reply_text("Bienvenido, soy geo ¿vamos por una pizza?",
                              reply_markup=menu.main_menu_keyboard())


def main_menu(update, context):
    query = update.callback_query
    query.edit_message_text(text="Bienvenido, soy geo ¿vamos por una pizza?",
                            reply_markup=menu.main_menu_keyboard())


def first_menu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="¿De qué tamaño quieres la pizza?",
        reply_markup=menu.first_menu_keyboard())


def first_submenu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="¿Está seguro que desea ordenar esta pizza?",
        reply_markup=menu.first_submenu_keyboard())


def second_menu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="Para crear una pizza primero indícame cuantas cubiertas tendrá tu pizza",
        reply_markup=menu.second_menu_keyboard())


def second_submenu(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="Aún estamos trabajando en esta función, cuando este recién orneada te cuento ¿vale?",
        reply_markup=menu.second_submenu_keyboard())


def second_submenu_1(update, context):
    query = update.callback_query
    query.edit_message_text(
        text="Listo te avisare cuando esté listo")

# COMMANDS


def help_command(update, context):
    update.message.reply_text(
        "George\'s Pizza permite realizar pedidos, revisar y crear pizzas a tu gusto!"
        "\n\nYo soy Geo, tu asistente te apoyare en todo tu recorrido"
        "\n/start Si tienes alguna duda de como puedes interactuar conmigo"
        "t\n\nEncontramos a Geo en busca de probar todas las pizzas del mundo, de como termino aqui no lo sabemos pero, creo que le gusta estar aquí")


def ingredients_command(update, context):
    user_says = " ".join(context.args)
    # update.message.reply_text("You said: " + user_says)
    update.message.reply_text(
        "Los ingredientes de  " + user_says + " son:\n\n"+search.get_response_dbpedia_ingredients(user_says.capitalize()))


def custom_command(update, context):
    update.message.reply_text(
        'Este es un comando de prueba\n\nGeo hora de una orden!')


def pizza_command(update, context):
    update.message.reply_text(
        "Vamos por una pizza\n\nSeleccione la pizza que desea:"
        "\nPizza_al_taglio"
        "\nDetroit-style_pizza"
        "\nNeapolitan_pizza"
        "\nDeep-fried_pizza"
        "\nDeep-fried_pizza"
        "\nItalian_tomato_pie"
        "\nSicilian_pizza"
        "\nChicago-style_pizza"
    )


def start_command(update, context):
    update.message.reply_text(
        'Hola, yo soy Geo\n\nTratare de entender tus mensajes si encuentro algo lo buscare en DBpedia para expandir nuestro conocimiento')
    update.message.reply_text(
        "Puedes usar los sientes comandos :\n"
        "\n/formenu usar un menu para facilitar tu pediodo"
        "\n/help para buscar mas información de mí"
        "\n/custom comando de prueba"
        "\n/types mostrar el listado de pizzas"
        "\n/pizza muestra las pizzas que puedes buscar"
        "\n/ingredients 'nombre de la pizza' permite buscar los ingredientes de la pizza")


def types_command(update, context):
    qres = search.get_response_dbpedia_pizzas()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name, comment, image_url = result['name']['value'], result['comment']['value'], result['image']['value']
        update.message.reply_text('Nombre de la pizza : ' + name +
                                  "\n\nDescripción : " + comment + "\n" + image_url)


# def pizza_callback_handler(update, context):
#     query = update.callback_query
#     query.answer()

#     # query.edit_message_text(
#     #    text=('Listo ' + update.callback_query.message.chat.first_name +
#     #          ', comencemos por seleccionar la pizza que deseas:')
#     # )
#     button1 = InlineKeyboardButton(
#         text='Descarga la app de George\'s Pizza',
#         url='https://github.com/jahurtadod/sematic-app-demo'
#     )

#     update.message.reply_text(
#         text='Bienvenido, soy geo ¿vamos por una pizza?',
#         reply_markup=InlineKeyboardMarkup([
#             [button1]
#         ])
#     )


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    listNoun = []
    listVerb = []
    # response = responses.get_response(text)
    # update.message.reply_text(response)
    # update.message.reply_text("te amo")
    doc = analysis.spacy_info(text)
    for w in doc:
        update.message.reply_text(w.text + " es un " + w.pos_)
        if w.pos_ == "NOUN" or "PROPN":
            listNoun.append(w.text)
        if w.pos_ == "VERB":
            listVerb.append(w.text)

    update.message.reply_text("Encontrado información entorno a tu mensaje")
    for list in listNoun:
        update.message.reply_text(
            "Información sobre "+list+" :\n\n"+search.get_response_dbpedia(list.capitalize()))


if __name__ == '__main__':
    updater = Updater(token=keys.API_KEY, use_context=True)

    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('formenu', menu_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))
    dp.add_handler(CommandHandler('types', types_command))
    dp.add_handler(CommandHandler('pizza', pizza_command))
    dp.add_handler(CommandHandler(
        'ingredients', ingredients_command, pass_args=True))

    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
    dp.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))

    dp.add_handler(CallbackQueryHandler(
        first_submenu, pattern='m3', pass_chat_data=True))

    dp.add_handler(CallbackQueryHandler(second_submenu, pattern='m4'))
    dp.add_handler(CallbackQueryHandler(second_submenu_1, pattern='m5'))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
