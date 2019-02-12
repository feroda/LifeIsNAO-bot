from telegram.ext import Updater, CommandHandler

from naoqi import ALProxy

from settings import TOKEN, NAO_IP, NAO_PORT


def hello(bot, update):
    msg = 'Hello {},sei in chat {}'.format(
		update.message.from_user.first_name,
		update.message.chat.title)

    update.message.reply_text(msg)

    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
    tts.say(msg)

def say(bot, update):
    txt = '{}'.format()
		
def echo(bot, update):
    txt = update.message.text[6:]
    update.message.reply_text(txt)
    
    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
    tts.say(txt)
    
updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('say', say))
updater.dispatcher.add_handler(CommandHandler('echo', echo))

updater.start_polling()
updater.idle()

