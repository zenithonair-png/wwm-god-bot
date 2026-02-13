from telegram import Update
from telegram.ext import ContextTypes

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "creator":
        await query.edit_message_text("🎮 Creator Engine Loading...")

    elif query.data == "ai":
        await query.edit_message_text("🤖 AI Brain Online...")

    elif query.data == "profile":
        await query.edit_message_text("🏆 Profile System Loading...")
