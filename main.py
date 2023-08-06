import discord
from discord.ext import commands
from config import settings
import key
from discord import FFmpegPCMAudio
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


@bot.command(name='подключить')
async def startq(ctx, name):
    voicechannel = discord.utils.get(ctx.guild.voice_channels, name=name)
    key.vc = await voicechannel.connect()
    print(key.vc.play)
    key.voiseconnect_b = True


@bot.command(name='отключить')
async def startqq(ctx, name):
    await key.vc.disconnect()
    key.voiseconnect_b, voise_name = False, None


@bot.command(name='стоп')
async def startqqq(ctx, *name):
    key.vc.stop()


@bot.command(name='пауза')
async def startqqqq(ctx, *name):
    if key.vc.is_paused():
        key.vc.resume()
    else:
        key.vc.pause()


@bot.command(name='играть')
async def startqqqqq(ctx, *, name):
    music_source = FFmpegPCMAudio(source=f'music/{name}.mp3', executable='ffmpeg.exe')
    key.vc.play(music_source)


@bot.command(name='сохранить')
async def on_message(ctx, *, name):
    for attach in ctx.message.attachments:
        await attach.save(f"music/{name}.mp3")  # {list(attach.filename.split('.'))[-1]}


bot.run(settings['token'])
