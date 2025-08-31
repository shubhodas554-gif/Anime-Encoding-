from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from AutoAnimeBot import app
from pyrogram import filters
from AutoAnimeBot.modules.db import is_voted, save_vote
from AutoAnimeBot.core.log import LOGGER

logger = LOGGER("Vote")

def get_vote_buttons(a,b,c):
    buttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(text=f"👍 {a}", callback_data="vote1"),
            InlineKeyboardButton(text=f"♥️ {b}", callback_data="vote2"),
            InlineKeyboardButton(text=f"👎 {c}", callback_data="vote3")
        ]]
    )
    return buttons

def strip_int(x):
    return "".join([i for i in x if i.isnumeric()])

def button_formatter(buttons):
    x = str(buttons)
    y = []
    x.replace("♥️","").replace("👍","").replace("'👎","")
    for i in range(3):
        a = x.find("text")
        z = x[a+9:]
        b = z.find('"')
        z = z[:b]
        y.append(strip_int(z.strip()))
        x = x[a+b+10:]
    return y

@app.on_callback_query(filters.regex("vote"))
async def votes_(_, query: CallbackQuery):
    try:
        id = query.message.id
        user = query.from_user.id
        vote = int(query.data.replace("vote","").strip())
        if await is_voted(id,user):
            return await query.answer("You Have Already Voted... You Can't Vote Again")
        await query.answer()
        x = query.message.reply_markup
        a,b,c = button_formatter(x)
        a = int(a) if a else 0
        b = int(b) if b else 0
        c = int(c) if c else 0
        if vote == 1: a +=1
        elif vote == 2: b +=1
        elif vote == 3: c +=1
        buttons = get_vote_buttons(a,b,c)
        await query.message.edit_reply_markup(reply_markup=buttons)
        await save_vote(id,user)
    except Exception as e:
        logger.warning(str(e))
