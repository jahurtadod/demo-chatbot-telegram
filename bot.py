import logging
from telegram.ext import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import responses
import Constants as keys

INPUT_TEXT = 0

# Set up the logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):

    button1 = InlineKeyboardButton(
        text='Descarga la app de George\'s Pizza',
        url='https://github.com/jahurtadod/sematic-app-demo'
    )

    button2 = InlineKeyboardButton(
        text='Solicitar Pizza',
        callback_data='pizza'
    )

    button3 = InlineKeyboardButton(
        text='Crear Pizzas',
        url='https://github.com/jahurtadod/sematic-app-demo'
    )

    update.message.reply_text(
        text='Bienvenido, soy geo ¿vamos por una pizza?',
        reply_markup=InlineKeyboardMarkup([
            [button3],
            [button2],
            [button1]
        ])
    )


def help_command(update, context):
    update.message.reply_text(
        'George\'s Pizza permite realizar pedidos, revisar y crear pizzas a tu gusto!')


def custom_command(update, context):
    update.message.reply_text('Este es un comando de prueba')


def pizza_command(update, context):
    update.message.reply_text('Seleccione la pizza que desea')


def pizza_callback_handler(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Seleccione la pizza que desea'
    )


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programme
if __name__ == '__main__':
    updater = Updater(token=keys.API_KEY, use_context=True)

    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('pizza', pizza_command),
            CallbackQueryHandler(pattern='pizza', callback=pizza_callback_handler)
        ],

        states={
            INPUT_TEXT: [MessageHandler(Filters.text, handle_message)]
        },

        fallbacks=[]
    ))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
