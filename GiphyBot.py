import discord
import giphy_client
import random
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')


client = discord.Client()
@client.event
async def on_ready():
    print('Ready to Rock n Roll!!')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    elif message.content.lower().startswith('-gif'):
        message.content = message.content.replace('-gif ', '')
        api_key = os.getenv('API_KEY')
        api_instance = giphy_client.DefaultApi()
        
        api_responce = api_instance.gifs_search_get(api_key,message.content, limit=15, rating='g')
        lst = list(api_responce.data)
        giff = random.choice(lst)
        await message.channel.send(giff.embed_url)
        
client.run(token)