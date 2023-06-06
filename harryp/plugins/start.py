from .. import bot, openai_key
from telethon import events 
import asyncio
import openai

openai.my_api_key = openai_key

@bot.on(events.NewMessage(incoming = True, pattern = "/start"))
async def start(event):
  await event.reply("Hello This is Harryp Bot")



  
@bot.on(events.NewMessage(incoming = True, pattern = "/get"))
async def start(event):
  a=await event.reply("Hello This is Get command")
  await asyncio.sleep(3)
  await a.edit("This is edited message")
  
    

@bot.on(events.NewMessage(incoming = True, pattern = "/eval"))
async def start(event):
  await event.reply("Hello This is Eval command")
  