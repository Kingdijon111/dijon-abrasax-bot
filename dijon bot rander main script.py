
# GainzAlgo Premium Telegram Bot - Render Deployment Version

import json
from datetime import datetime, timedelta
from telegram import Update, Bot, ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

DATA_FILE = "users.json"
try:
    with open(DATA_FILE, "r") as f:
        users = json.load(f)
except:
    users = {}

def save_users():
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    if user_id in users and users[user_id]["active"]:
        await update.message.reply_text("You're subscribed and receiving signals!")
    else:
        msg = "**Welcome to GainzAlgo Premium!**\n\n" +               "Pay via:\n" +               "- PayPal: galaxydijon2@gmail.com\n" +               "- Payoneer: galaxydijon22gmail.com\n" +               "- BTC: 1LgLmsfMSCdKwe8AP2u2SKZuwGoafXHVnR\n" +               "- ETH: 0x0909d8a64124af620e27fc8b371406a420c0e67f\n" +               "- USDT: TUghcHZR4FmhhjcuRvuEwn9MBqSSMbTc6x\n" +               "- BNB: 0x0909d8a64124af620e27fc8b371406a420c0e67f\n" +               "Then message @your_admin_username for activation."
        await update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)

async def grant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.username != "your_admin_username":
        return
    try:
        user_id = context.args[0]
        days = int(context.args[1])
        users[user_id] = {"active": True, "expires": (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")}
        save_users()
        await update.message.reply_text(f"✅ Access granted to {user_id} for {days} days.")
    except:
        await update.message.reply_text("Usage: /grant user_id days")

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.username != "@Kingdijon999":
        return
    try:
        user_id = context.args[0]
        if user_id in users:
            users[user_id]["active"] = False
            save_users()
            await update.message.reply_text(f"❌ User {user_id} banned.")
    except:
        await update.message.reply_text("Usage: /ban user_id")

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.username != "@Kingdijon999":
        return
    msg = " ".join(context.args)
    count = 0
    for uid, info in users.items():
        if info.get("active"):
            try:
                await context.bot.send_message(chat_id=int(uid), text=msg)
                count += 1
            except: continue
    await update.message.reply_text(f"Broadcast sent to {count} users.")

def main():
    app = ApplicationBuilder().token("7508697234:AAE3aLCVhqfleiOjFaw04Q0ZCXdtt2e2E9w").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("grant", grant))
    app.add_handler(CommandHandler("ban", ban))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.run_polling()

if __name__ == "__main__":
    main()
