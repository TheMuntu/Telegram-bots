import logging
import pyqrcode

from telegram import Update, Bot, Message, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace this with your own Telegram bot token
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Create a handler for the /scan command
def scan(bot: Bot, update: Update):
    update.message.reply_text("Please send me the QR code that you want to scan.")

# Create a handler for QR code messages
def qr_code(bot: Bot, update: Update):
    # Send a "typing" action to indicate that the bot is processing the message
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    # Decode the QR code and get its content
    qr = pyqrcode.QRCode(update.message.photo[-1].get_file().download_as_bytearray())
    content = qr.data.decode('utf-8')
    # Send the content back to the user
    update.message.reply_text(f"The QR code contains the following information: {content}")

# Create the Updater and pass it the bot's token
updater = Updater(TELEGRAM_TOKEN)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Add the handlers to the dispatcher
dispatcher.add_handler(CommandHandler('scan', scan))
dispatcher.add_handler(MessageHandler(Filters.photo, qr_code))

# Start the bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process is interrupted
updater.idle()
