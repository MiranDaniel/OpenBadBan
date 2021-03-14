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
import psycopg2

class Master(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.trusted = [476348613870616576, 812531539598508042, 610540629298118676]

    @commands.command()
    async def add(self, ctx, wallet, t, *, reason="none"):
        
        if ctx.author.id not in self.trusted:
            await ctx.send("You do not have the permissions to use this command. This incident will be reported.")
            return
        conn = psycopg2.connect(
        host=settings.sql.host,
        database=settings.sql.database,
        user=settings.sql.user,
        password=settings.sql.password)
        cursor = conn.cursor()
        sql = f"""INSERT INTO banned (uname,utype,ureason) VALUES ('{wallet}','{t}','{reason}')"""
        cursor.execute(sql)
        conn.commit()
        await ctx.send(f"I added `{wallet[:10]}...` to the database")

    @commands.command()
    async def remove(self, ctx, wallet):
        if ctx.author.id not in self.trusted:
            await ctx.send("You do not have the permissions to use this command. This incident will be reported.")
            return
        conn = psycopg2.connect(
        host=settings.sql.host,
        database=settings.sql.database,
        user=settings.sql.user,
        password=settings.sql.password)
        cursor = conn.cursor()
        sql = f"""DELETE FROM banned WHERE uname LIKE '{wallet}'"""
        cursor.execute(sql)
        conn.commit()
        await ctx.send(f"I removed `{wallet[:10]}...` from the database")

    @commands.command()
    async def search(self, ctx, wallet):
        conn = psycopg2.connect(
        host=settings.sql.host,
        database=settings.sql.database,
        user=settings.sql.user,
        password=settings.sql.password)
        try:
            cursor = conn.cursor()
        except:
            await ctx.send("Cannot access database.")
            return
        sql = f"""SELECT * FROM banned WHERE uname LIKE '{wallet}'"""
        cursor.execute(sql)
        d = cursor.fetchall()
        dl = len(d)
        if dl > 0:
            msg = [f"I have found {dl} record{'' if dl == 1 else 's'} about this user","`type | reason`","`-------------`"]
            for i in d:
                msg.append(f"`{i[1]} | {i[2]}`")
            await ctx.send("\n".join(msg))
        else:
            await ctx.send("I haven't found this user in my database")

    @commands.command()
    async def view(self, ctx):
        conn = psycopg2.connect(
        host=settings.sql.host,
        database=settings.sql.database,
        user=settings.sql.user,
        password=settings.sql.password)
        cursor = conn.cursor()
        sql = f"""SELECT * FROM banned"""
        cursor.execute(sql)
        d = cursor.fetchall()
        dl = len(d)
        await ctx.send(f"There are {dl} records in my database. *That's {dl} more than I would like to see*")

def setup(client):
    client.add_cog(Master(client))