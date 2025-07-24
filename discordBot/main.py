import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import random
import re
import base64
import os
import urllib.parse

# Load tokens from environment
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
VT_API_KEY = os.getenv('VT_API_KEY')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  
bot = commands.Bot(command_prefix='!', intents=intents)

# --- Security Tips ---
cyber_tips = [
  "🔐 Always use multi-factor authentication.",
  "📧 Watch out for phishing emails — check sender and links!",
  "💾 Keep your software and OS updated.",
  "📱 Don't reuse passwords — use a password manager.",
  "🛡️ Review the [OWASP Top 10](https://owasp.org/www-project-top-ten/) for common security issues."
]

ctf_challenges = [
    {"name": "SQL Injection", "path": "SQLInjection"},
    {"name": "Server-Side Request Forgery", "path": "SSRF"},
    {"name": "Web Authentication", "path": "WebAuth"},
    {"name": "Server-Side Scripting", "path": "XSS"}
]

# --- Commands ---

@bot.event
async def on_ready():
  print(f'✅ Logged in as {bot.user}')

@bot.command()
async def ipInfo(ctx, ip: str):
  url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
  headers = {"x-apikey": VT_API_KEY}
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    data = response.json()
    rep = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
    await ctx.send(f"📍 IP: {ip}\n🛡️ Harmless: {rep.get('harmless')}, Malicious: {rep.get('malicious')}")
  else:
    await ctx.send("❌ Could not fetch IP info.")

@bot.command()
async def linkInfo(ctx, *, raw_url: str):
  try:
    url_id = submit_url(raw_url)
    stats = get_url_report(url_id.removeprefix("u-"))
    # Send summary to Discord
    await ctx.send(
      f"🔍 URL: {raw_url}\n"
      f"🟢 Harmless: {stats.get('harmless')}\n"
      f"🟡 Suspicious: {stats.get('suspicious')}\n"
      f"🔴 Malicious: {stats.get('malicious')}\n"
      f"⚫ Undetected: {stats.get('undetected')}"
    )

    # Send summary to Discord
  except requests.HTTPError as e:
    await ctx.send(f"❌ Error checking URL: {e}")

def submit_url(raw_url):
    url = "https://www.virustotal.com/api/v3/urls"
    headers = {
        "x-apikey": VT_API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = f"url={raw_url}"

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()  # Raises HTTPError on bad request

    # Encode URL as per VirusTotal spec for the GET report
    encoded_url = base64.urlsafe_b64encode(raw_url.encode()).decode().strip("=")
    return encoded_url

def get_url_report(encoded_url_id):
    url = f"https://www.virustotal.com/api/v3/urls/{encoded_url_id}"
    headers = {
        "x-apikey": VT_API_KEY
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    stats = response.json().get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
    return stats

@bot.command()
async def ctf(ctx):
    challenge = random.choice(ctf_challenges)
    title = challenge["name"]
    path = challenge["path"]
    readme = fetch_readme(path)
    
    await ctx.send(f"🧩 **CTF Challenge: {title}**\n```md\n{readme}\n```")


@bot.command()
async def cybertip(ctx):
  tip = random.choice(cyber_tips)
  await ctx.send(f"💡 Security Tip:\n{tip}")

@bot.event
async def on_message(message):
  BAD_WORDS = ["free nitro", "click here", "spam", "scam", "malware"]
  if message.author == bot.user:
      return
  for word in BAD_WORDS:
    if word in message.content.lower():
      await message.delete()
      await message.channel.send(
        f"🚨 Message from {message.author.mention} was removed for containing suspicious content."
      )

  await bot.process_commands(message)


def fetch_readme(challenge_path):
    raw_url = f"https://raw.githubusercontent.com/Outpacing82/Ctfs-and-discord-bot/main/CTF/{challenge_path}/README.md"
    response = requests.get(raw_url)
    if response.status_code == 200:
        return response.text[:1900]  # Limit to Discord's 2000 char max
    else:
        return "README not found or failed to fetch."

bot.run(token)
