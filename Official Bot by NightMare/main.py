import os
import discord
import os
import requests
import json
import asyncio
import discord.ext
from discord.utils import find
from discord.ext import commands, tasks
import webserver
from webserver import keep_alive

intents = discord.Intents.all()
client=commands.Bot(command_prefix="", intents=intents,case_insensitive=True)
client.remove_command('help')

snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_member_join(member):
  guild = client.get_guild(946307290099761193) 
  channel = guild.get_channel(1025809358103257128) 
  message = await channel.send(f"{member.mention} welcome to .gg/originop")

@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.content.startswith('tag'):
    await message.reply(f"\<a:blackdot:969225953832222761> **Put our vanity in Your About me.**              <a:blackdot:969225953832222761>")
  if message.content.startswith('Tag'):
    await message.reply(f"<a:blackdot:969225953832222761> **Just add <$ in your username** <a:blackdot:969225953832222761>")  
  if message.mention_everyone:
    if message.guild.me.top_role.position >= message.author.top_role.position:
      await message.delete()  
      await message.channel.send(f"No Pings {message.author.mention}")
  if 'http' in message.content or 'www.' in message.content:
    if message.guild.me.top_role.position >= message.author.top_role.position:
      await message.delete()
      await message.channel.send(f"No Links allowed!")      
  if 'discord.gg' in message.content:
    if message.guild.me.top_role.position >= message.author.top_role.position:
      await message.delete()
      await message.channel.send(f"No Links allowed!") 

@client.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    channel_info = [ctx.channel.category, ctx.channel.position]
    await ctx.channel.clone()
    await ctx.channel.delete()
    embed=discord.Embed(title=f'Origin Base', color=0x2f3136, timestamp=ctx.message.created_at)
    embed.set_image(url="")
    embed.set_footer(text=f"Channel Nuked by {ctx.author}")
    new_channel = channel_info[0].text_channels[-1]
    await new_channel.edit(position=channel_info[1])
    await new_channel.send(embed=embed)
    embed.set_image(url="https://cdn.discordapp.com/attachments/975563704974344212/977600578131734669/xll2CW9.png")
    embed.set_footer(text=f"Channel Nuked by {ctx.author}")
    new_channel = channel_info[0].text_channels[-1]
    await new_channel.edit(position=channel_info[1])
    await new_channel.send(embed=embed)         
@client.command()
async def help(ctx):
  embed = discord.Embed(title='<a:Diamond:969240854919262218>**__/originop__**', description=f'<:a_:967354219629785138>**__Commands:__**\n\n **Prefix is Non**\n\n<a:blackdot:969225953832222761>**sync** - syncs official role(Admin Must)\n**<a:blackdot:969225953832222761>official** - used to give official role to members (Admin Must)\n<a:blackdot:969225953832222761>**Mute** - Removes all channles access \n<a:blackdot:969225953832222761>**Ban** - Bans user (Admin Must)\n**<a:blackdot:969225953832222761>officialcount** - shows count of supporters\n**<a:blackdot:969225953832222761>membercount** - shows count of members in server\n<a:blackdot:969225953832222761>**Snipe** - Snipes msg\n<a:blackdot:969225953832222761>**ping** - shows bot latency\n<a:blackdot:969225953832222761>**!mod / perms /head /admin /manager (Head Admins only)**', color=0x2f3136)
  await ctx.reply(embed=embed)

@client.command()
async def dinfo(ctx):
  embed = discord.Embed(title='<a:Diamond:969240854919262218>**__/devloper info__**', description=f'**Devloper Info**\n\n<a:blackdot:969225953832222761>**Devloped By FelixCodeZ**\n<a:blackdot:969225953832222761>**Join Origin** - https://discord.gg/originop', color=0x2f3136)
  await ctx.reply(embed=embed)
  
@client.command()
async def cmds(ctx):
  embed = discord.Embed(title='<a:Diamond:969240854919262218>**__/originop__**', description=f'**Commands**\n\n**Can only be used by admins of Origin Base**\n\n<a:blackdot:969225953832222761>Mod\n<a:blackdot:969225953832222761>perms\n<a:blackdot:969225953832222761>head\n<a:blackdot:969225953832222761>admin\n<a:blackdot:969225953832222761>manager', color=0x2f3136)
  await ctx.reply(embed=embed)



@client.event
async def on_ready():
  print(f"Connected to /originop")
  channel = client.get_channel(1025809325580632196)
  activity = discord.Activity(type=discord.ActivityType.watching, name="basement of origin base")
  await client.change_presence(status=discord.Status.idle, activity=activity)



@client.command()
async def sync(ctx):
  guild = client.get_guild(946307290099761193)
  role = guild.get_role(1025809312683130890)
  memberrrr = 0
  if ctx.author.top_role.position > ctx.guild.me.top_role.position or ctx.author == ctx.guild.owner:
    try:
      for member in ctx.guild.members:  
        if '†ᴰᵒᵍˡᵃ' in str(member.name) or '<$' in str(member.name):
          memberrrr += 1
          await member.add_roles(role)
      await ctx.reply(f'Successfully added roles to {memberrrr} officials!')
    except:
      pass
  else:
    await ctx.send("You must have role above me to use this!")

@client.command()
@commands.has_permissions(administrator=True)
async def official(ctx, user: discord.Member):
  guild = client.get_guild(946307290099761193)
  role = guild.get_role(1025809312683130890)
  if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
    await user.add_roles(role)
    await ctx.send(f"{user.mention} got official role")
  else:
    await ctx.send(f"{user.mention} doesn't have tag")

@client.command()
@commands.has_permissions(administrator=True)
async def perms(ctx, user: discord.Member):
  guild = client.get_guild(946307290099761193)
  role = guild.get_role(1025809307016630393)
  if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
    await user.add_roles(role)
    await ctx.send(f"{user.mention} got perms")
  else:
    await ctx.send(f"{user.mention} doesn't have tag")

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, user: discord.Member):
  guild = client.get_guild(946307290099761193)
  role = guild.get_role(1025809307016630393)
  if '†ᴰᵒᵍˡᵃ' in str(user.name) or '†ᴰᵒᵍˡᵃ' in str(user.name) or '' in str(user.name):
    await user.add_roles(role)
    await ctx.send(f"{user.mention} removed all access + muted")
  else:
    await ctx.send(f"{user.mention} doesn't have tag")

@client.command()
@commands.has_permissions(administrator=True)
async def manager(ctx, user: discord.Member):
  guild = client.get_guild(946307290099761193)
  role = guild.get_role(1025809309935861810)
  if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
    await user.add_roles(role)
    await ctx.send(f"{user.mention} got manager role")
  else:
    await ctx.send(f"{user.mention} doesn't have tag")
    
@client.command()
@commands.has_permissions(administrator=True)
async def mod(ctx, user: discord.Member):
  guild = client.get_guild(946307290099761193)
  role = guild.get_role(1025809310611157065)
  if '†' in str(user.name) or '' in str(user.name) or '' in str(user.name):
    await user.add_roles(role)
    await ctx.send(f"{user.mention} got mod role")
  else:
    await ctx.send(f"{user.mention} doesn't have tag")
    
@client.command()
@commands.has_permissions(administrator=True)
async def head(ctx, user: discord.Member):
  guild = client.get_guild(946307290099761193)
  role = guild.get_role(1025809306010001499)
  if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
    await user.add_roles(role)
    await ctx.send(f"{user.mention} got Head Admin role")
  else:
    await ctx.send(f"{user.mention} doesn't have tag")
    
@client.command()
@commands.has_permissions(administrator=True)
async def admin(ctx, user: discord.Member):
  guild = client.get_guild(946307290099761193)
  role = guild.get_role(1025809308870529024)
  if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
    await user.add_roles(role)
    await ctx.send(f"{user.mention} got admin role")
  else:
    await ctx.send(f"{user.mention} doesn't have tag")
    
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    await user.ban(reason=reason)
    ban = discord.Embed(color=0x080004, 
        title=f"Banned: {user.name}!",
        description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.channel.send(embed=ban)
    await user.send(f"**You have been banned from {ctx.guild.name}, Reason: {reason}**")

@client.command()
async def snipe(ctx):
    channel = ctx.channel 
    try:
        snipeEmbed = discord.Embed(color=0x080004, timestamp=ctx.message.created_at, title=f"Sniped!", description = snipe_message_content[channel.id])
        snipeEmbed.set_footer(text=f"Deleted by {snipe_message_author[channel.id]}")
        await ctx.reply(embed = snipeEmbed)
    except:
        await ctx.reply(f"There are no deleted messages")

@client.command()
async def officialcount(ctx):
  guild = client.get_guild(946307290099761193)
  role = guild.get_role(967320816029147146)
  embed = discord.Embed(title="**Officials Count of /originop**",description=f"**{len(role.members)} officials!**", color=0x2f3136)
  await ctx.reply(embed=embed)

@client.command(aliases=["mc"])
async def membercount(ctx):
        online = 0
        offline = 0
        dnd = 0
        idle = 0
        bots = 0
        for member in ctx.guild.members:
            if member.status == discord.Status.online:
                online += 1
            if member.status == discord.Status.offline:
                offline += 1
            if member.status == discord.Status.dnd:
                dnd += 1
            if member.status == discord.Status.idle:
                idle += 1
            if member.bot:
                bots += 1
        embed = discord.Embed(
            title=ctx.guild.name,
            description=" **`%s`**'s **Member Info**" %
            (ctx.guild.name),
            color=color)
        embed.add_field(name=":Online: **Online Members**", value="`%s`" % (online), inline=False)
        embed.add_field(name=":offline:**Offline Members**",
                        value="`%s`" % (offline),
                        inline=False)
        embed.add_field(name=":idle:**Idle Members**", value="`%s`" % (idle), inline=False)
        embed.add_field(name=":dnd:**DnD Members**",
                        value="`%s`" % (dnd),
                        inline=False)
        embed.add_field(name=":bots:**Bots**", value="`%s`" % (bots), inline=False)
        embed.add_field(name=":Members:**Total Members**",
                        value="`%s`" % (len(ctx.guild.members)),
                        inline=False)
        embed.set_footer(text=f"")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


keep_alive()
client.run(os.getenv('token'))      
