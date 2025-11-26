import random
import discord
import json
from discord.ext import commands
import re
from time_caps import TimeCapsule
import time
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='s!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Ready !")
    await bot.change_presence(activity=discord.Game(name="/help & s!‎ 🦋"))
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} slashs commands ready")
    except Exception as e:
        print(e)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(color=0x59042e, title="")
        embed.add_field(name="Erreur", value="La commande n'a pas été trouvée", inline=False)
        await ctx.send(embed=embed)
        print(f"Error : {error}")

    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=0x992d22, title="")
        embed.add_field(name="Erreur", value="Il manque un argument", inline=False)
        await ctx.send(embed=embed)
        print(f"Error : {error}")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(color=0x992d22, title="")
        embed.add_field(name="Erreur", value="Vous n'avez pas la permission requise", inline=False)
        await ctx.send(embed=embed)
        print(f"Error : {error}")

    if isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(color=0x992d22, title="")
        embed.add_field(name="Erreur", value="Je n'ai pas les permissions naicéssaire pour réaliser cette commande 😅", inline=False)
        await ctx.send(embed=embed)
        print(f"Error : {error}")


@bot.command()
async def vote(ctx, msgID: int):
    msg = await ctx.fetch_message(msgID)

    await msg.add_reaction(f"👍")
    await msg.add_reaction(f"👎")

@bot.tree.command(name="help", description="Manuel de Sýndromos#4001")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(color=0x992d22, title="Manuel de Sýndromos#4001", url="https://syndromos.kittyhosting.ch/")
    embed.add_field(name="\nPréfix : `s!`", value="\n", inline=False)
    embed.add_field(name="Commandes de Jeux 🎡\n ", value="\n- `popogame` : lance un jeu de potion\n- `stickgame` : lance un jeu de bâtons ( se joue à minimum deux personnes )\n‎ \n \n\n", inline=False)
    embed.add_field(name="Random Commandes 🎲\n ", value="\n- `randomsentence` : génère une phrase random\n- `syndrome` : donne un syndrome random ( il faut spécifier plus loin l'utilisateur qui recevera le syndrome ou sinon vous pouvez mettre random)\n\n- `randominteger` : génère un nombre __entier__ random compris entre deux nombres __entiers__\n- `randomdecimal` : génère un nombre __à virgule__ random compris entre deux nombres __entiers__\n\n- `pile_face` : choisis entre pile ou face\n \n", inline=False)
    embed.add_field(name="\nRéactions Commandes 👒\n ", value="\n-`vote (id du message)` : ajoute les réactions 👍 et 👎\n‎ \n", inline=False)
    embed.add_field(name="Autres Commandes (big) 🪅🎊\n ", value="\n- `caps` : Créer une **Time Capsule**\n- `qrcode 'url'` : renvoi **l'url** donné sous forme de **QR code**\n‎ \n", inline=False)
    embed.add_field(name="Autres Commandes (little) 📦\n ", value="\n- `say` : dit ce que vous écrirez\n- `gif` : renvoi un gif random de la liste de gif du bot\n- `member_list` : donne la liste des membres (pseudos et l'id)\n- `bam` : renvoi boum avec la latence de la réponse (ms, s, h)\n- `userinfo (membre)` : cette commande permet d'afficher les informations d'un utilisateur\n‎ \n", inline=False)
    embed.set_footer(text="Créateur : Shisaku")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1074611167844126790/1082295521663787038/images.png")
    await interaction.response.send_message(embed=embed)


@bot.command()
async def syndrome(ctx, user):
    syndrome_list = ["**Syndrome de Shisaku**, vous serez inattentif 🤔❓ pendant 3 minutes.",
                     "**Syndrome du Creeper qui a explosé la maison de Shisaku**, **💥  BOUM 💣**! Vous êtes SDF",
                     "**Syndrome de Shikamoto**, Vous êtes communiste ☭\n\nCitation :'Ce n'est pas ton chocolat. C'est notre chocolat parce que je suis communiste!",
                     "**Syndrome de Grizi**, Vous avez du mal à respirer pendant 30 secondes ⏲️.",
                     "**Syndrome de TheDragon et PouleQLF**, vous êtes maintenant un fan de **Nino Nakano**",
                     "**Syndrome d'Aīchīro**, vous êtes maintenant un fan de **Miku Nakano**",
                     "**Syndrome des Backrooms**, vous avez despawn 🍃.",
                     "**Syndrome de Mamie**, vous avez tout oublier 🤔(c'est le niveau 2 du syndrome de Shisaku)",
                     "**Syndrome du Quoi...**, vous répondez automatiquement de manière casse-couilles.",
                     "**syndrome de yun**, tu reçois un coup de jus ⚡ et une claque ✋"]
    random_syndrome = random.choice(syndrome_list)

    if user == "random":
        member_list = ctx.guild.members
        random_member = random.choice(member_list)
        await ctx.send(f"{random_member} à attraper le {random_syndrome}")
    else:
        await ctx.send(f"{user} à attraper le {random_syndrome}")


@bot.command()
async def say(ctx, *arg):
    await ctx.send("".join(arg))


@bot.command()
async def randominteger(ctx, nombre_de_depart, nombre_de_fin):
    nombre_generer = random.randint(int(nombre_de_depart), int(nombre_de_fin))

    await ctx.send(f"**{nombre_generer}**")


@bot.command()
async def randomdecimal(ctx, nombre_de_depart, nombre_de_fin):
    nombre_generer = random.uniform(int(nombre_de_depart), int(nombre_de_fin))

    await ctx.send(f"**{nombre_generer}**")


@bot.command()
async def randomsentence(ctx):
    sentence_list = ["Je t'aime bb", "Miko est gay", "Nino supremacy",
                     "Est-ce que t'as 10 millions de puissances sur Rise of Kingdom?", "Je passe",
                     "Les fans de miku Nakano doivent allez consulter le médecin tout de suite. De Thedragon",
                     "Quoi ?\n*(vas-y lache-toi)*", "m'en fout", "Il faut 250g de chocolat pour faire un brownie", "😏",
                     "8 morts 6 blessés, je pète ma bière, ma...", "toujours kawainé toujours cute",
                     "Niko Niko Niko Knee !", "Bakabeboubaeuwushrekemodpressifàladarksasuke",
                     "Big Mac Whooper Burger King !", "Tu me parle pas d'âge à moi", "Arrête Loulouteeeuuh",
                     "Watashiwa your mother et je vais lancer **la claquette magique** !", "Je me sabre le champagne",
                     "Raiha à 14 ans Pas Touche ! Même si elle est mature."]
    game = random.choice(sentence_list)

    await ctx.send(game)


@bot.command()
async def pile_face(ctx):
    pile_face_list = ["Pile", "Face"]
    game = random.choice(pile_face_list)

    await ctx.send(game)


@bot.command()
async def popogame(ctx):
    wallet = 100
    potion_stock = 0

    condition = True

    while condition == True:

        affichage = await ctx.send(f"Vous avez **{potion_stock} potions** et **{wallet} or**.\n\n\nVeuillez réagir avec 💲 pour acheter.          1 potion = 2 or     si vous saisissez acheter vous acheterez un nombre de potion random entre 1 et le maximum\nVeuillez réagir avec 💰 pour vendre.          1 potion = 5 or     si vous saisissez vendre vous vendrez un nombre de potion random entre 1 et le maximum\n\nVeuillez réagir avec ❌ pour annuler.")

        await affichage.add_reaction("💲")
        await affichage.add_reaction("💰")
        await affichage.add_reaction("❌")

        reaction, user = await bot.wait_for("reaction_add", timeout=60)

        if wallet < 1000000:
            if reaction.emoji == "💲":
                random_buy = random.randint(1, wallet // 2)
                potion_stock += random_buy
                wallet -= random_buy * 2
                await ctx.send(f"Vous avez réussi à acheter {random_buy} potions !")
            elif reaction.emoji == "💰":
                random_sell = random.randint(0, potion_stock)
                potion_stock -= random_sell
                wallet += random_sell * 5
                await ctx.send(f"Vous avez réussi à vendre {random_sell} potions !")
            elif reaction.emoji == "❌":
                await ctx.send("Commande annulée")
                break
            else:
                await ctx.send("Cette option n'existe pas...")
        else:
            await ctx.send(f"**BRAVO !** Vous avez dépassé les **1 MILLIONS** d'or. Vous avez fini le jeu !\n\nVotre score : **{wallet}**")
            break

@bot.command()
async def stickgame(ctx):
    stick_list = ""
    for i in range(0, 16):
        stick_list += "┃"

    await ctx.send(f"Les règles du jeu sont très simple :\n\nAu départ il y a 16 bâtons, le but est de ne pas être celui qui arrivera à 0\nvous pouvez les retirer par 1, 2 ou 3\n\nVeuillez réagir avec ❌ pour annuler.")

    while True:
        if len(stick_list) == 0:
            await ctx.send("Il n'y a plus de bâtons PERDU !")
            break
        else:
            affichage = await ctx.send(f"Il y a {stick_list} bâtons")

            await affichage.add_reaction("1️⃣")
            await affichage.add_reaction("2️⃣")
            await affichage.add_reaction("3️⃣")
            await affichage.add_reaction("❌")

            reaction, user = await bot.wait_for("reaction_add", timeout=60)

            if reaction.emoji == "1️⃣":
                stick_list = stick_list[:-1]
            elif reaction.emoji == "2️⃣":
                stick_list = stick_list[:-2]
            elif reaction.emoji == "3️⃣":
                stick_list = stick_list[:-3]
            elif reaction.emoji == "❌":
                await ctx.send("Commande annulée")
                break
            else:
                await ctx.send("Cette option n'existe pas...")



@bot.command()
async def caps(ctx):
    embed_name = discord.Embed(title="")
    embed_name.add_field(name="", value="**Veuillez donner un nom à votre Time Capsule**", inline=False)
    await ctx.send(embed=embed_name)

    def get_author_id():
        author_id = ctx.author.id
        return author_id

    def check(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    name = await bot.wait_for("message", timeout=30, check=check)
    embed_name_return = discord.Embed(title="")
    embed_name_return.add_field(name="", value=f"Vous avez choisi le nom : {name.content}", inline=False)
    await ctx.send(embed=embed_name_return)

    embed_timer = discord.Embed(title="")
    embed_timer.add_field(name="", value="**Veuillez renseigner un temps de décompte avant l'ouverture de la Time Capsule (en secondes)**", inline=False)
    await ctx.send(embed=embed_timer)
    counter = await bot.wait_for("message", timeout=30, check=check)

    async def countdown(ctx, counter):
        caractere_interdit = re.compile("[@#:!;,/§.?()+=*abcdefghijklmnopqrstuvwxyzABCDEFGHIJQLMNOPQRSTUVWXYZ]")
        if caractere_interdit.search(counter.content):
            print("Votre compteur comporte un ou plusieurs caractères non valide, veuillez en saisir un qui l'est: '@#:!;,/§.?()+=*abcdefghijklmnopqrstuvwxyzABCDEFGHIJQLMNOPQRSTUVWXYZ'")
        else:
            embed_timer_return = discord.Embed(title="")
            embed_timer_return.add_field(name="", value=f"Vous avez choisi un décompte de {counter.content} secondes", inline=False)
            await ctx.send(embed=embed_timer_return)
            return int(counter.content)

    count = await countdown(ctx, counter)
    objectlist = []
    ping = []

    caps = TimeCapsule(bot=bot, name=name, objectlist=objectlist, countdown_before_opening=count, author_id=get_author_id(), ping=ping)
    await caps.choose_an_action(ctx)

@bot.command(name="gif")
async def random_gif(ctx):
    await ctx.send(random.choice(links[ctx.invoked_with]))

@bot.command()
async def member_list(ctx):
    members_id = []
    for member in ctx.guild.members:
        members_id.append(member.id)
        await ctx.send(f"Membre: `{member}`   ID: `{member.id}`")


@bot.command()
async def qrcode(ctx, url: str):
    if url == "":
        embed_error = discord.Embed(title="")
        embed_error.add_field(name="", value="Vous avez oublié l'url.", inline=False)
        await ctx.send(embed=embed_error)
    else:
        embed_qr = discord.Embed(title=f"Le QR code est prêt")
        embed_qr.set_image(url=f"https://api.qrserver.com/v1/create-qr-code/?size=450x450&data={url}")
    await ctx.send(embed=embed_qr)


@bot.command()
async def bam(ctx):
    start = time.monotonic()
    await ctx.send('Boum 💥')
    end = time.monotonic()
    duration_ms = (end - start) * 1000
    duration_sec = (duration_ms / 1000)
    duration_hour = duration_sec / 3600
    await ctx.send(f'Latence: **{duration_ms}** MilliSeconde   **{duration_sec}** Seconde   **{duration_hour}**')


@bot.command()
async def ip(ctx, member):
    print(f'{member.name} a rejoint le serveur {member.guild.name} (IP: {member.guild.get_member(member.id).guild.me.ip})')

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    embed = discord.Embed(title="User Information", color=member.color)
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name="Name", value=member.name, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Status", value=member.status, inline=True)
    embed.add_field(name="Top Role", value=member.top_role.name, inline=True)
    embed.add_field(name="Joined", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    embed.add_field(name="Created", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
    await ctx.send(embed=embed)

@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Veuillez mentionner un utilisateur ou utilisez la commande sans argument pour obtenir vos propres informations.")
    else:
        await ctx.send(f"Une erreur s'est produite : {str(error)}")


bot.run(token)
