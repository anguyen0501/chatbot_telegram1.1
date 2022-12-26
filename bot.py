import googletrans

import Constants as keys
import Response as R
from telegram import Update, ReplyKeyboardMarkup, bot
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters, CallbackQueryHandler
import json
import telegram
from Method.News import News
from googletrans import LANGUAGES, Translator
import random
import requests
import ccxt

print("Bot Starting....")


def start_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Chào {update.effective_user.first_name}')


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Bạn muốn tôi giúp gì? \n 1. Đọc báo -> /news <số lượng>")


def news_command(update: Update, context: CallbackContext):
    try:
        limit_news = int(context.args[0])  # Lấy tham số từ input truyền vào -> cào về bao nhiêu tin
        news = News.GetNews(limit_news)
        for x in range(0, len(news)):  # Deserialize dữ liệu json trả về từ file News.py lúc nãy
            message = json.loads(news[x])
            update.message.reply_text(message['title'] + "\n"
                                      + message['link'] + "\n" + message['description'])
    except (IndexError, ValueError):
        update.message.reply_text('Vui lòng chọn số lượng tin hiển thị!!')


def photo_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_photo("https://picsum.photos/200")


def file_command(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    file = open('filetxt', 'rb')
    context.bot.send_document(chat_id, file)


def translate_command(update, context) -> None:
    message = update.message.text
    dest_lang = random.choice(list(LANGUAGES.values()))
    translator = Translator()
    translation = translator.translate(message, dest=dest_lang)
    context.bot.send_message(chat_id=update.effective_chat.id, text=translation.text)


# Define the correct answer and the options
correct_answer = "Paris"
options = ["Paris", "Berlin", "Rome", "London"]


# Define a function to handle the button press
def button_press(update, context):
    # Get the callback data
    data = update.callback_query.data

    # Extract the option number from the callback data
    option = int(data.split("_")[1])

    # Get the chat ID of the conversation
    chat_id = update.effective_chat.id

    # Check if the answer is correct
    if options[option] == correct_answer:
        context.bot.send_message(chat_id=chat_id, text="Correct guess!")
    else:
        context.bot.send_message(chat_id=chat_id, text="Wrong guess.")


# Define a function to handle the /ask_question command
def ask_question(update, context):
    # Get the chat ID of the conversation
    chat_id = update.effective_chat.id

    # Generate a question
    question = "What is the capital of France?"

    # Create buttons for each option
    buttons = []
    for i, option in enumerate(options):
        button = telegram.InlineKeyboardButton(option, callback_data=f"option_{i}")
        buttons.append([button])

    # Create a keyboard with the buttons
    keyboard = telegram.InlineKeyboardMarkup(buttons)

    # Send the question and keyboard to the user
    context.bot.send_message(chat_id=chat_id, text=question, reply_markup=keyboard)


def imgRandom_command(update, context):
    # Make a request to the random image API
    response = requests.get("https://source.unsplash.com/random")
    # Send the image to the user
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=response.content)


client = ccxt.binance()


def price_command(update, context):
    # Get the BTC/USDT market data from Binance
    market = client.fetch_ticker("BTC/USDT")

    # Extract the BTC price from the market data
    price = market["last"]

    # Send the BTC price to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Giá hiện tại của Bitcoin là ${price:.2f}.")


def weather_command(update, context):
    # Get the chat ID of the conversation
    chat_id = update.effective_chat.id

    # Make a request to the wttr.in API
    response = requests.get("http://wttr.in/Ho Chi Minh City?format=%C\n%T\n%w\n%t")

    # Translate the weather information to Vietnamese
    translator = googletrans.Translator()
    vietnamese_text = translator.translate(response.text, dest="vi").text

    # Send the weather information to the user
    context.bot.send_message(chat_id=chat_id, text=vietnamese_text)


def export_history(update, context):
    # Get the chat ID of the conversation
    chat_id = update.effective_chat.id

    # Get the history of messages in the conversation
    history = update.messages.getHistory

    # Save the history to a file
    with open("history.json", "w") as f:
        json.dump(history, f)


def handle_message(update: Update, context: CallbackContext):
    text = str(update.message.text).lower()
    response = R.sample_response(text)
    update.message.reply_text(response)


# Function dùng để xác định lỗi gì khi có thông báo lỗi
def error(update: Update, context: CallbackContext):
    print(f"Update {update} cause error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("news", news_command))
    dp.add_handler(CommandHandler("image", photo_command))
    dp.add_handler(CommandHandler("send", file_command))
    dp.add_handler(CommandHandler("translate", translate_command))
    dp.add_handler(CommandHandler("imagee", imgRandom_command))
    dp.add_handler(CommandHandler("price", price_command))
    dp.add_handler(CommandHandler("weather", weather_command))
    dp.add_handler(CommandHandler("save", export_history))
    dp.add_handler(CallbackQueryHandler(button_press))
    dp.add_handler(CommandHandler("ask1", ask_question))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    updater.idle()


main()
