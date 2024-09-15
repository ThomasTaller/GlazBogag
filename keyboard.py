import telebot 
from telebot import types

import config

button_1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

commands = types.KeyboardButton("🆘 Команды")
manual = types.KeyboardButton("📓 Руководство")
myaccount = types.KeyboardButton("👤 Мой аккаунт")
about = types.KeyboardButton("👁 О сервисе")

button_1.row(commands, manual)
button_1.row(myaccount, about)

inline_manual = types.InlineKeyboardMarkup()
download_link = types.InlineKeyboardButton(text="📎 Скачать PDF (5.2MB)", url="https://eog.pw/uploads/Руководство Глаз Бога 2024.pdf")
inline_manual.add(download_link)

inline_about = types.InlineKeyboardMarkup()
off_link = types.InlineKeyboardButton(text="🌍 Оффицеальный телегам канал", url="https://t.me/HalypostGames/")

inline_buy = types.InlineKeyboardMarkup()
buy = types.InlineKeyboardButton(text='Купить', callback_data='buying')
inline_buy.add(buy)