import telebot;
bot = telebot.TeleBot('1337818658:AAHxgDQ4clbnp0jZnIi9Vqdt1LWkm31lqcg');

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, "напиши /help")
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    bot.send_message(message.from_user.id, "Пока!")

@bot.message_handler(commands=['summ'])
def get_a(message):
    global b;
    b = message.text;
    bot.send_message(message.from_user.id, "Введите первое число для суммы");
    bot.register_next_step_handler(message, get_b);
def get_b(message):
    global c
    c = message.text;
    bot.send_message(message.from_user.id, "Введите второе число для суммы");
    bot.register_next_step_handler(message, summa);
def summa(message):
    global a;
    a = b + c;
    bot.send_message(message.from_user.id, a);

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет или /repeat или /summ")
    elif message.text == "/repeat":
        bot.send_message(message.chat.id, message.text)
    #elif message.text == "/summ":
    #    a=2+1
    #    bot.send_message(message.chat.id, a)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)
