<h1 align="center">
    <p>ChatBot Telegram</p>
</h1>
<h3 align="center">Telegram Bot using Python</h3>
<p align="center">
    <strong><a href="README.md">Readme</a></strong>
    •
    <strong><a href="https://ut.edu.vn/">UTH</a></strong>
    •
    <strong><a href="">Facebook</a></strong>
</p>

> Thực hiện: **Nguyễn Thái An** 

> Cập nhật lần cuối: **29/12/2022**

# How does it work? 
## Example:
1. **After opening an account on Telegram, in the search bar at the top search for “BotFather”**
  ![Step 1](https://media.geeksforgeeks.org/wp-content/uploads/20210919190057/Botfather2.JPG)
2. **Click on the ‘BotFather’ (first result) and type /newbot**
  ![Step 2](https://media.geeksforgeeks.org/wp-content/uploads/20210919190352/botfather3.JPG)
3. **Give a unique name to your bot. After naming it, Botfather will ask for its username. Then also give a unique name BUT remember the username of your bot must end with the bot, like my_bot, hellobot etc.**
  ![Step 3](https://media.geeksforgeeks.org/wp-content/uploads/20210919190610/botfather4.JPG)
4. **After giving a unique name and if it gets accepted you will get a message something like this**
  ![Step 4](https://media.geeksforgeeks.org/wp-content/uploads/20210919190816/accesstoken.JPG)

### Requirements
- **A Telegram Account**: If you don’t have the Telegram app installed just download it from the play store or website <strong><a href="https://desktop.telegram.org/">Telegram for Desktop</a></strong>. After downloading create an account using your mobile number just like **Messenger**.
- **.python-telegram-bot** module: Here we will need a module called **python-telegram-bot**, This library provides a pure Python interface for the Telegram Bot API. It’s compatible with Python versions 3.6.8+. In addition to the pure API implementation, this library features a number of high-level classes to make the development of bots easy and straightforward. These classes are contained in the **“telegram.ext”** submodule.
## Integrated development environment (IDE) :
- ### Pycharm
- Link download : <strong><a href="https://www.jetbrains.com/pycharm/">PyCharm</a></strong>
- ### Python :
- Link download : <strong><a href="https://www.python.org/downloads/">PyThon</a></strong>
## Python package manager :
- **Telegram :**
  - Update
     > This will invoke every time a bot receives an update i.e. message or command and will send the user a message.
- **python-telegram-bot :** 
  - Updater
      > This will contain the API key we got from BotFather to specify in which bot we are adding functionalities to using our python code.
  - CommandHandler
      > This Handler class is used to handle any command sent by the user to the bot, a command always starts with “/” i.e “/start”,”/help” etc.
  - MessageHandler
      > This Handler class is used to handle any normal message sent by the user to the bot.
  - CallbackContext
      > We will not use its functionality directly in our code but when we will be adding the dispatcher it is required (and it will work internally)
  - Filters
      > This will filter normal text, commands, images, etc from a sent message.
  - CallbackQueryHandler
      > Handler class to handle Telegram callback queries. Optionally based on a regex
- **json**
> JSON (JavaScript Object Notation): Là một định dạng dữ liệu rất phổ biến, được dùng để lưu trữ và thể hiện các dữ liệu có  cấu trúc.
- **requests**
> Thư viện Requests trong Python giúp lập trình viên có thể thực hiện các tác vụ như gửi request tới server cũng như xử lý response một cách đơn giản.
- **cctx**
- **html**
- **datetime**
# API :
- Telegram API : <strong><a href="https://core.telegram.org/">Telegram API</a></strong>
- Weather API : <strong><a href="http://vi.wttr.in/">Weather wttr.in</a></strong>
- YouTube API : <strong><a href="https://developers.google.com/youtube/v3">YouTube API</a></strong>
# Main function :
  - **Câu hỏi về trường học**
  - **Đọc báo**
  - **Xem thời tiết**
  - **Bức ảnh bất kì**
  - **Tỉ giá BTC**
  - **Dịch ngôn ngữ**
  - **Câu đố [Ví dụ]**
  - **Tìm kiếm Youtube**
