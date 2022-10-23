import os
import telebot
import tempfile
from PIL import ImageGrab
import pyautogui
pyautogui.FAILSAFE = False
API_TOKEN = '5696614832:AAETZRjAntx5LT5CZhaFJGy7A-3f56hFgBk'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Получить скриншот 📸")
    markup.add("Изменить громкость 🔊")
    markup.add("Управление клавиатурой ⌨️")
    markup.add("Включение/Перезагрузка 🔛")
    bot.send_message(message.chat.id, '👋 дарова чел 👋', reply_markup=markup)

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

@bot.message_handler(regexp='Изменить громкость 🔊')
def echo_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Увеличить громкость 📈")
    markup.add("Уменьшить громкость 📉")
    markup.add("Назад 🔙")
    bot.send_message(message.chat.id, 'Увеличить или уменьшить?', reply_markup=markup)

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
        os.system("shutdown -s -t 0")
    @bot.message_handler(regexp='Перезагрузка 🔃')
    def echo_message(message):
        bot.send_message(message.chat.id, 'Перезагружаю...')
        os.system("shutdown -t 0 -r -f")

@bot.message_handler(regexp='Получить скриншот 📸')
def echo_message(message):
    path = tempfile.gettempdir() + 'screenshot.png'
    screenshot = ImageGrab.grab()
    screenshot.save(path, 'PNG')
    bot.send_photo(message.chat.id, open(path, 'rb'))


bot.infinity_polling()