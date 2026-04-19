import discord
from discord.ext import commands
import random

# Using intents.all() as you have it set
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user.name}')
    print('------')

@bot.command(name="8ball")
async def eight_ball(ctx, *, question=None):
    # 1. Check if they asked for the version
    if question is not None and question.lower() == "version":
        await ctx.send("🤖 **Current Version:** 1.0.0\n🛠️ **Running on:** Q330")
        return

    # 2. Check if they forgot to ask a question
    if question is None:
        await ctx.send("Please ask a question! Example: `!8ball will I be rich?`")
        return

    # 3. Standard 8ball responses
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
        "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.",
        "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
        "Don't count on it.", "My reply is no.", "My sources say no.",
        "Outlook not so good.", "Very doubtful.",
        "Have you tried turning it on and off again?",
        "Perhaps.", "Sounds like a great idea!",
        "It's really hard to say at this time.",
        "Better ask Zoltar!", "Who is Stephan?",
        "Hm... what would ChatGPT say?", "It depends.",
        "Ha, wouldn't you like to know!", "All signs point to YES!"
    ]
    
    await ctx.send(f"**Question:** {question}\n**Answer:** {random.choice(responses)}")


# Reminder: Replace this with your newly reset token from the Dev Portal!
bot.run("YOUR-TOKEN-HERE")
