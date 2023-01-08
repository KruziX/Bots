from threading import Thread
import logging
import os
from aiogram import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import *

bot = Bot(token='5325183488:AAFMiD29IxXGt3Jf1QxEc9TmyLMtQ5GqzcQ', parse_mode=types.ParseMode.HTML)
keyboard = types.InlineKeyboardMarkup()
dp = Dispatcher(bot)
user = bot.get_me(response)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["📜 Просмотр без спама"]
    buttons2 = ["💻 VERSACE GANG", "👜 Kruz Shop", "⚖ Kruz Quarant"]
    buttons3 = ["📝 Kruz Post", "👨🏻‍💻 Kruz Hacker", "🥝 Kruz Farm"]
    buttons4 = ["🎧 Kruz Music"]
    keyboard.add(*buttons)
    keyboard.add(*buttons2)
    keyboard.add(*buttons3)
    keyboard.add(*buttons4)
    await message.reply("👋", reply_markup=keyboard)
    await message.answer("👋 <b>Приветствую Вас!</b>\n\n🤖 Я Ваш <b>робот-помощник</b>!\n\nℹ Я могу рассказать Вам информацию о любом из проектов от <b>KruzariuM</b>\n\n🔥 Достаточно лишь <b>нажать на кнопку с именем того проекта, которым Вы интересуетесь</b>!\n\n🔗 Вместе с описание проекта я дам Вам <b>ссылку</b> на интересующий Вас проект\n\n💻 Так же Вы можете посмотреть <b>веб-сайт от KruzariuM</b> через меня, используя кнопки ниже!\n\n💡 Если меню с кнопками не появилось, то <b>пропишите /start заново</b>.", reply_markup=h_keyboard)
############################################################################

btn = InlineKeyboardButton("💻 VERSACE GANG", callback_data="cb")
btn2 = InlineKeyboardButton("👜 Kruz Shop", callback_data="cb2")
btn3 = InlineKeyboardButton("⚖ Kruz Quarant", callback_data="cb3")
btn4 = InlineKeyboardButton("📝 Kruz Post", callback_data="cb4")
btn5 = InlineKeyboardButton("👨🏻‍💻 Kruz Hacker", callback_data="cb5")
btn6 = InlineKeyboardButton("🥝 Kruz Farm", callback_data="cb6")
btn7 = InlineKeyboardButton("🎧 Kruz Music", callback_data="cb7")
v = InlineKeyboardButton("🔗 Перейти", url = "https://t.me/VersaceGangBot")
k = InlineKeyboardButton("🔗 Перейти", url = "https://t.me/KruzShopBot")
h = InlineKeyboardButton("1⃣ Страница", web_app=WebAppInfo(url = "https://kruzarium.webu.repl.co"))
h2 = InlineKeyboardButton("Страница 2⃣", web_app=WebAppInfo(url = "https://kruzarium.webu.repl.co/projects.html"))
q = InlineKeyboardButton("🔗 Перейти", url = "https://t.me/KruzQuarantBot")
p = InlineKeyboardButton("🔗 Перейти", url = "https://t.me/KruzPostBot")
hk = InlineKeyboardButton("🔗 Перейти", url = "https://t.me/KruzHackerBot")
f = InlineKeyboardButton("🔗 Перейти", url = "https://t.me/KruzFarmBot")
m = InlineKeyboardButton("🔗 Перейти", url = "https://t.me/KruzMusicBot")

btn_keyboard = InlineKeyboardMarkup(row_width=11).row(btn, btn2, btn3, btn4, btn5, btn6, btn7)
btn_keyboard = InlineKeyboardMarkup().add(btn, btn2, btn3, btn4, btn5, btn6, btn7)

v_keyboard = InlineKeyboardMarkup(row_width=11).row(v)
v_keyboard = InlineKeyboardMarkup().add(v)

k_keyboard = InlineKeyboardMarkup(row_width=11).row(k)
k_keyboard = InlineKeyboardMarkup().add(k)

h_keyboard = InlineKeyboardMarkup(row_width=11).row(h, h2)
h_keyboard = InlineKeyboardMarkup().add(h, h2)

q_keyboard = InlineKeyboardMarkup(row_width=11).row(q)
q_keyboard = InlineKeyboardMarkup().add(q)

p_keyboard = InlineKeyboardMarkup(row_width=11).row(p)
p_keyboard = InlineKeyboardMarkup().add(p)

hk_keyboard = InlineKeyboardMarkup(row_width=11).row(hk)
hk_keyboard = InlineKeyboardMarkup().add(hk)

f_keyboard = InlineKeyboardMarkup(row_width=11).add(f)
f_keyboard = InlineKeyboardMarkup().add(f)

m_keyboard = InlineKeyboardMarkup(row_width=11).add(m)
m_keyboard = InlineKeyboardMarkup().add(m)

@dp.message_handler()
async def any_text_message(message: types.Message):
    if message.text == '📜 Просмотр без спама':
        await bot.send_message(message.from_user.id, f'''
                📖 <b>Доступные</b> проекты:''', parse_mode='HTML', reply_markup=btn_keyboard)

    if message.text == '💻 VERSACE GANG':
            await bot.send_message(message.from_user.id, f'''
                💻 Искал бота со всякими хакерскими штуками? Ты его нашёл!

💟 У нас есть:
👾 Скрипты ботов
😈 Вирусы
🌍 VPN
📱 iOS Программы
😱 И многое другое!
                                   
🔗 <a href="https://t.me/versacegangbot">Перейти в бота</a>''', parse_mode='HTML', reply_markup=v_keyboard)

    if message.text == '👜 Kruz Shop':
            await bot.send_message(message.from_user.id, f'''
                🔥 Искал бота с множеством товара по низким ценам?!
💡 Ты его нашёл!

👉 У нас есть: 👈
[1⃣] Discord Nitro
[2⃣] YouTube Premium
[3⃣] Spotify Premium
[4⃣] Подписки На Онлайн Кинотеатры
[5⃣] QIWI Аккаунты
[6⃣] Верификации
[7⃣] Аккаунты Множества Сервисов
[8⃣] Очень Много Способов
[🔢] И МНОГО ЧЕГО ЕЩЁ!

🎩 Быстрая и эффективная помощь от поддержки!

❤ Понятный и красивый дизайн!

📖 Инструкции и правила!

💎 И всё по одной <a href="https://t.me/KruzShopBot">ссылке</a>!''', parse_mode='HTML', reply_markup=k_keyboard)

    if message.text == '⚖ Kruz Quarant':
            await bot.send_message(message.from_user.id, f'''
                ⚖ Искал проверенного гаранта? Ты его нашёл!

🚀 Мы гарантируем:

💸 Вывод средств
🤝 Честную сделку
📖 Список действительно проверенных продавцов
 💫 И многое другое!

💡 Так же есть инструкция по использованию бота в разделе "Помощь"

🔗 <a href="https://t.me/KruzQuarantBot">Перейти в бота</a>''', parse_mode='HTML', reply_markup=q_keyboard)
      
    if message.text == '📝 Kruz Post':
           await bot.send_message(message.from_user.id, f'''
                📷 Хочешь создавать крутые посты для телеграм каналов и чатов, но не знаешь как?

👌 С нашим ботом это будет очень просто!

😯 У нас есть:

✒ Разметки HTML
🔥 Кнопки
⚙ Удобные настройки
📝 Лёгкое редактирование постов

🌌 Будет достаточно лишь написать "@KruzPostBot" без кавычек и через пробел номер Вашего поста!

🔗 <a href="https://t.me/KruzPostBot">Перейти в бота</a>''', parse_mode='HTML', reply_markup=p_keyboard)
  
    if message.text == '👨🏻‍💻 Kruz Hacker':
            await bot.send_message(message.from_user.id, f'''
                💎 Искал бота для пробивов? Ты его нашёл!

🚀 Мы пробьём по:
🔗 Ссылке на соц-сеть
🔢 Номеру машины
🔢 Номеру телефона
👦 Имени
📬 Почте
👤 Логину
🆔 ID, телеграм аккаунту, пересланному сообщению
👥 Юр. лицам
🔢 ИНН
🌐 IP или домене
📑 Фото
🌍 Геолокации

🎤 Присутствуют голосовые команды!

🔗 <a href="https://t.me/KruzHackerBot">Перейти в бота</a>''', parse_mode='HTML', reply_markup=hk_keyboard)
  
    if message.text == '🥝 Kruz Farm':
           await bot.send_message(message.from_user.id, f'''
                💱 Искал настоящую ферму киви кошельков? Ты нашёл её!
    
🔥 У нас есть:
🚀 Моментальные выводы        
⚙️ Настройки выводов        
💷 Вывод на QIWI и карты        
🆓 Бесплатный доступ        
♻️ Логирование баланса        
🔔 Уведомления о выводах                
🔒 Блокировка после вывода        
🔥 И многое другое!

💰 Наша комиссия всего лишь 3%!

🔗 <a href="https://t.me/KruzHackerBot">Перейти в бота</a>''', parse_mode='HTML', reply_markup=f_keyboard)
                                
    if message.text == '🎧 Kruz Music':
           await bot.send_message(message.from_user.id, f'''
                💿 Музыкальный бот Kruz Music

⌛ Автоматический поиск и скачивание файлов!
📉 Минимум рекламы
💸 Бесплатный поиск без изменений песен
📲 Возможность скачать все найденные песни одновременно!

🔗 <a href="https://t.me/KruzMusicBot">Перейти в бота</a>''', parse_mode='HTML', reply_markup=m_keyboard)
      
    if message.text == '/dice':
           await bot.send_message(message.from_user.id, f'''
😳 Как ты узнал об этой <b>секретной</b> команде?''', parse_mode='HTML')
    if message.text == '/dice':
           await bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAIzUWO6r1rB6u9rRPnfQMBvw-8ZclU-AAJcAANkYXEuySwsmkGqvE4tBA")
    if message.text == '/ping':
           await bot.send_message(message.from_user.id, print(user))
      
@dp.callback_query_handler(lambda c: c.data == "cb")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, "💻 Искал бота со всякими хакерскими штуками? Ты его нашёл!\n\n💟 У нас есть:\n👾 Скрипты ботов\n😈 Вирусы\n🌍 VPN\n📱 iOS Программы\n😱 И многое другое!\n\n\n🔗 @VersaceGangBot", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == "cb2")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, "🚀 Бот для автоматических продаж интернет-подписок.\n\n📉 Самые низкие цены!\n\n😍 Личный подход к клиентам!\n\n💲 Всегда готовы сделать скидку!\n\n✅ Товар всегда в наличии!\n\n🔗 @KruzShopBot", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == "cb3")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, "⚖ Искал проверенного гаранта? Ты его нашёл!\n\n🚀 Мы гарантируем:\n\n💸 Вывод средств\n🤝 Честную сделку\n📖 Список проверенных продавцов\n💫 И многое другое!\n\n💡 Есть инструкции\n\n🔗 @KruzQuarantBot", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == "cb4")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id,"📷 Хочешь делать посты?\n\n👌 С нами это просто!\n\n😯 У нас есть:\n\n✒ Разметки HTML\n🔥 Кнопки\n⚙ Удобные настройки\n📝 Лёгкое редактирование\n\n🌌 Нужно написать @KruzPostBot и номер Вашего поста!\n\n🔗 @KruzPostBot", show_alert=True)
  
@dp.callback_query_handler(lambda c: c.data == "cb5")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, "💎 Искал бота для пробивов?\n\n🚀 Мы найдём по:\n🔗 Соц-сетям\n🔢 Машине\n🔢 Телефону\n👦 Имени\n📬 Почте\n👤 Логину\n🆔 ID, телеграм..\n👥 Юр. лицам\n🔢 ИНН\n🌐 IP или домену\n📑 Фото\n🌍 Гео\n\n🔗 @KruzHackerBot", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == "cb6")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, "💱 Искал QIWI-ферму?\n\n🔥 У нас есть:\n🚀 Быстрые выводы\n⚙️ Настройки\n💷 Вывод на QIWI, карты\n🆓 Всё бесплатно\n♻️ Логи\n🔔 Уведомления\n🔒 Блокировка\n🔥 И многое другое!\n\n💰 Комиссия 3%\n\n🔗 @KruzFarmBot", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == "cb7")
async def test_function(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, "💿 Музыкальный бот Kruz Music\n\n⌛ Авто поиск и скачивание!\n📉 Мало рекламы\n💸 Бесплатный поиск\n📲 Возможность скачать все найденные песни одновременно!\n\n🔗 @KruzMusicBot", show_alert=True)
  ######################################################

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
