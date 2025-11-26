import discord
from discord.ext import commands
import re
import time

class TimeCapsule(commands.Cog):
    def __init__(self, bot, name: str, objectlist: list, countdown_before_opening: int, author_id: int, ping: list):
        self.name = name
        self.countdown_before_opening = countdown_before_opening
        self.objectlist = objectlist
        self.bot = bot
        self.author_id = author_id
        self.ping = ping


    async def choose_an_action(self, ctx):
        embed_choice = discord.Embed(title="")
        embed_choice.add_field(name="", value=f"Nom de la Capsule : **{self.name.content}**\n\nVeuillez choisir une action :\n\n\n0 - Veuillez saisir cette action lorsque vous aurez fini d'ajouter vos objets\n1 - Ajouter un objet à la Time Capsule\n2 - Mentionner quelqu'un à l'ouverture de la Time Capsule\n\n\n", inline=False)
        choice = await ctx.send(embed=embed_choice)

        await choice.add_reaction("▶️")
        await choice.add_reaction("1️⃣")
        await choice.add_reaction("📞")

        reaction, user = await self.bot.wait_for("reaction_add", timeout=60)

        if reaction.emoji == "▶️":
            await self.count(ctx)
        elif reaction.emoji == "1️⃣":
            await self.add_object(ctx)
        elif reaction.emoji == "📞":
            await self.mention(ctx)
            # créer une réaction/méthode pour ping une personne à l'ouverture de la capsule

    async def count(self, ctx):
        for i in range(self.countdown_before_opening, 0, -1):
            await ctx.send(i)
            time.sleep(1)
        await ctx.send(f"<@{self.author_id}>")
        for i in self.ping:
            await ctx.send(f"{i}")
        embed_opening = discord.Embed(title="")
        embed_opening.add_field(name="", value="Ouverture de la Time Capsule...\n", inline=False)
        await ctx.send(embed=embed_opening)
        embed_count = discord.Embed(title="")
        embed_count.add_field(name="", value=f"La Capsule '**{self.name.content}**' contenait les éléments ci-dessous :\n\n", inline=False)
        await ctx.send(embed=embed_count)
        for l in self.objectlist:
            embed_object = discord.Embed(title="")
            embed_object.add_field(name="", value=f"- **{l}**", inline=False)
            await ctx.send(embed=embed_object)


    async def add_object(self, ctx):
        embed_add = discord.Embed(title="")
        embed_add.add_field(name="", value="Que voulez-vous ajouter à votre Capsule ?", inline=False)
        await ctx.send(embed=embed_add)
        add = await self.bot.wait_for("message", check=None)
        self.objectlist.append(add.content)
        embed_add_return = discord.Embed(title="")
        embed_add_return.add_field(name="", value=f"l'élément : {add.content} à été ajouté à la Time capsule {self.name.content}.", inline=False)
        await ctx.send(embed=embed_add_return)
        await self.choose_an_action(ctx)

    async def mention(self, ctx):
        embed_asked = discord.Embed(title="")
        embed_asked.add_field(name="", value="Qui voulez-vous ping à l'ouverture de la Capsule ?", inline=False)
        await ctx.send(embed=embed_asked)
        ping = await self.bot.wait_for("message", check=None)
        mention = ping.content
        self.ping.append(mention)
        embed_confirmation = discord.Embed(title="")
        embed_confirmation.add_field(name="", value=f"{ping.content} sera ping à l'ouverture de la Capsule", inline=False)
        await ctx.send(embed=embed_confirmation)
        await self.choose_an_action(ctx)

    # async def remove_object(self, ctx):
    #     await ctx.send("Que voulez-vous enlever de votre Capsule ?")
    #     which_object = await self.bot.wait_for('message', check=None)
    #     for i in self.objectlist:
    #         if i == which_object.content:
    #             self.objectlist.remove(which_object.content)
    #             await ctx.send(f"l'élément : {which_object.content} à été ajouté à la Time capsule {self.name.content}.")
    #             await self.choose_an_action(ctx)


