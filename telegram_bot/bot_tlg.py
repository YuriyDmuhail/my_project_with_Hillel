import requests

TELEGRAM_BOT_TOKEN= "7639216997:AAFaTgFinXBcT0fhgkRgLl_Qt7XfLjMQxh8"
TELEGRAM_CHAT_ID = "454288618"
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"❌ Ошибка отправки в Telegram: {e}")