import os,telebot,tempfile,webbrowser,pyautogui,tinytuya
import screen_brightness_control as sbc
from PIL import ImageGrab
pyautogui.FAILSAFE = False

device = tinytuya.BulbDevice('-', '-', '-')
device.set_version(3.3)

API_TOKEN = '-'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Умный дом 🏠")
    markup.add("Управление настройками 🔊")
    markup.add("Управление клавиатурой ⌨️")
    markup.add("Включение/Перезагрузка 🔛")
    markup.add("Работа с браузером 🌐")
    markup.add("Получить скриншот 📸")
    bot.send_message(message.chat.id, '👋 дарова чел 👋', reply_markup=markup)

@bot.message_handler(commands=['reload'])
def echo_message(message):
    send_welcome(message)


@bot.message_handler(regexp='Умный дом 🏠')
def echo_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = telebot.types.KeyboardButton('ON')
    b2 = telebot.types.KeyboardButton('OFF')
    b4 = telebot.types.KeyboardButton('Назад 🔙')
    b3 = telebot.types.KeyboardButton('Brightness')
    markup.row(b1)
    markup.row(b2)
    markup.row(b3)
    markup.row(b4)
    bot.send_message(message.chat.id, 'Чё делаем жиез?', reply_markup=markup)

    @bot.message_handler(regexp='Назад 🔙')
    def echo_message(message):
        bot.send_message(message.chat.id, 'Возвращаюсь..')
        send_welcome(message)
                
    @bot.message_handler(regexp='ON')
    def echo_message(message):
        bot.send_message(message.chat.id, 'Включил свет в спальне')
        device.turn_on()              

    @bot.message_handler(regexp='OFF')
    def echo_message(message):
        bot.send_message(message.chat.id, 'Выключил свет в спальне')
        device.turn_off()

    @bot.message_handler(regexp='Brightness')
    def echo_message(message):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = telebot.types.KeyboardButton('Increase')
        b2 = telebot.types.KeyboardButton('Decrease')
        b3 = telebot.types.KeyboardButton('Назад 🔙')
        markup.row(b1,b2)
        markup.row(b3)
        bot.send_message(message.chat.id, '??', reply_markup=markup)
        
        @bot.message_handler(regexp='Increase')
        def echo_message(message):
            bot.send_message(message.chat.id, '...', reply_markup=markup)
            device.set_brightness(device.brightness()+300)
            bot.send_message(message.chat.id, f'Current brightness: {device.brightness()}', reply_markup=markup)
        @bot.message_handler(regexp='Decrease')
        def echo_message(message):
            bot.send_message(message.chat.id, 'Ready', reply_markup=markup)
            device.set_brightness(device.brightness()-300)
            bot.send_message(message.chat.id, f'Current brightness: {device.brightness()}', reply_markup=markup)
        @bot.message_handler(regexp='Назад 🔙')
        def echo_message(message):
            bot.send_message(message.chat.id, 'Возвращаюсь..')
            send_welcome(message)

@bot.message_handler(regexp='Управление клавиатурой ⌨️')
def echo_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = telebot.types.KeyboardButton('⬅️')
    b2 = telebot.types.KeyboardButton('⏸️')
    b3 = telebot.types.KeyboardButton('➡️')
    b4 = telebot.types.KeyboardButton('Назад 🔙')
    markup.row(b1,b2,b3)
    markup.row(b4)
    bot.send_message(message.chat.id, 'Чё делаем жиез?', reply_markup=markup)

    @bot.message_handler(regexp='Назад 🔙')
    def echo_message(message):
        bot.send_message(message.chat.id, 'Возвращаюсь..')
        send_welcome(message)

    @bot.message_handler(regexp='⬅️')
    def echo_message(message):
        bot.send_message(message.chat.id, 'двиганул влево жиес')
        pyautogui.press('left')

    @bot.message_handler(regexp='⏸️')
    def echo_message(message):
        bot.send_message(message.chat.id, 'прожал пробельчик да')
        pyautogui.press('space')
    @bot.message_handler(regexp='➡️')
    def echo_message(message):
        bot.send_message(message.chat.id, 'двиганул вправо жиес')
        pyautogui.press('right')

@bot.message_handler(regexp='Управление настройками 🔊')
def echo_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = telebot.types.KeyboardButton('Увеличить громкость 📈')
    b2 = telebot.types.KeyboardButton('Уменьшить громкость 📉')
    b3 = telebot.types.KeyboardButton('Изменить яркость')
    b4 = telebot.types.KeyboardButton('Назад 🔙')
    markup.row(b1,b2)
    markup.row(b3,b4)
    bot.send_message(message.chat.id, 'Что делаем?', reply_markup=markup)

    @bot.message_handler(regexp='Назад 🔙')
    def echo_message(message):
        bot.send_message(message.chat.id, 'Возвращаюсь..')
        send_welcome(message)

    @bot.message_handler(regexp='Увеличить громкость 📈')
    def echo_message(message):
        bot.send_message(message.chat.id, '+15%')
        pyautogui.press('volumeup',7)

    @bot.message_handler(regexp='Уменьшить громкость 📉')
    def echo_message(message):
        bot.send_message(message.chat.id, '-15%')
        pyautogui.press('volumedown',7)

    @bot.message_handler(regexp='Изменить яркость')
    def echo_message(message):
        
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = telebot.types.KeyboardButton('Соточка')
        b2 = telebot.types.KeyboardButton('Полтос')
        b3 = telebot.types.KeyboardButton('На ноль')
        b4 = telebot.types.KeyboardButton('Назад 🔙')
        markup.row(b1,b2,b3)
        markup.row(b4)
        bot.send_message(message.chat.id, '??', reply_markup=markup)

        @bot.message_handler(regexp='Соточка')
        def echo_message(message):
            bot.send_message(message.chat.id, 'Поставил на 100')
            sbc.set_brightness(100)

        @bot.message_handler(regexp='Полтос')
        def echo_message(message):
            bot.send_message(message.chat.id, 'Поставил на 50')
            sbc.set_brightness(50)       

        @bot.message_handler(regexp='На ноль')
        def echo_message(message):
            bot.send_message(message.chat.id, 'Поставил на 0')
            sbc.set_brightness(1)

        @bot.message_handler(regexp='Назад 🔙')
        def echo_message(message):
            bot.send_message(message.chat.id, 'Возвращаюсь..')
            send_welcome(message)

@bot.message_handler(regexp='Включение/Перезагрузка 🔛')
def echo_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Выключить 📴")
    markup.add("Перезагрузка 🔃")
    markup.add("Назад 🔙")
    bot.send_message(message.chat.id, 'Выключить или перезагрузить?', reply_markup=markup)

    @bot.message_handler(regexp='Назад 🔙')
    def echo_message(message):
        bot.send_message(message.chat.id, 'Возвращаюсь..')
        send_welcome(message)
    @bot.message_handler(regexp='Выключить 📴')
    def echo_message(message):
        bot.send_message(message.chat.id, 'Выключаю...')
        send_welcome(message)
        os.system("shutdown -s -t 0")
    @bot.message_handler(regexp='Перезагрузка 🔃')
    def echo_message(message):
        bot.send_message(message.chat.id, 'Перезагружаю...')
        send_welcome(message)
        os.system("shutdown -t 0 -r -f")

@bot.message_handler(regexp='Работа с браузером 🌐')
def echo_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("Дождь 🌧️")
    markup.add("VK 😍")
    markup.add("Назад 🔙")
    
    bot.send_message(message.chat.id, 'Чего включаем?', reply_markup=markup)

    @bot.message_handler(regexp='Назад 🔙')
    def echo_message(message):
        bot.send_message(message.chat.id, 'Возвращаюсь..')
        send_welcome(message)
    @bot.message_handler(regexp='Дождь 🌧️')
    def echo_message(message):
        bot.send_message(message.chat.id, 'Подрубалити из реалити, спокойной ночи)')
        webbrowser.open('https://youtu.be/cPlnjdnPU74?t=1', new=2)
    @bot.message_handler(regexp='VK 😍')
    def echo_message(message):
        bot.send_message(message.chat.id, 'Запускаем..')
        webbrowser.open('https://vk.com/im', new=2)

@bot.message_handler(regexp='Получить скриншот 📸')
def echo_message(message):
    path = tempfile.gettempdir() + 'screenshot.png'
    screenshot = ImageGrab.grab()
    screenshot.save(path, 'PNG')
    bot.send_photo(message.chat.id, open(path, 'rb'))



bot.infinity_polling()
