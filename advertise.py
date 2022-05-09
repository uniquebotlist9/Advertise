#!/usr/bin/env python
# -*- coding: UTF-8 -*-
v_=1.0

import discord, ctypes, requests, os, time, asyncio
from pystyle import Colors, Colorate, Center
from discord.ext import commands
import logging

logging.basicConfig(level=logging.CRITICAL, format=(Colorate.Vertical(Colors.red_to_black, "%(asctime)s | %(message)s")), datefmt="%I:%M:%S")
logging.getLogger().setLevel(logging.CRITICAL)
ctypes.windll.kernel32.SetConsoleTitleW(f"Advertise | {v_} | Startup")
os.system("mode 90, 45")




bot = commands.Bot(self_bot=True, command_prefix=".")

def ascii():
    os.system("cls")
    a="""
▄▄▄· ·▄▄▄▄   ▌ ▐·▄▄▄ .▄▄▄  ▄▄▄▄▄▪  .▄▄ · ▄▄▄ .
▐█ ▀█ ██▪ ██ ▪█·█▌▀▄.▀·▀▄ █·•██  ██ ▐█ ▀. ▀▄.▀·
▄█▀▀█ ▐█· ▐█▌▐█▐█•▐▀▀▪▄▐▀▀▄  ▐█.▪▐█·▄▀▀▀█▄▐▀▀▪▄
▐█ ▪▐▌██. ██  ███ ▐█▄▄▌▐█•█▌ ▐█▌·▐█▌▐█▄▪▐█▐█▄▄▌
 ▀  ▀ ▀▀▀▀▀• . ▀   ▀▀▀ .▀  ▀ ▀▀▀ ▀▀▀ ▀▀▀▀  ▀▀▀ 
───────────────────────────────────────────────

"""
    print(Colorate.Vertical(Colors.red_to_black, Center.XCenter(a), 1))


@bot.event
async def on_connect():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Advertise | {v_} | Scraping...")
    channels_scraped=0
    friends_scraped=0
    sus1=0
    sus2=0
    channels_success=0
    friends_success=0
    channels_failed=0
    friends_failed=0

    for g_ in bot.guilds: # scrape
        for c_ in g_.channels:
            if c_.permissions_for(g_.me).send_messages and c_.type is discord.ChannelType.text:
                channels_scraped+=1
    for f_ in bot.user.friends:
        friends_scraped+=1
    logging.critical("Successfully finished scraping")
    logging.critical("Starting guild advertising")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Advertise | {v_} | Channels: 0/{channels_scraped} | Friends: 0/{friends_scraped} | Total: 0/{friends_scraped+channels_scraped}")

    for guild in bot.guilds: # guild
        ascii()
        logging.critical(f"Guild: {guild.name}")
        for channel in guild.channels:
            if channel.permissions_for(guild.me).send_messages and channel.type is discord.ChannelType.text:
                sus1+=1
                ctypes.windll.kernel32.SetConsoleTitleW(f"Advertise | {v_} | Channels: {sus1}/{channels_scraped} | Friends: {sus2}/{friends_scraped} | Total: {sus1+sus2}/{friends_scraped+channels_scraped}")
                try:
                    x=await channel.send(f"{message_channels}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||@everyone")
                    await asyncio.sleep(.5)
                    try:
                        await x.add_reaction("💥")
                        await x.remove_reaction("💥", bot.user)
                        logging.critical(f"+ | {channel.name}")
                        channels_success+=1
                    except Exception as E:
                        print(E)
                        logging.critical(f"- | {channel.name}")
                        channels_failed+=1
                except:
                    logging.critical(f"- | {channel.name}")
                    channels_failed+=1
        await asyncio.sleep(1)

    ascii() # friends
    logging.critical("Starting friend advertising")
    for friend in bot.user.friends:
        sus2+=1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Advertise | {v_} | Channels: {sus1}/{channels_scraped} | Friends: {sus2}/{friends_scraped} | Total: {sus1+sus2}/{friends_scraped+channels_scraped}")
        try:
            await friend.create_dm()
            await friend.send(f"{message_friends}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||<@{friend.id}>")
            logging.critical(f"+ | {friend.name}")
            friends_success+=1
            
        except:
            logging.critical(f"- | {friend.name}")
            friends_failed+=1
    await asyncio.sleep(1)

    ctypes.windll.kernel32.SetConsoleTitleW(f"Advertise | {v_} | Finished") # stats
    ascii()
    logging.critical("Finished...")
    time.sleep(.5)
    ascii()
    logging.critical("Stats:\n")
    logging.critical(f"Total channels: {sus1}")
    logging.critical(f"Channels successful: {channels_success}")
    logging.critical(f"Channels failed: {channels_failed}\n")
    logging.critical(f"Total friends: {sus2}")
    logging.critical(f"Friends successful: {friends_success}")
    logging.critical(f"Friends failed: {friends_failed}")
    input("")
    os._exit(1)



if __name__ == "__main__":
    ascii()
    logging.critical(f"Token:") # login
    token=input("")
    r=requests.get("https://discordapp.com/api/v9/users/@me", headers={"Authorization": token})
    if r.status_code!=200:
        logging.critical("Invalid token...")
        time.sleep(2)
        os._exit(1)
    ascii()

    logging.critical(f"Server message:")
    message_channels=input("")

    logging.critical(f"Friends message:")
    message_friends=input("")
    
    bot.run(token, bot=False)