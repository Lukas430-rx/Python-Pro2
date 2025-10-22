import discord
import random
import requests
import os
from discord.ext import commands
from musicbot import Music

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.add_cog(Music(bot))

@bot.command()
async def coinflip(ctx):
    #lanza una moneda al aire
    await ctx.send(random.choice(["🪙 Cara", "🪙 Cruz"]))

@bot.command()
async def emoji(ctx):
    #envia un emoji aleatorio
    await ctx.send(random.choice(["😀", "😎", "🔥", "🤖", "🐍"]))

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    # Joined at can be None in very bizarre cases so just handle that as well
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')
@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')



@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

#Obtener aleatoriamente una imagen de perro desde una API
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    embed = discord.Embed(title="🐶 ¡Un perrito para ti!")
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

@bot.command()
async def meme(ctx):
    imagenes = os.listdir('imagenes')
    with open(f'imagenes/{random.choice(imagenes)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

#Obtener aleatoriamente una imagen de zorro desde una API
def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']
@bot.command('fox')
async def fox(ctx):
    image_url = get_fox_image_url()
    embed = discord.Embed(title="🦊 ¡Un zorro salvaje aparece!")
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

#Obtener aleatoriamente un Pokémon desde una API
def get_pokemon():
    pokemon_id = random.randint(1, 151)  # primeros 151 (generación 1)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    res = requests.get(url)
    data = res.json()
    nombre = data['name'].capitalize()
    imagen = data['sprites']['front_default']
    return nombre, imagen
@bot.command('pokemon')
async def pokemon(ctx):
    nombre, imagen = get_pokemon()
    embed = discord.Embed(title=f"🎮 ¡Has encontrado a {nombre}!")
    embed.set_image(url=imagen)
    await ctx.send(embed=embed)
