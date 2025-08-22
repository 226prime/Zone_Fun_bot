import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random

# Active les logs (utile pour Render)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Ton token (ne le partage plus à personne 😉)
TOKEN = "8311439481:AAFkqUJVSaeAAvEWCYxhIIuaBa04ZypiMGk"

# Exemple de blagues
jokes = [
    "Pourquoi les programmeurs préfèrent-ils l'obscurité ? Parce que la lumière attire les bugs !",
    "Un ordinateur dit à un autre : tu as trop de RAM ? L'autre répond : non, j'en ai juste assez pour me souvenir de toi.",
    "Pourquoi les développeurs aiment-ils le café ? Parce que c'est leur source principale de Java !",
    "Erreur 404 : blague non trouvée 😅"
]

# Commande /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Salut 👋 Bienvenue sur Fun Zone Bot ! Tape /blague pour rire 😄")

# Commande /blague
def blague(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(jokes))

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("blague", blague))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
