from telethon import TelegramClinet, client, events

api_id = 
api_hash = ''

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(outgoing=True, pattern=r\'.ping'))
async def pingme(event):
   chat = event.get_chat()
   await rendy.edit_message(event.message, "ping......")
  
@client.on(events.NewMessage(outgoing=True, pattern=r\'.alive'))
async def alive(event):
   chat = event.get_chat()
   await client.delete_message(chat, event.message)
   photo = await client.download_profile_photo('me')
   await client.send_file(chat, file=photo, 
   caption=
   "yes i'am alive.\n"
   "Owner [dev](https://t.me/FFmpegNotInstalled)\n"
   "Channel [dev](https://t.me/Rendyprojects)\n"
   )
   os.remove(photo)

client.start()
client.run.until.disconnected()
