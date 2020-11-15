import discord 

with open('token_discord.txt') as f:
    token = f.read()

with open('id_spotify.txt') as f:
    client_id = f.read()
with open('secret_spotify.txt') as f:
    client_secret = f.read()
with open('redirect_spotify.txt') as f:
    redirect_uri = f.read()
with open('username_spotify.txt') as f:
    username = f.read()
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run(token)