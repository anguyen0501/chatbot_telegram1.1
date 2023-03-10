import Constants as keys
import Response as R
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters, CallbackQueryHandler
import json
import telegram
from Method.News import News
import googletrans
import requests
import ccxt
import html
import datetime
from Method.Youtube.Youtube import search_youtube

print("Bot Starting....")


# Tạo command /start
def start_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Xin chào {update.effective_user.first_name}, đây là bot chat tự động phiên bản đầu '
                              f'tiên, vui lòng /help '
                              f'để được giúp đỡ !!! Xin cảm ơn')


# Tạo command /help
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("\n 1. Đọc báo -> /news <số lượng>"
                              "\n 2. Xem thời tiết -> /weather <location>"
                              "\n 3. Bức ảnh bất kì -> /imagee"
                              "\n 4. Xem giá BTC -> /price"
                              "\n 5. Hỏi câu hỏi về trường -> nhập câu hỏi bạn muốn hỏi"
                              "\n 6. Câu đố -> /ask1"
                              "\n 7. Xem youtube -> /youtube [tên muốn tìm]"
                              "\n 8. Thông báo thời gian -> time"
                              "\n 9. Gửi file -> /send_file"
                              "\n 10. Gửi mp3 -> /send_audio"
                              "\n 11. Gửi video -> /send_video")


# Tạo hàm tin tức
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


# Tạo command gửi file
def file_command(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    file = open('filetxt', 'rb')
    context.bot.send_document(chat_id, file)


# Tạo command gửi audio
def audio_command(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    context.bot.send_audio(chat_id=chat_id, audio=open('Mp3_File/audio.mp3', 'rb'))


# Tạo command gửi video
def video_command(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    context.bot.send_video(chat_id=chat_id, video=open('Video_File/video.mp4', 'rb'))


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


# Tạo câu trắc nghiệm
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


# Tạo câu trắc nghiệm
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


# Tạo ảnh random từ trang web unsplash
def imgRandom_command(update, context):
    # Make a request to the random image API
    response = requests.get("https://source.unsplash.com/random")
    # Send the image to the user
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=response.content)


# Tạo command gửi giá BTC từ web binance
client = ccxt.binance()


def price_command(update, context):
    # Get the BTC/USDT market data from Binance
    market = client.fetch_ticker("BTC/USDT")

    # Extract the BTC price from the market data
    price = market["last"]

    # Send the BTC price to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Giá hiện tại của Bitcoin là ${price:.2f}.")


# Tạo command gửi thời tiết cập nhật liên tục
def weather_command(update, context):
    # Get the chat ID of the conversation
    chat_id = update.effective_chat.id
    # Get the location from the command arguments
    location = " ".join(context.args)
    # Make a request to the wttr.in API
    response = requests.get(f"http://vi.wttr.in/{location}?format=%l\n%C\n%T%m\n%w\n%t%c")

    # Send the weather information to the user
    context.bot.send_message(chat_id=chat_id, text=response.text)


# Use the `search_youtube` function to search for and retrieve a link to a YouTube video
def youtube_command(update, context):
    # Extract the search query from the command
    query = update.message.text.split(" ", 1)[1]

    # Search for the video and send the link to the user
    link = search_youtube(query)
    bot.send_message(chat_id=update.message.chat_id, text=link)


def facebook_command(update: telegram.Update, context: CallbackContext):
    bot.send_message(chat_id=update.message.chat_id, text="An Nguyễn : "
                                                          "https://www.facebook.com/ankronee/\n"
                                                          "Nguyễn Bình Trọng : https://www.facebook.com/Btrong1\n"
                                                          "Nguyễn Trường Vinh : https://www.facebook.com/profile.php"
                                                          "?id=100011912614150\n "
                                                          "Nguyễn Văn Thơ : https://www.facebook.com/Ther.Nguyen0106\n")


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
        html_file.write('<head>\n<meta charset="UTF-8">\n<title>Save History Chatbot '
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
    dp.add_handler(CommandHandler("send_file", file_command))
    dp.add_handler(CommandHandler("send_audio", audio_command))
    dp.add_handler(CommandHandler("send_video", video_command))
    dp.add_handler(CommandHandler("imagee", imgRandom_command))
    dp.add_handler(CommandHandler("price", price_command))
    dp.add_handler(CommandHandler("weather", weather_command))
    dp.add_handler(CallbackQueryHandler(button_press))
    dp.add_handler(CommandHandler("ask", ask_question))
    dp.add_handler(CommandHandler('translate', translate_command))
    dp.add_handler(CommandHandler("youtube", youtube_command))
    dp.add_handler(CommandHandler('fb', facebook_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    updater.idle()


main()
