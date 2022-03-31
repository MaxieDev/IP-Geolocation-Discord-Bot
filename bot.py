#Ips is against discord tos I have nothing to do with whatever you do with this. This is just for learning experience.
#Required Imports
from discord.ext import commands
import os, re, json, cogs, requests, discord

#Config
with open("config.json", "r") as confjson:
	configData = json.load(confjson)

token = configData["Token"]
prefix = configData["Prefix"]

client = commands.Bot(command_prefix = commands.when_mentioned_or(prefix), help_command = None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.playing, name = "Funny Funny"))#activity status
    print("Bot is now online!")

    @client.command()
    async def geolocate(ctx, ip):
            r = requests.get( url = f'https://ipinfo.io/{ip}/geo')#API
            embed = discord.Embed(title="Geolocation")
            embed.add_field(name="Ip", value=(r.json()["ip"]), inline=False)
            embed.add_field(name="City", value=(r.json()["city"]), inline=False)
            embed.add_field(name="Region", value=(r.json()["region"]), inline=False)
            embed.add_field(name="Country", value=(r.json()["country"]), inline=False)
            embed.add_field(name="Location", value=(r.json()["loc"]), inline=False)
            embed.add_field(name="Org", value=(r.json()["org"]), inline=False)
            embed.add_field(name="Timezone", value=(r.json()["timezone"]), inline=False)
            embed.color = discord.Color.blurple()
            await ctx.send(embed=embed)

    @client.command()
    async def help(ctx, cmd=None):
            embed = discord.Embed()
            embed.title = "Discord Bot Help / Dashboard"
            embed.add_field(name=":globe_with_meridians: **IP Location**", value="`geolocate`", inline=False)
            embed.set_thumbnail(url= ctx.guild.icon_url)
            embed.set_footer(text="Help Commands", icon_url = ctx.guild.icon_url)
            embed.color = discord.Color.blurple()
            await ctx.reply(embed=embed, mention_author=False)

#Token
client.run(token)#you put your bot token inside of config.json
