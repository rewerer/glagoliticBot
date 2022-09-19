import telebot
from transliter import GlagoliticTransliter
from keyboa import Keyboa

TOKEN = 'aboba'
bot = telebot.TeleBot(TOKEN)
MODE = 'none'

def cyrillic_to_glagolitic():
    global MODE
    if MODE == 'none' or MODE == 'glagolitic_to_cyrillic':
        MODE = 'cyrillic_to_glagolitic'


def glagolitic_to_cyrillic():
    global MODE
    if MODE == 'none' or MODE == 'cyrillic_to_glagolitic':
        MODE = 'glagolitic_to_cyrillic'


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global MODE
    if call.data == 'кириллица => глаголица':
        cyrillic_to_glagolitic()
        print('press button: "/cyrillic_to_glagolitic"')
    elif call.data == 'глаголица => кириллица':
        glagolitic_to_cyrillic()
        print('press button: "/glagolitic_to_cyrillic"')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    menu = ["кириллица => глаголица", "глаголица => кириллица"]
    keyboard = Keyboa(items=menu)
    bot.send_message(m.chat.id, 'Добро пожаловать выберите режим трансляции.', reply_markup=keyboard())


@bot.message_handler(commands=["cyrillic_to_glagolitic"])
def cyrillic_to_glagolitic_endpoint(m, res=False):
    cyrillic_to_glagolitic()


@bot.message_handler(commands=["glagolitic_to_cyrillic"])
def glagolitic_to_cyrillic_endpoint(m, res=False):
    glagolitic_to_cyrillic()


@bot.message_handler(content_types=["text"])
def handle_text(message):
    global MODE
    sended_message = ''
    if MODE == 'cyrillic_to_glagolitic':
        sended_message = GlagoliticTransliter.cyrillic_to_glagolitic(message.text)
        bot.send_message(message.chat.id, sended_message)
    elif MODE == 'glagolitic_to_cyrillic':
        sended_message = GlagoliticTransliter.glagolitic_to_cyrillic(message.text)
        bot.send_message(message.chat.id, sended_message)
    else:
        bot.send_message(message.chat.id, 'Выберите режим!')
    print(message.chat.id, ': ', message.text)
    print(message.chat.id, '(bot): ', sended_message)

bot.polling(none_stop=True, interval=0)