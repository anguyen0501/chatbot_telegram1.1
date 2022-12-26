import Constants as keys
import Response as R
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
import json
from Method.News import News
from googletrans import LANGUAGES, Translator
import random


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


def translate_command(update: Update, context: CallbackContext) -> None:
    message = update.message.text
    dest_lang = random.choice(list(LANGUAGES.value()))
    translator = Translator()
    translation = translator.translate(message, dest=dest_lang)
    context.bot.send_message(chat_id=update.effective_chat.id, text=translation.text)


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
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
