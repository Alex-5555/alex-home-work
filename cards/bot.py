'''
Done! Congratulations on your new bot. 
You will find it at t.me/dima_alex_bot. 
You can now add a description, 
about section and profile picture for your bot
, see /help for a list of commands. 
By the way, when you've finished 
creating your cool bot, ping our Bot 
Support if you want a better username for it. 
Just make sure the bot is fully operational 
before you do this.

Use this token to access the HTTP API:
5421316348:AAGTF48XjwyB1TAushbQhVY-JTrFAmZPmyI
Keep your token secure and store it safely, 
it can be used by anyone to control your bot.

For a description of the Bot API, see this page:
 https://core.telegram.org/bots/api

'''
import telebot
bot = telebot.TeleBot('5421316348:AAGTF48XjwyB1TAushbQhVY-JTrFAmZPmyI')
print('Bot started....')

@bot.message_handler()
def start_message(message):
    print(message)

bot.polling()