import telebot
import datetime
from telebot import types

with open("./acm.token", "r") as TOKEN:
    bot = telebot.TeleBot(TOKEN.read().strip())


def listener(messages):
    # When new messages arrive TeleBot will call this function.
    for m in messages:
        now = str(datetime.datetime.now()).split(' ')[-1].split('.')[0]
        if m.content_type == 'text':
            # Prints the sent message to the console
            if m.chat.type == 'private':
                print(now + ":: Chat -> " + str(m.chat.first_name) +
                      " [" + str(m.chat.id) + "]: " + m.text)
        else:
            print(now + ":: Group -> " + str(m.chat.title) +
                  " [" + str(m.chat.id) + "]: " + m.text)


@bot.inline_handler(lambda query: query.query == 'menu')
def menu(inline_query):
    image_name = './menu.jpg'
    r = types.InlineQueryResultPhoto('1',
                                     'Result1',
                                     image_name,
                                     input_message_content=types.InputTextMessageContent('hi'))
    bot.answer_inline_query(inline_query.id, [r])

print("Running...")

bot.polling()
