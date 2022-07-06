from tethon import TelegramClinet, events

api_id = 
api_hash = ''

rendy = TelegramClient('session', api_id, api_hash)

@rendy.on(events.NewMessage(outgoing=True, pattern=r\'.ping'))
async def pingme(event):
  chat = event.get_chat()
  await rendy.edit_message(chat, "ping......")
