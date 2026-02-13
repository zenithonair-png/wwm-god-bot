from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎮 Creator Engine", callback_data="creator")],
        [InlineKeyboardButton("🤖 AI Brain", callback_data="ai")],
        [InlineKeyboardButton("🏆 Profile", callback_data="profile")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🚀 WWM CREATOR 2100 CONTROL PANEL",
        reply_markup=reply_markup,
    )
