import telebot

Token = "5676009389:AAFwvf4gUi53q886sGl-SnhGjE6xOWK_8zU"

bot =telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the silicon bot \n""Developed by HPDJOY""\n\n/logout  logout from system\n /first_year ")

@bot.message_handler(commands=['first_year'])
def first_year(message):
 bot.reply_to(message,"https://drive.google.com/drive/u/3/folders/1gaUT2tERY39mFuGybEpHalM0Fg7VU5aq")
    
@bot.message_handler(commands=['logout'])
def logout(message):
 bot.reply_to(message,"thank you..")
bot.polling()

