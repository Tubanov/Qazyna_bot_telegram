import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('8038407331:AAHkKlCrd0g5LIRvw24MelNFu07Gi7D-xMc')

first_name = None

@bot.message_handler(commands=['start'])
def start(message):
    username = message.from_user.username
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🛒 Посмотреть каталог товаров')
    btn2 = types.KeyboardButton('📦 Узнать о текущих акциях и скидках')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('📍 Найти наш магазин на карте')
    btn4 = types.KeyboardButton('🛠 Получить консультацию специалиста')
    markup.row(btn3, btn4)

    if username == 'q1w2eer':
        btn_admin = types.KeyboardButton('📋 Заявки')
        markup.add(btn_admin)
    bot.send_message(message.chat.id, f"""Приветствуем вас в строительном магазине "Qazyna"! 🏗️

Здесь вы найдете всё для строительства и ремонта: от инструментов до строительных материалов. Мы рады предложить вам качественную продукцию по доступным ценам!

Что вы хотите сделать?

🛒 Посмотреть каталог товаров
📦 Узнать о текущих акциях и скидках
📍 Найти наш магазин на карте
🛠 Получить консультацию специалиста 

Просто выберите нужную опцию, и мы поможем вам с любым вопросом!""", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == '📍 Найти наш магазин на карте')
def callback_addres(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('2ГИС', url='https://2gis.kz/taraz/geo/70000001052642114')
    btn2 = types.InlineKeyboardButton('Яндекс Навигатор', url='https://yandex.ru/navi/org/kazyna/241483308849?si=29w5j2pf7p2dnk10881tx2whnr')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f"""📍 Наш адрес: 🏙 г. Тараз, проспект Жамбыла, 87

Заглядывайте к нам за качественными строительными материалами и профессиональной консультацией! Мы всегда рядом, чтобы помочь с любым вопросом!""", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == '🛒 Посмотреть каталог товаров')
def calback_catalog(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт!', url='http://127.0.0.1:8000/'))
    bot.send_message(message.chat.id, f"""🛒 Вы можете ознакомиться с нашим каталогом товаров на сайте!""", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == '🛠 Получить консультацию специалиста')
def base(message):
    conn = sqlite3.connect('Qazyna_bot_telegram.db')
    cur = conn.cursor()


    cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, phone_number TEXT)''')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Введите ваше имя:')
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global first_name
    first_name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите номер телефона:')
    bot.register_next_step_handler(message, get_number)


def get_number(message):
    phone_number = message.text.strip()
    username = message.from_user.username


    conn = sqlite3.connect('Qazyna_bot_telegram.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (first_name, phone_number) VALUES (?, ?)", (first_name, phone_number))
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()

    if username == 'q1w2eer':
        markup.add(types.InlineKeyboardButton('Список пользователей', callback_data='users'))

    bot.send_message(message.chat.id, 'Спасибо за ваш запрос! Наши сотрудники свяжутся с вами в ближайшее время. 📞 Ожидайте звонка! 😊', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'users')
def callback(call):
    conn = sqlite3.connect('Qazyna_bot_telegram.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'<i><b>Имя:</b></i> {el[1]}, <i><b>Номер телефона:</b></i> {el[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info, parse_mode='html')

@bot.message_handler(func=lambda message: message.text == '📋 Заявки')
def handle_requests(message):
    conn = sqlite3.connect('Qazyna_bot_telegram.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'<i><b>Имя:</b></i> {el[1]}, <i><b>Номер телефона:</b></i> {el[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, info, parse_mode='html')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    bot.send_message(message.chat.id, '<a href="http://127.0.0.1:8000/">Qazyna WebSite</a>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, message)


bot.polling(none_stop=True)