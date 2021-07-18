from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import connection_georgepizza as georgepizza


def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Descarga la app de George\'s Pizza',
                                      url='https://github.com/jahurtadod/sematic-app-demo')],
                [InlineKeyboardButton(
                    'Solicitar una pizza', callback_data='m1')],
                [InlineKeyboardButton('Crear una pizza', callback_data='m2')]]
    return InlineKeyboardMarkup(keyboard)


def first_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Menu Principal', callback_data='main')]]

    qres = georgepizza.get_pizzas()

    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        print(name)
        keyboard.insert(0, [InlineKeyboardButton(
            name, callback_data='m3')])

    return InlineKeyboardMarkup(keyboard)


def first_submenu_keyboard():
    keyboard = [[InlineKeyboardButton('Si, proceder a pagar',
                                      url='https://github.com/jahurtadod/sematic-app-demo')],
                [InlineKeyboardButton('No, Menu Principal', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def second_menu_keyboard():
    keyboard = [[InlineKeyboardButton('1 Cubierta', callback_data='m4')],
                [InlineKeyboardButton('2 Cubiertas', callback_data='m4')],
                [InlineKeyboardButton('3 Cubiertas', callback_data='m4')],
                [InlineKeyboardButton('Menu Principal', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def second_submenu_keyboard():
    keyboard = [[InlineKeyboardButton('De acuerdo', callback_data='m5')],
                [InlineKeyboardButton('Menu Principal', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)
