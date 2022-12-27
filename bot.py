import Constants as keys
import Response as R
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters, CallbackQueryHandler
import json
import telegram
from Method.News import News
import googletrans
import requests
import ccxt
import html
import datetime

print("Bot Starting....")


def start_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Xin chào {update.effective_user.first_name}, đây là bot chat tự động, vui lòng /help '
                              f'để được giúp đỡ !!!')


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Bạn muốn tôi giúp gì? "
                              "\n 1. Đọc báo -> /news <số lượng>"
                              "\n 2. Xem thời tiết -> /weather <location>"
                              "\n 3. Bức ảnh bất kì -> /imagee"
                              "\n 4. Xem giá BTC -> /price"
                              "\n 4. Dịch ngôn ngữ -> /translate"
                              "\n 5. Câu đố -> /ask1")


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


bot = telegram.Bot(token=keys.API_KEY)


def translate_command(update, context) -> None:
    # Get the chat ID of the conversation
    chat_id = update.effective_chat.id

    # Get the source language and target language from the command arguments
    src_lang = context.args[0]
    dest_lang = context.args[1]

    # Get the text to be translated from the command arguments
    text = " ".join(context.args[2:])

    # Translate the text
    translator = googletrans.Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text

    # Send the translated text to the user
    bot.send_message(chat_id=chat_id, text=translated_text)


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
    # Get the location from the command arguments
    location = " ".join(context.args)
    # Make a request to the wttr.in API
    response = requests.get(f"http://vi.wttr.in/{location}?format=%l\n%C\n%T%m\n%w\n%t%c")

    # Send the weather information to the user
    context.bot.send_message(chat_id=chat_id, text=response.text)


def handle_message(update: Update, context: CallbackContext):
    text = str(update.message.text).lower()
    response = R.sample_response(text)
    update.message.reply_text(response)
    # Get the message object
    message = update.message

    # Get the chat ID of the conversation
    chat_id = message.chat_id

    # Get the message text, sender's username, and current time
    text = message.text
    username = message.from_user.username
    now = datetime.datetime.now()

    # Write the message to an HTML file
    with open("chat_history.html", "a", encoding='utf-8') as html_file:
        html_file.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>Save History Chatbot '
                        'Telegram</title>\n</head>\n<body>\n')
        html_file.write(
            f"<p><b>{html.escape(username)}</b> ({now.strftime('%Y-%m-%d %H:%M:%S')}): {html.escape(text)} </p>\n"
            f"</body>\n")


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
    dp.add_handler(CommandHandler("imagee", imgRandom_command))
    dp.add_handler(CommandHandler("price", price_command))
    dp.add_handler(CommandHandler("weather", weather_command))
    dp.add_handler(CallbackQueryHandler(button_press))
    dp.add_handler(CommandHandler("ask", ask_question))
    dp.add_handler(CommandHandler('translate', translate_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    updater.idle()


main()
