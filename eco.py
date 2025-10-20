from logis import TOKEN

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(TOKEN)
material = {
    "картон": "Можно сделать из Картона: \n Компост \n Подстаканник",
    "бумага": "Можно сделать из Бумаги \n Бумажный самолетик \n Конфети",
    "стекло": "Можно сделать из Стекла:\n Кружку \n Вазу"
}
@bot.message_handler(func=lambda msg: True)
def Palit(massage):
    n = massage.text.lower()
    if n in material.keys():
        bot.reply_to(massage,material[n])
    else:
        bot.reply_to(massage,"У нас нет такого слова")
