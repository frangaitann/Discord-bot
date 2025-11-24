from discord import app_commands
from discord.ext import commands
import discord, re

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix='?', intents=intents)
                
                
                
def ttsymbols(text):
    abecedary = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",  "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻")
    return text.translate(abecedary)



def embed_jumpline(text):
    if r"%1%" in text:
        new_text= re.sub(r"%1%", " \n", text)
        
    if r"%2%" in text:
        new_text= re.sub(r"%2%", "\n\n", text)
        
    return new_text



class ColourTransformer(app_commands.Transformer):
    async def transform(self, interaction: discord.Interaction, value: str) -> discord.Colour:
        try:
            return discord.Colour(int(value.lstrip("#"), 16))
        except ValueError:
            raise app_commands.TransformerError("Formato de color inválido. Usa #RRGGBB.")