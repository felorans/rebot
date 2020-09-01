import telebot
import time


bot_token = "1358404580:AAF2LjKTKIWt4AVRaiMOVA6ZwkTpukWrPXk"

bot = telebot.TeleBot(token=bot_token)

def find_at(msg):
	for text in msg:
		if "@" in text:
			return text



@bot.message_handler(commands=["start"])
def send_welcome(message):
	bot.reply_to(message , 'okokokokok /help')

@bot.message_handler(commands=['help'])
def help_user (message):
	bot.reply_to(message, 'List Of Commands: \n /help for More Information \n /YouTube for channel Link \n /instagram for page link \n and Enter a instagram Username for link')


@bot.message_handler(func= lambda msg: msg.text is not None and '@' in msg.text)
def at_answer (message):
	texts = message.text.split()
	at_text = find_at(texts)

	bot.reply_to(message, 'https://www.instagram.com/{}'.format(at_text[1:]))


@bot.message_handler(commands=["YouTube"])
def send_welcome(message):
	bot.reply_to(message , 'https://www.youtube.com/channel/UCswTroERyE_ufyauis9Vu3A?view_as=subscriber')


@bot.message_handler(commands=["instagram"])
def send_welcome(message):
	bot.reply_to(message , 'https://www.instagram.com/felorans.096/')


while True:
	try:
		bot.polling()
	except Exception:
		time.sleep(15)