#######################################################
# MADE BY MIRANDANIEL (u/mirandanielcz, @mirandaniel) #
# DONATIONS:                                          #
# ban_1aws637mb3qnuf9j8swzufq3nj3fttuzkixbd817nmmhyms6a6kt1zyptq87
#######################################################

import discord
from discord.ext import commands
import sys
sys.path.append("mdbot")
import settings

class Master(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\nLOGGED IN")
        print("="*25)
        print(f"ID = {self.bot.user.id}")
        print(f"NAME = {self.bot.user.name}#{self.bot.user.discriminator}")
        print(f"PING = {round(self.bot.latency*1000)}ms")
        print(f"GUILDS = {len(self.bot.guilds)}")
        print("="*25)
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id != self.bot.user.id:
            print(f"MESSAGE")

    @commands.Cog.listener()
    async def on_message_edit(self,before, after):
        print(f"EDIT")

    @commands.command()
    async def ping(self,ctx):
        ping = round(self.bot.latency*1000)
        if ping > 250:
            c = 0xFBDD11
        elif ping > 150:
            c = 0xFBDD11
        else:
            c = 0xFBDD11
        embed = discord.Embed(
            color=c)
        embed.add_field(name="Ping", value=f"{ping}ms", inline=False)
        embed.set_footer(text=f"Requested by {ctx.message.author.name}#{ctx.message.author.discriminator}")
        await ctx.message.channel.send(embed=embed)

    @commands.command()
    async def info(self,ctx):
        embed = discord.Embed(title="Info", color=0xFBDD11)
        embed.add_field(name="Version", value=settings.bot.version, inline=False)
        embed.add_field(name="Prefixes", value=settings.bot.prefixes, inline=False)

        embed.add_field(name="Developer", value="github.com/mirandaniel")
        embed.set_footer(text=f"Requested by {ctx.message.author.name}#{ctx.message.author.discriminator}")
        await ctx.message.channel.send(embed=embed)

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title="Help", color=0xFBDD11)
        embed.add_field(name="search \{wallet\}", value="Shows database records of a wallet", inline=False)
        embed.add_field(name="view", value="Shows number of database records", inline=False)
        embed.add_field(name="add \{wallet\} \{type\} \{reason\}", value="Adds a wallet to the database ***admin only***", inline=False)
        embed.add_field(name="remove \{wallet\} \{type\} \{reason\}", value="Removes a wallet from the database ***admin only***", inline=False)

        embed.set_footer(text=f"Requested by {ctx.message.author.name}#{ctx.message.author.discriminator}")
        await ctx.message.channel.send(embed=embed)


def setup(client):
    client.add_cog(Master(client))