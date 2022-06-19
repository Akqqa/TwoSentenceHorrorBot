import os
import discord
from scraper import *
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = discord.Bot()

@bot.slash_command(name="scareme", description="Creates a horror story")
async def scareme(ctx):
    reddit = setupScraper()
    title=randomPostTitle(reddit, "twosentencehorror")
    text = randomPostText(reddit, "twosentencehorror")

    await ctx.respond("**" + title + "**" + "\n\n" + "||" + text + "||")

bot.run(token)
