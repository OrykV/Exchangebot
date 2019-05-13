from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, RegexHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Bot
from logic import *


# check for new messages
updater = Updater(token="")

# allows to register handler
dispatcher = updater.dispatcher


# define a command callback function
def start(bot, update):
    kb = [[KeyboardButton('	🇺🇸 Долар США'), KeyboardButton('🇪🇺 Евро'), KeyboardButton('🇵🇱 Злотий')]]
    kb_markup = ReplyKeyboardMarkup(kb,
                                    resize_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id,
                     text='Вас вітає бот. Оберіть валюту для здійснення операцій!',
                     reply_markup=kb_markup)


def usd(bot, update):
    startf()
    b = 0
    a = 1
    bid = bid_compare(b)
    ask = ask_compare(a)
    button = [
        [InlineKeyboardButton("Найвигідніше здати", callback_data=bid)],
        [InlineKeyboardButton("Найвигідніше купити", callback_data=ask)],
        [InlineKeyboardButton("Goverla", callback_data=f'\nGoverla: купівля - {gvrl_result[b]}, продаж - {gvrl_result[a]}.'),
         InlineKeyboardButton("West Finance", callback_data=f'\nWest Fianance: купівля - {west_result[b]}, продаж - {west_result[a]}.'),
         InlineKeyboardButton("Niko Lutsk", callback_data=f'\nNiko Lutsk: купівля - {niko_result[b]}, продаж - {niko_result[a]}.')]
    ]
    reply_markup = InlineKeyboardMarkup(button)
    bot.send_message(chat_id=update.message.chat_id,
                     text="Виберіть необхідний пошук:",
                     reply_markup=reply_markup)


def eur(bot, update):
    startf()
    b = 2
    a = 3
    bid = bid_compare(b)
    ask = ask_compare(a)
    button = [
        [InlineKeyboardButton("Найвигідніше здати", callback_data=bid)],
        [InlineKeyboardButton("Найвигідніше купити", callback_data=ask)],
        [InlineKeyboardButton("Goverla", callback_data=f'\nGoverla: купівля - {gvrl_result[b]}, продаж - {gvrl_result[a]}.'),
         InlineKeyboardButton("West Finance", callback_data=f'\nWest Fianance: купівля - {west_result[b]}, продаж - {west_result[a]}.'),
         InlineKeyboardButton("Niko Lutsk", callback_data=f'\nNiko Lutsk: купівля - {niko_result[b]}, продаж - {niko_result[a]}.')]
    ]
    reply_markup = InlineKeyboardMarkup(button)

    bot.send_message(chat_id=update.message.chat_id,
                     text="Виберіть необхідний пошук:",
                     reply_markup=reply_markup)


def pln(bot, update):
    startf()
    b = 4
    a = 5
    bid = bid_compare(b)
    ask = ask_compare(a)
    button = [
        [InlineKeyboardButton("Найвигідніше здати", callback_data=bid)],
        [InlineKeyboardButton("Найвигідніше купити", callback_data=ask)],
        [InlineKeyboardButton("Goverla", callback_data=f'\nGoverla: купівля - {gvrl_result[b]}, продаж - {gvrl_result[a]}.'),
         InlineKeyboardButton("West Finance", callback_data=f'\nWest Fianance: купівля - {west_result[b]}, продаж - {west_result[a]}.'),
         InlineKeyboardButton("Niko Lutsk", callback_data=f'\nNiko Lutsk: купівля - {niko_result[b]}, продаж - {niko_result[a]}.')]
    ]
    reply_markup = InlineKeyboardMarkup(button)

    bot.send_message(chat_id=update.message.chat_id,
                     text="Виберіть необхідний пошук:",
                     reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          text=query.data,
                          message_id=query.message.message_id)


# create a command handler
start_handler = CommandHandler("start", start)
usd_handler = CommandHandler("USD", usd)
eur_handler = CommandHandler("EUR", eur)
pln_handler = CommandHandler("PLN", pln)
reg_handler_usd = RegexHandler('🇺🇸 Долар США', usd)
reg_handler_eur = RegexHandler('🇪🇺 Евро', eur)
reg_handler_pln = RegexHandler('🇵🇱 Злотий', pln)
button_handler = CallbackQueryHandler(button)


# add command handler to dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(usd_handler)
dispatcher.add_handler(eur_handler)
dispatcher.add_handler(pln_handler)
dispatcher.add_handler(reg_handler_usd)
dispatcher.add_handler(reg_handler_eur)
dispatcher.add_handler(reg_handler_pln)
dispatcher.add_handler(button_handler)


updater.start_polling()














