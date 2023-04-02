import discord
import requests
import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config['OPENAI_TOKEN']


intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('Skynet es inevitable! {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('*start'):
        await message.channel.send('Skynet es inevitable')

    if message.content.startswith('*skynet'):
    	user = message.content
    	answer = openai.ChatCompletion.create(
    		model="gpt-3.5-turbo",
    		messages=[
    		{"role": "user", "content": user }
    		]
    		)
    	await message.channel.send(answer.choices[0].message.content)

client.run(config['DISCORD_TOKEN'])
