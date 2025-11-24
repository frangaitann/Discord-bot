import discord, requests, zoneinfo, datetime
from .defs import bot
from discord.ext import tasks

@bot.event
async def on_ready():
    print(f'Bot connected as: {bot.user}')
    await bot.tree.sync()
    epic_fg.start()
    

# Epic Games weekly-free games checker
@tasks.loop(hours=12)
async def epic_fg():
    tz = zoneinfo.ZoneInfo("America/Buenos_Aires")  # Change the timezone to yours
    print(f"{datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}(ARG)  Checking Epic Free Games")
    
    url = "https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=US&allowCountries=US"
    response = requests.get(url)
    data = response.json()

    games = data["data"]["Catalog"]["searchStore"]["elements"]
    titles = []
    channel = bot.get_channel(0000000000000) # <---- Here must go your channel id, you got it by right clicking channel and copy channel id (with developer tools option enabled)
            
    for i in games:
        if i['promotions'] and 'promotionalOffers' in i['promotions']:
            
            free = i['promotions']['promotionalOffers']
            if free:
                game = free[0]['promotionalOffers'][0]
                g_title = i['title']
                g_desc = i.get('description')
                g_thumb = i['keyImages'][0]['url']
                
                with open("free_gs.txt", "+a", newline="\n") as f:
                    f.seek(0)
                    g_list = f.read()
                    lines = f.readlines()

                    if g_title not in g_list:
                        f.write(f"{g_title}\n")
                    elif g_title in g_list:
                        return
            
                ye = game['endDate'][:4]
                me = game['endDate'][5:7]
                de = game['endDate'][8:10]
                ending = de + "/" + me + "/" + ye
                
                if g_desc != None:
                    desc = g_desc
                else:
                    desc = "No se encontró una descripción disponible"
                    
                embed= discord.Embed(
                    title=f"¡{g_title} Está gratis en EpicGames!",
                    description=f"{desc} \n\n **Disponbile hasta: {ending}**",
                    color=0xFFFFFF,
                )
                embed.set_image(url=g_thumb)
                
                await channel.send(embed=embed)