# pc_client.py
import os
import time
import pyautogui
import webbrowser
import subprocess
from telegram import Bot

TOKEN = os.getenv("8742372301:AAEMNeh8TjCNqEePNw9sVuwbEAI_KxVc800")      # тот же токен
CHAT_ID = os.getenv("MY_CHAT_ID")   # твой Telegram chat_id

bot = Bot(TOKEN)
last_command = None

def main():
    global last_command
    while True:
        updates = bot.get_updates()
        for u in updates:
            if u.message and u.message.text:
                text = u.message.text.lower()
                if text != last_command:
                    last_command = text

                    if text == "photo":
                        screenshot_path = "screenshot.png"
                        pyautogui.screenshot().save(screenshot_path)
                        with open(screenshot_path, "rb") as f:
                            bot.send_photo(chat_id=CHAT_ID, photo=f)

                    elif text == "open_site":
                        webbrowser.open("https://example.com")
                        bot.send_message(chat_id=CHAT_ID, text="🌐 Сайт открыт!")

                    elif text == "run_program":
                        subprocess.Popen(["notepad.exe"])  # пример: открыть Блокнот
                        bot.send_message(chat_id=CHAT_ID, text="💻 Программа запущена!")

        time.sleep(2)

if __name__ == "__main__":

    main()
