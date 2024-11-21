import requests
from datetime import datetime

class TelegramHandler:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{bot_token}"

    def send_message(self, message):
        try:
            url = f"{self.api_url}/sendMessage"
            data = {
                "chat_id": self.chat_id,
                "text": message,
                "parse_mode": "HTML"
            }
            response = requests.post(url, json=data)
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Error sending Telegram message: {e}")
            return False

    def send_alert(self, host, status, previous_status):
        if status == "DOWN":
            emoji = "🔴"
            alert_type = "CẢNH BÁO"
            status_message = "Mất kết nối"
        else:  # UP from DOWN
            emoji = "🟢"
            alert_type = "PHỤC HỒI"
            status_message = "Đã phục hồi kết nối"

        message = (
            f"{emoji} <b>{alert_type}</b>\n"
            f"Tên: {host['name']}\n"
            f"IP/Domain: {host['ip']}\n"
            f"Loại: {host['type']}\n"
            f"Mô tả: {host['description']}\n"
            f"Trạng thái: {status_message}\n"
            f"Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        return self.send_message(message)