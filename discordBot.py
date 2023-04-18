import discord, requests, asyncio

token = "MTA5NTQwMDMyOTk0NTgyNTM2MQ.GeK03f.IZd010KVHnNvv3OsEg_gyJUTy-HdF0IxRRHzBU"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def botStart():
    print("Starting Discord bot")
    client.run(token)
    return

@client.event
async def apiNotifications():
    channel = client.get_channel(1095401554284122152)
    if requests.get("https://api.coingecko.com/api/v3/ping").status_code == 200:
        await channel.send("The sheet has successfully been updated.")
    else:
        await channel.send("CoinGecko API is not responding.")
    return

@client.event
async def on_ready():
    print(f"Login success")
    await apiNotifications()
    await client.close()
    return
