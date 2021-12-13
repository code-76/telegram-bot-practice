import logging
from telegram import Update, chat
from telegram.bot import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram.ext.inlinequeryhandler import InlineQueryHandler
from telegram.inline.inlinequeryresultarticle import InlineQueryResultArticle
from telegram.inline.inputcontactmessagecontent import InputContactMessageContent

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token='5053367584:AAGDKRtPHNnc-Z-Ljy_kBmaxtI_8mnmIcF8')
updater = Updater(bot=bot, use_context=True)
dispatcher = updater.dispatcher

def hello(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'support inline mode is {bot.supports_inline_queries}')

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper() 
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def inline_caps(update: Update, context: CallbackContext):
    query = update.inline_query.query
    if query == "":
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputContactMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

# add a command to interact with the user, so they can enter "/hello" with the channel
hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

# add handler to reactive when user input a word
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler("caps", caps)
dispatcher.add_handler(caps_handler)

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

# interval to update the mssage with Telegram Channel
updater.start_polling()
updater.idle()