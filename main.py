import discord
from discord.ext import commands
 
banned_user_ids = [656429456109338624]
 
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Streaming(
            name="OK'RA Shop",
            url="https://www.twitch.tv/OK'RA Hosting"
        )
    )
    print(f'Bot en ligne !')
 
@bot.event
async def on_member_join(member):
    if member.id in banned_user_ids:
        # Use The {member} Variable To Say The Users Name In The Following Code...
        await member.kick(reason="Blacklist")

bot.run('MTM1MTYzMDE3MTU4ODc5MjQwMA.Gtbq7Z.IIcG6xvquKsefDqHc2ZoDN0rPrM7iOhbxel5Zs')