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


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()

