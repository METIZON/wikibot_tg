import telebot
import wikipedia

# http://t.me/Wiki_tg_bot
# telegram: t.me/metiz0n

bot = telebot.TeleBot('[YOUR TOKEN HERE]')


markup1 = telebot.types.InlineKeyboardMarkup()


russian = telebot.types.InlineKeyboardButton(text='Russian',
                                             callback_data='ru')
english = telebot.types.InlineKeyboardButton(text='English',
                                             callback_data='en')
markup1.add(russian)
markup1.add(english)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='🇷🇺 Для начала, '
                     'выберите ваш язык: 🇷🇺'
                     '\n🇺🇸 Choose your lang: 🇺🇸',
                     reply_markup=markup1)

    @bot.callback_query_handler(func=lambda call: True)
    def query_handler(call):
        if call.data == 'ru':
            bot.send_message(message.chat.id, 'Вас приветствует Wikibot! '
                             'Моя цель, это найти всё, что вы спросите! '
                             'Для поиска нужного текста, введите '
                             '/search [текст]',)
            wikipedia.set_lang("ru")
        if call.data == 'en':
            bot.send_message(message.chat.id, 'Welcome! My name is Wikibot!'
                             'My goal is to find everything you need'
                             'Type /search [text] to find sth! Good luck!')
            wikipedia.set_lang("en")


@bot.message_handler(commands=['search'])
def search(message):
    try:
        msg = message.text.replace('/search', '')
        srch = wikipedia.summary(msg)
        bot.send_message(message.chat.id, srch)
    except Exception:
        bot.send_message(message.chat.id, 'Crash: '
                         '[Can\'t find your request...]')


bot.polling()
