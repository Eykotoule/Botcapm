from keep_alive import keep_alive
keep_alive()

from telegram.ext import ApplicationBuilder
from bot import setup_bot

import os

TOKEN = os.getenv("BOT_TOKEN") or "8041985955:AAGNPL_dWWWI5AWlYFue5NxkNOXsYqBOmiw"

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    setup_bot(app)
    app.run_polling()