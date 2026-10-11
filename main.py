from local_data import get_advice, get_visual, get_page
from agent import rta
import time
import discord
from discord import client
from discord import message
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'He ingresado como {bot.user}... ')

@bot.command()
async def ecohelp(ctx):
    await ctx.send("```Hola, soy EcoBot, te ayudaré con tus deberes para ayudar al planeta.\n"
        "?ecohelp - Muestra esta lista de comandos\n"
        "?ecoadvice - Te da un consejo para ayudar al planeta\n"
        "?ecovisual - Te envía una imagen para ayudar al planeta\n"
        "?ecopage - Te envía una página web para ayudar al planeta\n"
        "?ecogo - Apaga el bot```")

@bot.command()
async def ecogo(ctx):
    await ctx.send("```Gusto mio en poder ayudarte, nos vemos!```")
    await ctx.bot.close()

@bot.command()
async def ecoadvice(ctx):
    adv = get_advice()
    await ctx.send(f'```{adv}```')

@bot.command()
async def ecovisual(ctx):
    picture = get_visual()
    await ctx.send(file=picture)

@bot.command()
async def ecowhatdo(ctx, material : str):
    await ctx.send("```Veamos qué podemos hacer para ayudar al planeta con este material...```")
    info = rta(material)
    with open("respuestas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{info}\n\n")
    await ctx.send(f"```{info}```")

@bot.command()
async def ecopage(ctx):
    await ctx.send("```Veamos que podemos encontrar en internet para ayudar al planeta...```")
    time.sleep(1)
    await ctx.send(get_page())
    await ctx.send("```Esta pagina puede ser útil para aprender más sobre cómo ayudar al planeta.```")

bot.run("Token Here")