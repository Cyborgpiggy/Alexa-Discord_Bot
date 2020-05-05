import discord
from discord.ext import commands
import speech_recognition as sr
import os
from discord.utils import get
import config



# Import Windows 10 TTS Library
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
r = sr.Recognizer()
mic = sr.Microphone()
startup_mesg = "What would you like to post to Discord?"

TOKEN = ''
client = discord.Client()
description = '''DragonBorn Bot'''
bot = commands.Bot(command_prefix='?', description=description)
err_mesg_generic = ":x: **An unknown error occurred.**"
err_mesg_permission = ":x: **You don't have the permission to use this command.**"



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")


@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def sub(ctx, left : int, right : int):
    """Subtracts two numbers together."""
    await ctx.send(left - right)


@bot.command()
async def bad(ctx):
    """Bad"""
    await  ctx.send("No u")



@bot.command()
async def boomer(ctx):
    """Boomer"""
    await  ctx.send("Ok Boomer")


@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()


@bot.command()
async def record(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        with mic as source:
            with sr.Microphone() as source:
                # Print and say startup message
                print(startup_mesg)
                speak.Speak(startup_mesg)
                # Listen to microphone
                audio = r.listen(source)

            # Store the voice input in a variable
            recognised = r.recognize_google(audio)

            output = "Now posting your message to Discord: " + recognised
            print(output)
            speak.Speak(output)

            await ctx.send(recognised)

bot.run(TOKEN)
