import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import sqlite3

# Connect to the database
conn = sqlite3.connect('dating_bot.db')
c = conn.cursor()

# Create the 'profiles' table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS profiles
             (user_id INTEGER PRIMARY KEY, name TEXT, city TEXT, age INTEGER, picture TEXT, sex TEXT)''')

# Initialize the Telegram bot
bot = telegram.Bot(token='YOUR_BOT_TOKEN')

# Handle the '/start' command
def start(update, context):
    update.message.reply_text("Welcome to the dating bot! To create a profile, please enter your name:")
    return "NAME"

# Handle the user's name input
def name(update, context):
    name = update.message.text
    context.user_data['name'] = name
    update.message.reply_text("Thanks! Please enter your city:")
    return "CITY"

# Handle the user's city input
def city(update, context):
    city = update.message.text
    context.user_data['city'] = city
    update.message.reply_text("Thanks! Please enter your age:")
    return "AGE"

# Handle the user's age input
def age(update, context):
    age = int(update.message.text)
    context.user_data['age'] = age
    update.message.reply_text("Thanks! Please send a picture of yourself:")
    return "PICTURE"

# Handle the user's picture input
def picture(update, context):
    picture = update.message.photo[-1].get_file()
    picture.download('user_picture.jpg')
    context.user_data['picture'] = 'user_picture.jpg'
    update.message.reply_text("Thanks! Please enter your sex (M/F):")
    return "SEX"

# Handle the user's sex input
def sex(update, context):
    sex = update.message.text
    context.user_data['sex'] = sex
    user_id = update.message.from_user.id
    name = context.user_data['name']
    city = context.user_data['city']
    age = context.user_data['age']
    picture = context.user_data['picture']
    sex = context.user_data['sex']
    c.execute("INSERT INTO profiles VALUES (?,?,?,?,?,?)", (user_id, name, city, age, picture, sex))
    conn.commit()
    update.message.reply_text("Thanks! You have successfully created your profile!")
    return ConversationHandler.END

# Create the ConversationHandler
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        "NAME": [MessageHandler(Filters.text, name)],
        "CITY": [MessageHandler(Filters.text, city)],
        "AGE": [MessageHandler(Filters.text, age)],
        "PICTURE": [MessageHandler(Filters.photo, picture)],
        "SEX": [MessageHandler(Filters.text, sex)]
    },
    fallbacks=[]
)

# Add the ConversationHandler to the dispatcher
dispatcher.add_handler(conv_handler)
