import telebot
from transliter import GlagoliticTransliter
from keyboa import Keyboa

TOKEN = 'aboba'
bot = telebot.TeleBot(TOKEN)
MODE = 'none'

def english_to_gothic():
    global MODE
    MODE = 'english_to_gothic'

def cyrillic_to_glagolitic():
    global MODE
    MODE = 'cyrillic_to_glagolitic'


def glagolitic_to_cyrillic():
    global MODE
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
    elif call.data == 'latin => gothic':
        english_to_gothic()
        print(call.data)
        print('press button: "/english_to_gothic"')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    menu = ["кириллица => глаголица", "глаголица => кириллица", "latin => gothic"]
    keyboard = Keyboa(items=menu)
    bot.send_message(m.chat.id, 'Добро пожаловать выберите режим трансляции.', reply_markup=keyboard())

@bot.message_handler(commands=["english_to_gothic"])
def english_to_gothic_endpoint(m, res=False):
    english_to_gothic()

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
    elif MODE == 'english_to_gothic':
        sended_message = GlagoliticTransliter.english_to_gothic(message.text)
        bot.send_message(message.chat.id, sended_message)
    else:
        bot.send_message(message.chat.id, 'Выберите режим!')
    print(message.chat.id, ': ', message.text)
    print(message.chat.id, '(bot): ', sended_message)

bot.polling(none_stop=True, interval=0)