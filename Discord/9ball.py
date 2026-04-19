import discord
from discord import app_commands
from discord.ext import commands
import random
from typing import List

# 1. Setup the Bot with Sync Logic
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def setup_hook(self):
        await self.tree.sync()
        print("✅ Slash commands synced to Discord")

bot = MyBot()

# 2. Define the Autocomplete Suggestions
async def question_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    # These are your pre-defined questions
    suggestions = [
        "Will I every be rich?",
        "Is today my lucky day?",
        "Should I eat pizza?",
        "Will I get a promotion?",
        "Is the moon made of cheese?",
        "version" # Added version here so it's easy to find!
    ]
    # Filter the list as the user types
    return [
        app_commands.Choice(name=q, value=q)
        for q in suggestions if current.lower() in q.lower()
    ][:25]

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user.name}')
    print('------')

# 3. The Slash Command with Autocomplete linked
@bot.tree.command(name="9ball", description="Ask the magic 9-ball a question")
@app_commands.describe(question="Pick a suggestion or type your own custom question")
@app_commands.autocomplete(question=question_autocomplete)
async def nine_ball(interaction: discord.Interaction, question: str):
    
    # Check for version
    if question.lower() == "version":
        await interaction.response.send_message("🤖 **Current Version:** 1.1.0\n🛠️ **Running on:** Q330")
        return

    # Standard 9ball responses
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
    
    await interaction.response.send_message(f"**Question:** {question}\n**Answer:** <:9Ball:1495473917408579806> {random.choice(responses)}")

async def setup_hook(self):
        # This clears the old commands and forces the new ones up
        await self.tree.sync()
        print(f"✅ Synced commands for {self.user.name}")


# Replace with your actual token
bot.run("YOUR-TOKEN-HERE")
