from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pump.fun bot is running!")

def setup_bot(app):
    app.add_handler(CommandHandler("start", start))