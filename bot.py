import random
from telegram.ext import Updater, CommandHandler

# Liste de blagues
blagues = [
    "Pourquoi les plongeurs plongent-ils toujours en arrière ? Parce que sinon ils tombent dans le bateau 😂",
    "Quel est le comble pour un électricien ? De ne pas être au courant ⚡",
    "Docteur, j’ai mal quand je fais ça ! – Alors ne faites plus ça 🤣"
]

def start(update, context):
    update.message.reply_text("Bienvenue sur 🎉 Zone Fun Bot 🎉 ! Tape /blague pour rigoler 😃")

def blague(update, context):
    update.message.reply_text(random.choice(blagues))

# Ici ton vrai token
updater = Updater("8311439481:AAFkqUJVSaeAAvEWCYxhIIuaBa04ZypiMGk", use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("blague", blague))

updater.start_polling()
updater.idle()
