import os
import discord
from openai import AsyncOpenAI
from discord.ext import commands
from dotenv import load_dotenv

# Load our environment variables
load_dotenv()
    
TOKEN = os.getenv('discord_token')

client = AsyncOpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
conversations = {}

# Configure Discord permissions
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Runs when the bot successfully connects
@bot.event
async def on_ready():
    print(f"{bot.user} is now online!")
    print("Nexus AI is ready.")

@bot.command()
async def ping(ctx):
    await ctx.send("Nexus AI is online! 🤖")


@bot.command()
async def ask(ctx, *, question):
    async with ctx.typing():
        try:
            response = await client.responses.create(
                model="openai/gpt-oss-20b",
                instructions="You are NexusAI, a helpful and intelligent Discord assistant.",
                input=question
            )

            await ctx.reply(response.output_text[:1900])

        except Exception as e:
            print(f"AI Error: {e}")
            await ctx.reply("NexusAI encountered an error. Try again.")


@bot.event
async def on_message(message):

    # Ignore messages from bots
    if message.author.bot:
        return

    # Detect if NexusAI was mentioned
    mentioned = bot.user in message.mentions

    # Detect if someone replied to NexusAI
    replied_to_bot = False
    replied_message = None

    if message.reference:
        replied_message = message.reference.resolved

        if replied_message is None and message.reference.message_id:
            try:
                replied_message = await message.channel.fetch_message(
                    message.reference.message_id
                )
            except discord.NotFound:
                pass

        if replied_message and replied_message.author.id == bot.user.id:
            replied_to_bot = True

    # Only respond to mentions or replies to NexusAI
    if mentioned or replied_to_bot:

        # Remove the bot mention from the question
        question = message.content.replace(
            f"<@{bot.user.id}>", ""
        ).replace(
            f"<@!{bot.user.id}>", ""
        ).strip()

        if not question:
            await message.reply("Hey! What can I help you with?")
            return

        # Include the replied message as context
        if replied_to_bot and replied_message:
            question = (
                f"Previous NexusAI message: {replied_message.content}\n"
                f"User's reply: {question}"
            )

        async with message.channel.typing():
            try:
                response = await client.responses.create(
                    model="openai/gpt-oss-20b",
                    instructions=(
                        "You are NexusAI, a helpful, intelligent "
                        "and conversational Discord assistant."
                    ),
                    input=question
                )

                await message.reply(response.output_text[:1900])

            except Exception as e:
                print(f"AI Error: {e}")
                await message.reply(
                    "Something went wrong. Try again!"
                )

    # Keep existing ! commands working
    await bot.process_commands(message)

# Start the bot
if not TOKEN:
    raise ValueError("DISCORD_TOKEN is missing from .env")

bot.run(TOKEN)