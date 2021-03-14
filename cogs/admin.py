#######################################################
# MADE BY MIRANDANIEL (u/mirandanielcz, @mirandaniel) #
# DONATIONS:                                          #
# ban_1aws637mb3qnuf9j8swzufq3nj3fttuzkixbd817nmmhyms6a6kt1zyptq87
#######################################################

import discord
from discord.ext import commands
import settings
import sys

async def is_owner(ctx):
    return ctx.author.id in settings.bot.admins


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.check(is_owner)
    @commands.command()
    async def shutdown(self, ctx):
        print("Shutting down...")
        await self.bot.logout()

def setup(client):
    client.add_cog(Admin(client))