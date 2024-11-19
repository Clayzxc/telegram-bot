import telebot
from telebot import types
import webbrowser
from telebot.apihelper import send_photo
import random

bot = telebot.TeleBot('7937961728:AAHq8HLlp8Wh8faKPyI6ZPxezVK1X3TJOkY')

meme = ['https://static9.tgstat.ru/channels/_0/2c/2c8a6764da71e3b35436b5be1545aa72.jpg', 'https://sun9-29.userapi.com/s/v1/ig2/ZeZidw-4nVYSQoU3ooToMgSdWAtAWPNLluQ0FfxVN0FdPeUdMviVzlaBJGuNnLbuUayXCC6O2LgQUWKe_Bt4gqO2.jpg?quality=96&as=32x26,48x38,72x58,108x87,160x128,240x192,360x289,480x385,540x433,600x481&from=bu&u=Dr7moSn6ghrOh9wi5_opjZEMdVA55WDuvnmaYO4uFLM&cs=600x481', 'https://i.pinimg.com/originals/dd/2b/df/dd2bdfe9dc1a289df7819ed80f1f5d83.jpg', 'https://3fc4ed44-3fbc-419a-97a1-a29742511391.selcdn.net/coub_storage/coub/simple/cw_image/a0323f14c5a/c5f3ef8ea915fa248a16c/1515177326_00032.jpg']

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Go on Instagram')
    markup.row(button1)
    button2 = types.KeyboardButton('Prediction')
    markup.row(button2)
    bot.send_message(message.chat.id, 'Hello!', reply_markup = markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Go on Instagram':
        webbrowser.open('https://www.instagram.com')
    elif message.text == 'Prediction':
        bot.send_photo(message.chat.id, photo = random.choice(meme))
    bot.register_next_step_handler(message, on_click)

@bot.message_handler(commands = ['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <u>information</u>', parse_mode = 'html')

@bot.message_handler(commands = ['site', 'website'])
def site(message):
    webbrowser.open('https://music.youtube.com')

@bot.message_handler(content_types = ['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Go on Instagram', url = 'https://www.instagram.com')
    markup.row(button1)
    button2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    button3 = types.InlineKeyboardButton('Edit text', callback_data = 'edit')
    markup.row(button2, button3)
    bot.reply_to(message, 'This photo looks pretty! You should definitely post it ;)', reply_markup = markup)

@bot.message_handler(commands = ['prediction'])
def prediction(message):
    bot.send_photo(message.chat.id, photo=random.choice(meme))

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'<b>ID:</b> <u>{message.from_user.id}</u>', parse_mode = 'html')

bot.polling(none_stop = True)