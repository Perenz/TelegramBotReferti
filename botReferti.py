import telebot
import random
from datetime import datetime
import locale
import pandas as pd

locale.setlocale(category=locale.LC_ALL, locale="Italian")


# Reads games and clean
games = pd.read_excel('games.xlsx')
games['DATA'] = pd.to_datetime(games['DATA'], format='%A %d %B %Y')
now = datetime.now().date()
games = games[games['CASA'] == 'B.C. GARDOLO 2000']
games = games[games['DATA']>now]


print(now)
games = games.reset_index(drop=True)
print(games.head())


print(games.iloc[0]['CAMP.'] + '\n'+ games.iloc[0]['DATA'].strftime("%x")  +'\n' + games.iloc[0]['ORA'] +  '\n' + games.iloc[0]['FUORI'])

#Convert to common comparable dates
objDate = datetime.strptime("venerdì 25 ottobre 2019", "%A %d %B %Y")
print(objDate)

bot = telebot.TeleBot("712533036:AAFf0sO-_jeStnBqIu3NPv1TwYl2MmUIqGk ")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    response = "Prossime 5 partite:\n"
    k=1
    for i, g in games.head(n=5).iterrows():
        response += str(k) + ":\n" + g['CAMP.'] + '\n' + g['DATA'].strftime("%A %x") + '\n' + g['ORA'] +  '\n' + g['FUORI'] + "\n\n"
        k += 1
    
    bot.reply_to(message, response)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, random.choice(['Perenzoni','Claus','Dellai']))

bot.polling()
