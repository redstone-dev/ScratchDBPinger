import scratchcloud as scratch3
from scratchcloud.ext import BaseCodec 
import asyncio
import requests
from dotenv import dotenv_values
from os.path import exists
from sys import exit

if not exists('.env'):
    print('ERROR * No .env file found!')
    print('      * You must create one in the same directory as this script.')
    print('      * Then, add the following to .env:')
    print("""          1  USER="<Scratch username>"
          2  PASS="<Scratch password>"
""")
    print('      * Finally, run this script again.')
    exit(1)

SERVER_PASSWORD = dotenv_values('.env')['PASS']

codec = BaseCodec()
client = scratch3.CloudClient(
    "Redstone1080", 
    878884618, 
    disconnect_messages=True,
    encoder=codec.encode,
    decoder=codec.decode,
    ignore_missing_variables=True,
    reconnect_cooldown=3
)

first = True
count = 0

async def looping_task():
    is_scratchdb_up = requests.get('https://scratchdb.lefty.one/v3/user/info/Redstone1080')
    while True:
        if client.logged_in:
            expr = 'up' if is_scratchdb_up.text != None else 'down'
            print(f'sent {expr}')
            await client.set_cloud('RESPONSE', expr)
        
        await asyncio.sleep(1)

@client.event
async def on_connect():
    global first
    if first:
        first = False
        client.loop.create_task(looping_task())
        
client.run(SERVER_PASSWORD)