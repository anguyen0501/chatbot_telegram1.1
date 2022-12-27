from datetime import datetime


def sample_response(input):
    user_mess = str(input).lower()

    if user_mess in ("hi", "hello", "ok"):
        return "Chào bạn, tôi có thể giúp gì cho bạn không?"
    if user_mess in ("time", "time?"):
        now = "Hôm nay là: " + datetime.now().strftime("%d-%m-%y, %H:%M:%S")
        return str(now)
    if user_mess in "bye":
        return "Tạm biệt, hẹn gặp lại nhé!"

    return "Lệnh sai rồi, vui lòng kiểm tra lại!"
