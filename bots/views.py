import telebot
from telebot import types


API_TOKEN = '6091100310:AAEcnQ0wTXoUIFM1Iq9Tixw_QKhzZ22_hr8'

bot = telebot.TeleBot(API_TOKEN)

def generate_markup(options, back=False):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    for option in options:
        markup.add(types.KeyboardButton(option))
    if back:
        markup.add(types.KeyboardButton('Back'))
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    options = ['Option 1', 'Option 2']
    markup = generate_markup(options)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Option 1":
        options = ['Suboption 1', 'Suboption 2']
        markup = generate_markup(options, back=True)
        bot.send_message(message.chat.id, "You chose Option 1. Choose a suboption:", reply_markup=markup)
    elif message.text == "Option 2":
        options = ['Suboption 3', 'Suboption 4']
        markup = generate_markup(options, back=True)
        bot.send_message(message.chat.id, "You chose Option 2. Choose a suboption:", reply_markup=markup)
    elif message.text.startswith("Suboption"):
        options = ['Subsuboption 1', 'Subsuboption 2']
        markup = generate_markup(options, back=True)
        bot.send_message(message.chat.id, f"You chose {message.text}. Choose a subsuboption:", reply_markup=markup)
    elif message.text.startswith("Subsuboption"):
        bot.send_message(message.chat.id, f"You chose {message.text}")
    elif message.text == "Back":
        options = ['Option 1', 'Option 2']
        markup = generate_markup(options)
        bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

bot.polling()