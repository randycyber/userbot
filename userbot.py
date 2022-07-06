from telethon import TelegramClinet, client, events

api_id = 
api_hash = ''

rendy = TelegramClient('session', api_id, api_hash)

@rendy.on(events.NewMessage(outgoing=True, pattern=r\'.ping'))
async def pingme(event):
  chat = event.get_chat()
  await rendy.edit_message(event.message, "ping......")
  
@rendy.on(events.NewMessage(outgoing=True, pattern=r\'.alive'))
async def alive(event):
  chat = event.get_chat()
  await client.delete_message(chat, event.message)
  photo = await client.download_profile_photo('me')
  await client.send_file(chat, file=photo, caption="yes i'am alive")
  os.remove(photo)

rendy.start()
rendy.run.until.disconnected()
