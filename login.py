from telethon import TelegramClient, events, sync

api_id = 5186264
api_hash = 'eabf4c3c6406043aba5718ab9f4e2ff0'

client = TelegramClient('anoon', api_id, api_hash)
client.start()

client.send_message('BepCHK_BOT', 'Bot is run.')