import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    # This clears all global commands for this specific bot token
    bot.tree.clear_commands(guild=None)
    await bot.tree.sync()
    print(f"🧹 Old commands for {bot.user.name} have been wiped!")
    await bot.close()

bot.run("YOUR-TOKEN-HERE")
