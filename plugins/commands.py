from pyrogram import Client, filters, idle
import pyrogram
from pyrogram.errors import FloodWait
from helper.ban import BanChek
from helper.motor_db import db
from helper.utils import not_subscribed
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from helper.database import insert, getid
from variables import STAT_STICK, PICS, ADMIN, DELAY, LOG_CHANNEL, LOG_TEXT, B_TEXT
from plugins.logo_maker import generate_logo
import asyncio
import random
import time

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**Sorry bro,You didn't Joined Our Updates Channel Join now and start againπ**",
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton(text="π’πΉπππ πΌπ’ ππππππ π²πππππππ’", url=client.invitelink)
           ],[
           InlineKeyboardButton("π πππ’ π°ππππ π", url=f"https://t.me/{client.username}?start=start")            
           ]]
           )
       )

@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
       kikked = await BanChek(bot, message)
       if kikked == 400:
           return
       insert(int(message.chat.id))
       await message.reply_chat_action("Typing")    
       m=await message.reply_sticker(STAT_STICK)
       await asyncio.sleep(DELAY)
       await m.delete()             
       await message.reply_photo(
           photo=random.choice(PICS),
           caption=f"Hello {message.from_user.mention}ππ»\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\nβ send channel last message with forwerd tag to get the channel id π―",               
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("β£οΈ πππππππ", url="https://t.me/BETA_BOTSUPPORT"),
               InlineKeyboardButton("π’ πππππππ", url="https://t.me/Beta_Bot_Updates")
               ],[            
               InlineKeyboardButton("βΉοΈ ππππ", callback_data="help"),
               InlineKeyboardButton("π πππ", callback_data="fun")
               ],[
               InlineKeyboardButton("π¨βπ» ππππ π¨βπ» ", callback_data="devs"),
               InlineKeyboardButton("π€ πππππ", callback_data="about")
               ]]
               )
           )
       if not await db.is_user_exist(message.from_user.id):
          await db.add_user(message.from_user.id)
          await bot.send_message(LOG_CHANNEL, text=LOG_TEXT.format(id=message.from_user.id, dc_id=message.from_user.dc_id, first_name=message.from_user.first_name, username=message.from_user.username, bot=bot.mention))

         
@Client.on_message(filters.command("id"))
async def id_message(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return
    await message.reply_text(
    text = f"""<i>
<u>ποΈβπ¨οΈYOUR DETAILS</u>

β ID : <code>{message.from_user.id}</code>
β DC : <code>{message.from_user.dc_id}</code>
β First Name : <code>{message.from_user.first_name}<code>
β UserName : @{message.from_user.username}
β link : <code>https://t.me/{message.from_user.username}</code>

Thank You For Using Meβ£οΈ</i>""")


@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message): 
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")


@Client.on_message(filters.command(["photoid"]))
async def photoid(bot, message): 
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    if message.reply_to_message.photo:
       await message.reply(f"**Photo ID is**  \n `{message.reply_to_message.photo.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.photo.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a  Photo")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   success = 0 
   failed = 0 
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	time.sleep(0.5)
     	await message.reply_to_message.copy(id)
     	success += 1 
     except:
     	failed += 1 
     	pass
     try:
     	await ms.edit(B_TEXT.format(success=success, failed=failed, tot=tot))
     except FloodWait as e:
     	await asyncio.sleep(t.x)


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(bot, message):    
    a = await message.reply_text(text="<b>Processing</b>")
    await asyncio.sleep(0.5)
    b = await a.edit("<b>Processing β </b>")
    await asyncio.sleep(0.5)
    c = await b.edit("<b>Processing β β </b>")
    await asyncio.sleep(0.5)
    d = await c.edit("<b>Processing β β β </b>")
    await asyncio.sleep(0.5)
    e = await d.edit("<b>Processing β β β β </b>")
    await asyncio.sleep(0.5)
    f = await e.edit("<b>Processing β β β β β </b>")
    await asyncio.sleep(0.5)
    ids = getid()
    tot = len(ids)
    await f.edit(f"Total uses = {tot}")


@Client.on_message(filters.command("logosq") & filters.incoming & filters.text & ~filters.forwarded & filters.private)
async def logosq(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return
    try:
      text = message.text.replace("logosq","").replace("/","").replace("[α·ETα©]","").strip().upper()
      
      if text == "":
        return await message.reply_text("**To Make Logo -** /logo Your Name\n**To Make Square Logo - ** /logosq Your Name\n\n**β»οΈ Example:**\n/logo BETA\n/logosq BETA")
  
      x = await message.reply_text("`π Generating Logo For You...`")  
      logo = await generate_logo(text,True)
  
      if "telegra.ph" not in logo:
        return await x.edit("`β Something Went Wrong...`\n\nReport This Error In [α·ETα©]")
        
      if "error" in logo:
        return await x.edit(f"`β Something Went Wrong...`\n\nReport This Error In [α·ETα©] \n\n`{logo}`")
        
      await x.edit("`π Done Generated... Now Sending You`")
      
      logo_id = logo.replace("https://telegra.ph//file/","").replace(".jpg","").strip()
      
      await message.reply_photo(logo,caption="**πΌ Logo Generated By [α·ETα©]**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File π", callback_data=f"flogo {logo_id}")]]))
      await x.delete()
    except FloodWait:
      pass
    except Exception as e:
      try:
        await x.delete()
      except:
        pass
      return await message.reply_text("`β Something Went Wrong...`\n\nReport This Error In [α·ETα©]")

@Client.on_message(filters.command("logo") & filters.incoming & filters.text & ~filters.forwarded & filters.private)
async def logo(bot, message):
  kikked = await BanChek(bot, message)
  if kikked == 400:
      return
  try:
    text = message.text.replace("logo","").replace("/","").replace("@TechZLogoMakerBot","").strip().upper()
    
    if text == "":
      return await message.reply_text("**To Make Logo -** /logo Your Name\n**To Make Square Logo - ** /logosq Your Name\n\n**β»οΈ Example:**\n/logo BETAs\n/logosq MKN")

    x = await message.reply_text("`π Generating Logo For You...`")  
    logo = await generate_logo(text)

    if "telegra.ph" not in logo:
      return await x.edit("`β Something Went Wrong...`\n\nReport This Error In [α·ETα©]")
      
    if "error" in logo:
      return await x.edit(f"`β Something Went Wrong...`\n\nReport This Error In [α·ETα©] \n\n`{logo}`")
      
    await x.edit("`π Done Generated... Now Sending You`")

    logo_id = logo.replace("https://telegra.ph//file/","").replace(".jpg","").strip()
    await message.reply_photo(logo,caption="**πΌ Logo Generated By [α·ETα©]**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File π", callback_data=f"flogo {logo_id}")]]))
    await x.delete()
  except FloodWait:
    pass
  except Exception as e:
    try:
      await x.delete()
    except:
      pass
    return await message.reply_text("`β Something Went Wrong...`\n\nReport This Error In [α·ETα©]")


@Client.on_callback_query(filters.regex("flogo"))
async def logo_doc(_,query):
  await query.answer()
  try:
    x = await query.message.reply_text("`π Sending You The Logo As File`")
    await query.message.edit_reply_markup(reply_markup=None)
    link = "https://telegra.ph//file/" + query.data.replace("flogo","").strip() + ".jpg"
    await query.message.reply_document(link,caption="**πΌ Logo Generated By [α·ETα©]**")
  except FloodWait:
    pass
  except Exception as e:
    try:
      return await x.edit(f"`β Something Went Wrong...`\n\nReport This Error In [α·ETα©] \n\n`{str(e)}`")
    except:
      return
    
  return await x.delete()






