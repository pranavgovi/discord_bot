import discord
import requests
import json
import random
from keep_alive import keep_alive
api_key='tkHtxZ-gcftp'
run_token='tOTWSDaUZCCT'
proj_token='tPQ1K8T2tE3T'
client=discord.Client()
class Data:
    def __init__(self, api_key, proj_token):
        self.api_key = api_key
        self.proj_token = proj_token
        self.params = {
            "api_key": self.api_key
        }
        self.getdata()

    def getdata(self):
        response = requests.get(f'https://parsehub.com/api/v2/projects/{proj_token}/last_ready_run/data',
                                params=self.params)
        self.data = json.loads(response.text)
l=[]

f=Data(api_key,proj_token)
for i in range(0,len(f.data['selection1'])):
  l.append(f.data['selection1'][i]['name'])

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  mes=message.content
  if message.author == client.user:
    return
  if message.content.startswith('hello'):
    await message.channel.send('Hi I am {0.user} How can i help you?'.format(client))
  s=["Pranav",'Sachin']
  for i in s:
    if i in mes:
      await message.channel.send("heyy {0}".format(i))
  d=['pickup','pickup line','romantic','love']
  for i in d:
    if i in mes:
      await message.channel.send(random.choice(l))
keep_alive()
client.run('ODcxNDM3OTgwMzc4NzQ2OTYw.YQbT3Q.tvwU7Vbd92pDw8CKVcOOOWd4DPc')