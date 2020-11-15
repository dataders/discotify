import re

import discord
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


def is_spot_url(url):
    rgx = re.compile(r'^(spotify:|https://[a-z]+\.spotify\.com/)')
    return re.match(rgx, url) is not None

with open('token_discord.txt') as f:
    token_discord = f.read()

with open('id_spotify.txt') as f:
    client_id = f.read()
with open('secret_spotify.txt') as f:
    client_secret = f.read()
with open('redirect_spotify.txt') as f:
    redirect_uri = f.read()
with open('username_spotify.txt') as f:
    username = f.read()

scope_str = ','.join(['playlist-read-collaborative','playlist-modify-private'])

token = util.prompt_for_user_token(
        username=username,
        scope=scope_str,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri)

id_bangerz = '2uzDA17Iy7SQnjcrugRpN4'


spotify = spotipy.Spotify(auth=token)
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
        if is_spot_url(message.content):
            rsp = spotify.playlist_add_items(id_bangerz, [message.content])
            pl = spotify.playlist(id_bangerz)
            tr = spotify.track(message.content)
            await message.channel.send('added {} by {} to the {} playlist'.format(
                tr['name'],
                tr['artists'][0]['name'],
                pl['name']
                # pl['external_urls']['spotify']
            ))

client = MyClient()
client.run(token_discord)