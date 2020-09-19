import discord
import asyncio
from discord.ext import commands

client = discord.Client()  # 接続に使用する
bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready(): # botが起動したときに動作する処理
    print('ログインしました')
    await client.change_presence(activity=discord.Game(name="Call56NetWorkサーバーログ転送中", type=1))

@bot.command(name="a")
async def rank(ctx):
    await ctx.send(f"https://cdn.discordapp.com/attachments/725964985670303795/746604189337255936/card.png")

client.run('TOKEN')
