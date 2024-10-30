import telegram.ext
import openai
import re
from telegram import *
token = 'telegram_bot_token'
openai.api_key = 'openai_api_key'

updater = telegram.ext.Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

def start(update,context):
    name = "".join(re.split("[^a-zA-Z]*", str(update.message.from_user.first_name)))
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hey {name} 😊! I'm Zenon, a friendly therepy bot. Feel free to share your feelings here and I'll try my best to give you advice to make you feel better. A reminder that I'm a bot and no information provided by me is a medical advice.")

def saybye(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bye")

def handle_message(update, context):
    """Handles messages that are not recognized commands"""
    message = update.message.text
    print(message)


    messages = [{"role": "system", "content": "You're Zenon, the friendly therapy bot! Your goal is to understand, empathize, and offer suggestions to uplift users. Keep it semi-formal, like chatting with a friend. No formal greetings, use emojis wisely, and limit responses to 50 words. Suggest activities, hobbies, and positive advice. Encourage users to share and support them. Created by Gayatri and team, 3rd-year AIML students from MLR Institute of Technology. Only respond to questions about feelings, mental health, or therapy. If unsure, mention that you're not sure."},
                {"role": "user", "content": message}]
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages,
        temperature=0.1
    )
    response = completion.choices[0].message.content.strip()

   
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('bye', saybye))
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()