import discord, random
from .defs import *


# Embed builder for easy embed type messages (Color uses HEX without #, just letter/number example: #fffff == fffff)
@bot.tree.command(name="embedbuild", description="Embed message easy builder [ONLY FG .Teams MEMBERS]")

async def embedbuilder(interaction: discord.Interaction, title :str, text: str, channel: discord.TextChannel, color: ColourTransformer, image: str = None, foot: str = None):
    
    admin_roles = ["Founder", "Manager"]
    
    for i in admin_roles:
        role = discord.utils.get(interaction.guild.roles, name=i)
        if role in interaction.user.roles:
            embed = discord.Embed(title=title, description=embed_jumpline(text), color=color)     # if you type %1% in the text arg it wil make a jumpline, if you type %2% makes 2 jumplines
            embed.set_author(name="FG .Teams", icon_url="https://i.imgur.com/PNl9OKH.jpeg")
        
            if image:
                embed.set_image(url=image)
            if foot:
                embed.set_footer(icon_url="https://i.imgur.com/PNl9OKH.jpeg", text=foot)
            
            await channel.send(embed=embed)

            await interaction.response.send_message(f"Embed has been sent to {channel}", ephemeral=True)
    
        else:
            await interaction.response.send_message("You don't have permissions to use this command ❌", ephemeral=True)



# Social media command (Can be adapted to an event, for auto-spamming)
@bot.tree.command(name="socialmedia", description="Mirá lo que hago acá.")

async def social_med(interaction: discord.Interaction):
    embed = discord.Embed(title="Mis proyectos 👤💼", description=ttsymbols(f"Puedes ver mis trabajos y proyectos en: ") + "\n- Github: https://github.com/frangaitann \n- Behance: https://www.behance.net/fgaitan \n- Website: ||**Soon**|| ;)", color= 0x8c66c9)
    embed.set_author(name="FG.", icon_url="https://i.imgur.com/PNl9OKH.jpeg")
    embed.set_image(url="https://i.imgur.com/PNl9OKH.jpeg")

    await interaction.response.send_message(embed=embed)



# Clean command, for erasing chats or part of them
@bot.tree.command(name="clean", description="Limpia una cantidad X de mensajes en el chat.")
async def clean(interaction: discord.Interaction, amount: int):
    admin_roles = ["Founder", "Manager"]
    
    for i in admin_roles:
        role = discord.utils.get(interaction.guild.roles, name=i)
        if role in interaction.user.roles:
            await interaction.channel.purge(limit=amount)
    
    try:
        await interaction.response.send_message(f"🧹 {amount} mensajes eliminados", ephemeral=True)
    except:
        await interaction.response.send_message(f"🧹 {amount} mensajes eliminados", ephemeral=True) # Poor solving to asynchronous purge erasing bot response too, but works


# Salva a Messi
@bot.tree.command(name="messi", description="Messi necesita tu ayuda...")

async def messi(interaction: discord.Interaction):
    N = random.randint(1, 7) 
    
    if N == 1:
        embed = discord.Embed(title="💳 Messi te pide tu tarjeta de credito...", description=f"Resulta que Messi realmente estaba en apuros con hacienda y gracias a ti se salvó, ganamos la 4ta y el pueblo Argentino y Catalán están agradecidos contigo", color=0x15ff00)
        embed.set_author(name="Messi", icon_url="https://img.a.transfermarkt.technology/portrait/big/28003-1740766555.jpg?lm=1")  
        embed.set_image(url="https://media.minutouno.com/p/d6dbcff318c3f537c617e21799b9bc9a/adjuntos/150/imagenes/042/309/0042309457/messi-copa-del-mundojpg.jpg")
        await interaction.response.send_message(embed=embed)

    elif N == 2:
        embed = discord.Embed(title="💳 Messi te pide tu tarjeta de credito...", description=f"Resulta que Messi en realidad era un estafador Nigeriano, tu cuenta de banco se desplomó a 0 y te mueres de hambre bajo el puente Avellaneda.", color=0xff0000)
        embed.set_author(name="Messi", icon_url="https://img.a.transfermarkt.technology/portrait/big/28003-1740766555.jpg?lm=1")  
        embed.set_image(url="https://aica.org/imagenes/noticias/2021/obispo-nigeriano-lamento-la-crisis-del-pais-se-parece-a-una-guerra-contra-los-cristianos-fgK0.jpg")
        await interaction.response.send_message(embed=embed)

    elif N == 3:
        embed = discord.Embed(title="💳 Messi te pide tu tarjeta de credito...", description=f"Messi era el verdadero, el problema es que no tenía problema ninguno y simplemente decidió irse de vacaciones sin poner dinero, estás pobre y muerto de hambre... Pero al menos hablaste con Messi 🙂", color=0xff7300)
        embed.set_author(name="Messi", icon_url="https://img.a.transfermarkt.technology/portrait/big/28003-1740766555.jpg?lm=1")  
        embed.set_image(url="https://s3.amazonaws.com/arc-wordpress-client-uploads/infobae-wp/wp-content/uploads/2017/01/01122134/messi-pileta-1920.jpg")
        await interaction.response.send_message(embed=embed)

    elif N == 4:
        embed = discord.Embed(title="💳 Messi te pide tu tarjeta de credito...", description=f"Messi en realidad era Cristiano Ronaldo queriendo dejar a su rival mal parado, te diste cuenta de esto en el momento en el que al pasarle la tarjeta escuchaste al otro lado del telefono a alguien gritar 'SIUUUUU'", color=0xff7300)
        embed.set_author(name="Messi", icon_url="https://img.a.transfermarkt.technology/portrait/big/28003-1740766555.jpg?lm=1")  
        embed.set_image(url="https://kawaink.co.uk/cdn/shop/articles/c.ronaldo7.jpg?v=1732614242")
        await interaction.response.send_message(embed=embed)

    elif N == 5:
        embed = discord.Embed(title="💳 Messi te pide tu tarjeta de credito...", description=f"Tras una llamada, te juntaste en persona con Messi para darle tu tarjeta en persona, Yassine Cheuko, el guardia de Messi, creyó que ibas a hacerle daño asi que te tacleó y te noqueó. ", color=0xff7300)
        embed.set_author(name="Messi", icon_url="https://img.a.transfermarkt.technology/portrait/big/28003-1740766555.jpg?lm=1")  
        embed.set_image(url="https://images2.minutemediacdn.com/image/upload/c_crop,w_3834,h_2156,x_166,y_3/c_fill,w_720,ar_16:9,f_auto,q_auto,g_auto/images/voltaxMediaLibrary/mmsport/si/01jqv03yvs5xprsgwjjh.jpg")
        await interaction.response.send_message(embed=embed)

    elif N == 6:
        embed = discord.Embed(title="💳 Messi te pide tu tarjeta de credito...", description=f"Tras ayudarlo a Messi, te invitaron a comer en su casa de Miami en forma de agradecimiento, Ibai estaba ahí también y pudiste tener una buena charla con ellos.", color=0x15ff00)
        embed.set_author(name="Messi", icon_url="https://img.a.transfermarkt.technology/portrait/big/28003-1740766555.jpg?lm=1")  
        embed.set_image(url="https://images.pagina12.com.ar/styles/focal_content_1200x1050/public/am750-legacy-img/ibai-llanos-lionel-messi-e1628511039159.jpg?itok=FI_EqB0V")
        await interaction.response.send_message(embed=embed)

    elif N == 7:
        embed = discord.Embed(title="💳 Messi te pide tu tarjeta de credito...", description=f"La aduana y el AFIP te detuvieron al intentar sacar dinero del país, enfrentas un juicio millonario y tus posesiones han sido embargadas, mas suerte a la proxima 💕", color=0xff0000)
        embed.set_author(name="Messi", icon_url="https://img.a.transfermarkt.technology/portrait/big/28003-1740766555.jpg?lm=1")  
        embed.set_image(url="https://www.elindependiente.com.ar/elindependiente/1.0/img/061913971.jpg")
        await interaction.response.send_message(embed=embed)