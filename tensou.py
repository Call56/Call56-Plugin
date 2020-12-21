import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready(): # botが起動したときに動作する処理
    print('ログインしました')
    await client.change_presence(activity=discord.Game(name="Call56NetWorkサーバーログ転送中", type=1))

@bot.command()
async def rank(rank):
    await rank.send("https://cdn.discordapp.com/attachments/725964985670303795/746604189337255936/card.png")

bot.run('TOKEN')
