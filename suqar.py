import code
import ctypes
from datetime import datetime
import json
from colorama import Fore, Style
import os
import discord
import requests
import time
from requests import Session
from threading import Thread
from time import strftime, gmtime
from licensing.methods import Key, Helpers
from discord.ext import commands




def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


ctypes.windll.kernel32.SetConsoleTitleW(f"Multi Tool || 3rodi#0001")


def tokeninfo():
    global token
    token = str(input(Fore.MAGENTA + f"""\nToken > """))

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
    }

    cc_digits = {
        'american express': '3',
        'visa': '4',
        'mastercard': '5'
    }

    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)

    if res.status_code == 200:
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        user_id = res_json['id']
        avatar_id = res_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        phone_number = res_json['phone']
        email = res_json['email']
        mfa_enabled = res_json['mfa_enabled']
        flags = res_json['flags']
        locale = res_json['locale']
        verified = res_json['verified']
        
        language = languages.get(locale)
        creation_date = datetime.datetime.fromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        has_nitro = False
        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)

        if has_nitro:
            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            days_left = abs((d2 - d1).days)
        billing_info = []

        for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
            yy = x['billing_address']
            name = yy['name']
            address_1 = yy['line_1']
            address_2 = yy['line_2']
            city = yy['city']
            postal_code = yy['postal_code']
            state = yy['state']
            country = yy['country']

            if x['type'] == 1:
                cc_brand = x['brand']
                cc_first = cc_digits.get(cc_brand)
                cc_last = x['last_4']
                cc_month = str(x['expires_month'])
                cc_year = str(x['expires_year'])
                
                data = {
                    'Payment Type': 'Credit Card',
                    'Valid': not x['invalid'],
                    'CC Holder Name': name,
                    'CC Brand': cc_brand.title(),
                    'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                    'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }

            elif x['type'] == 2:
                data = {
                    'Payment Type': 'PayPal',
                    'Valid': not x['invalid'],
                    'PayPal Name': name,
                    'PayPal Email': x['email'],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }

                billing_info.append(data)

        print(f"""\n Basic Information:""")
        print(f"""           Username: {user_name}""")
        print(f"""           User ID: {user_id}""")
        print(f"""           Creation Date: {creation_date}""")
        print(f"""           Avatar URL: {avatar_url if avatar_id else ""}""")
        print(f"""           Token: {token}\n\n""")
        
        print(f""" Nitro Information:""")
        print(f"""           Nitro Status: {has_nitro}""")

        if has_nitro:
            print(f"""           Expires in: {days_left} day(s)\n\n""")
        else:
            print(f"""           Expires in: None day(s)\n\n""")

        print(f""" Contact Information:""")
        print(f"""           Phone Number: {phone_number if phone_number else ""}""")
        print(f"""           Email: {email if email else ""}\n\n""")

        if len(billing_info) > 0:
            print(f""" Billing Information:""")
            if len(billing_info) == 1:
                for x in billing_info:
                    for key, val in x.items():
                        if not val:
                            continue
                        print(Fore.RESET + '    {:<23}{}{}'.format(key, Fore.CYAN, val))

            else:
                for i, x in enumerate(billing_info):
                    title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                    print('    ' + title)
                    print('    ' + ('=' * len(title)))
                    for j, (key, val) in enumerate(x.items()):
                        if not val or j == 0:
                            continue
                        print(Fore.RESET + '        {:<23}{}{}'.format(key, Fore.CYAN, val))

                    if i < len(billing_info) - 1:
                        print('\n')

            print('\n')

        print(f""" Account Security:""")
        print(f"""           2FA/MFA Enabled: {mfa_enabled}""")
        print(f"""           Flags: {flags}\n\n""")
        print(f""" Other:""")
        print(f"""           Locale: {locale} ({language})""")
        print(f"""           Email Verified: {verified}""")

    elif res.status_code == 401:
        print(f"""          {Fore.RED } Invalid token""")
        time.sleep(2)

    else:
        print(f"""          {Fore.RED } An error occurred while sending request""")
        time.sleep(2)


def mass_report():
    tokennn = input("Token :")
    server_id = input("Gib die Server-ID ein: ")
    channel_id = input("Gib die Channel-ID ein: ")
    message_id = input("Gib die Message-ID ein: ")
    message = input("Gib die Meldung ein: ")
    custom = int(input("Threads :"))

    headers = {
        "authorization": tokennn,
        "content-type": "application/json"
    }

    data = {
        "channel_id": channel_id,
        "guild_id": server_id,
        "message_id": message_id,
        "reason": message
    }

    print("Starte Mass-Report...")
    time.sleep(1)

    for i in range(custom):
        response = requests.post("https://discord.com/api/v6/report", headers=headers, json=data)
        if response.status_code == 201:
            print(f"Report {i+1} gesendet.")
        else:
            print(f"Report {i+1} konnte nicht gesendet werden.")
        ctypes.windll.kernel32.SetConsoleTitleW(f"Sended: {i+1} | Failed: {i+1}")


def nuker():
                import asyncio
                from colorama import Fore
                import discord
                from discord.ext import commands

                intents = discord.Intents.all()
                intents.members = True
                client = commands.Bot(command_prefix='.', intents=intents)

                print()
                inputt = input(Fore.LIGHTBLACK_EX + "Discord Bot token > ")
                print()
                inputtt = input(Fore.LIGHTBLACK_EX + "message that sends in the channel > ")
                print()
                inputttt = input(Fore.LIGHTBLACK_EX + "message that sends everyone in the server privat > ")
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
                    print()
                    clear()
                    pass


def nitro_gen():
    import random
    upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letter = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'

    print()
    numbtogen = int(input(Fore.LIGHTBLACK_EX + 'How many codes? > '))
    check = input(Fore.LIGHTBLACK_EX + 'Wanna check the codes? (y/n) > ')
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
    valid_codes = []
            
    if check == 'y' :
        for x in range(int(numbtogen)):
            nitro = ''.join(random.sample(all, length))
            url = f"https://discord.com/api/v8/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
            response = requests.get(url)
            if response.status_code == 200:
                print(f'[{Fore.GREEN}+{Fore.RESET}] {Fore.GREEN}Valid > {Fore.WHITE}https://discord.gift/' + nitro + Fore.RESET)
                valid_codes.append(nitro)
            else:
                print(f'[{Fore.RED}+{Fore.RESET}] {Fore.RED}Invalid > {Fore.WHITE}https://discord.gift/' + nitro + Fore.RESET)
            
    if check == 'n' :
        for x in range(int(numbtogen)):
            nitro = ''.join(random.sample(all, length))
            print(f'[{Fore.RED}+{Fore.RESET}] {Fore.RED}Invalid > {Fore.WHITE}https://discord.gift/' + nitro + Fore.RESET)
    input()
    clear()
    pass


def id_to_token():
    import base64
    from colorama import Fore, init
    init()

    userid = input(Fore.LIGHTBLACK_EX + "Discord ID > ")
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print(Fore.LIGHTBLACK_EX + f'\n TOKEN FIRST PART : {encodedStr}')
    print()
    input()
    clear()
    pass


def webhook_spammer():
                print()
                webhook_url = input(Fore.LIGHTBLACK_EX + "Webhook-URL > ")

            # Einlesen der Nachricht über die Kommandozeile
                print()
                message = input(Fore.LIGHTBLACK_EX + "Message > ")

                print()
                amountt = int(input(Fore.LIGHTBLACK_EX + "amount >"))

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
                    input()
                    clear()
                    pass


def token_check():
                import json
                print()
                token = input(Fore.LIGHTBLACK_EX + "Token you wanna check > ")

                headers = {
                    "Authorization": token
                }

                response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)

                if response.status_code == 200:
                    user = json.loads(response.text)
                    print()
                    print(Fore.GREEN + f"The token is valid! Discord Username : {user['username']}#{user['discriminator']}.")
                    print()
                    input()
                    clear()
                    pass
                else:
                    print()
                    print(Fore.RED + "The token is not valid.")
                    print()
                    input()
                    clear()
                    pass


def token_gen():
                import random
                import string
                import base64
                print()
                N = input("how many you wanna generate > ")
                count = 0
                current_path = os.path.dirname(os.path.realpath(__file__))
                url = "https://discordapp.com/api/v6/users/@me/library"

                while(int(count) < int(N)):
                    tokens = []
                    base64_string = "=="
                    while(base64_string.find("==") != -1):
                        sample_string = str(random.randint(000000000000000000, 999999999999999999))
                        sample_string_bytes = sample_string.encode("ascii")
                        base64_bytes = base64.b64encode(sample_string_bytes)
                        base64_string = base64_bytes.decode("ascii")
                    else:
                        token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                    for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
                        count += 1
                        time.sleep(0.4)
                        tokens.append(token)

                    for token in tokens:
                        header = {
                            "Content-Type": "application/json",
                            "authorization": token
                        }
                        print(Fore.WHITE + f"[{Fore.RED}!{Fore.RESET}]{Fore.RED} Invalid : "+ Fore.WHITE + token + Fore.RESET)


def generate_fake_link():
                    import random
                    import string
                    time.sleep(0.2)
                    link = f"[{Fore.RED}+{Fore.RESET}] {Fore.RED}Invalid > {Fore.WHITE}https://www.netflix.com/redeem/{Fore.RESET}"
                    for i in range(11):
                        link += random.choice(string.ascii_lowercase)
                    return link



def success():
            from colorama import Fore, Style
            import time
            clear()
            while True:
                import base64
                import code
                import ctypes
                from datetime import datetime
                import json
                import msvcrt
                from licensing.methods import Key, Helpers
                import random
                import string
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
                print(Fore.LIGHTRED_EX + f"""                                                                                                                                                           
                                     _..._
                                   .'     '.      _
                                  /    .-""-\   _/ \\
                                .-|   /:.   |  |   |
                                |  \  |:.   /.-'-./
                                | .-'-;:__.'    =/
                                .'=  *=|3яσ∂ι_.='
                                /   _.  |    ;
                                ;-.-'|    \   \\          > discord.gg/suqar <
                                /   | \    _\  _\\          > Open Source <
                                \__/'._;.  ==' ==\\         
                                        \    \   |
                                        /    /   /
                                        /-._/-._/
                                        \   `\  \\
                                         `-._/._/                               
                            """)
                
                print_menu= Fore.LIGHTBLACK_EX + """
            ╔══════════════════════╦═════════════════════════╦═══════════════════════╦═══════════════════╗
            ║                      ║                         ║                       ║                   ║
            ║  (1) - Nitro Gen     ║  (5) - Id to Token      ║  (9) - Token Gen      ║  (13) - About Us  ║
            ║  (2) - Discord Nuke  ║  (6) - Webhook Spammer  ║  (10) - Token Info    ║  (14) - Exit      ║
            ║  (3) - Mass Dm       ║  (7) - Token Checker    ║  (11) - Netflix Gen   ║                   ║
            ║  (4) - Invalid       ║  (8) - INVALID          ║  (12) - Roblox Gen    ║                   ║
            ║                      ║                         ║                       ║                   ║
            ╚══════════════════════╩═════════════════════════╩═══════════════════════╩═══════════════════╝
                """
                print(print_menu)

                choice = int(input(Fore.LIGHTRED_EX + "[>] "))
                if choice < 1 or choice > 14:
                    print(Fore.RED + "Invalid choice. Please select a valid option.\n")
                    time.sleep(1)
                    input()
                    clear()
                    continue
                if choice == 1:
                    nitro_gen()

                elif choice == 2:
                    nuker()

                elif choice == 3:
                    mass_report()

                elif choice == 4:
                    print("No section found")
                    input()
                    clear()
                    pass

                elif choice == 5:
                    id_to_token()

                elif choice == 6:
                    webhook_spammer() 

                elif choice == 7:
                    token_check()

                elif choice == 8:
                    print("No section found")
                    input()
                elif choice == 14:
                    print()
                    print(Fore.RED + "Exiting...")
                    time.sleep(1)
                    break
                elif choice == 9:
                    token_gen()
                    input("Tokens are all fake!")
                    clear()
                    pass
                elif choice == 10:
                    tokeninfo()
                    input()
                    clear()
                    pass
                elif choice == 11:
                    many = int(input("How many codes > "))
                    for i in range(many):
                        print(generate_fake_link())
                    print()
                    input("Codes dont work! Its a Fake gen!")
                    clear()
                    pass

                elif choice == 12:
                    many = int(input("How many codes > "))
                    for i in range(many):
                        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                        time.sleep(0.2)
                        print(f"[{Fore.RED}+{Fore.RESET}] {Fore.RED}Invalid > {Fore.WHITE}{code}-{code}-{code}{Fore.RESET}")
                    print()
                    input("Codes dont work! Its a Fake gen!")
                    clear()
                    pass
                elif choice == 13:
                    print(Fore.RED + """
                            About Us!
                
                1. Code is selfmade and coded by 3яσ∂ι#0001
                2. I needed like 1 week to create this.
                3. License Keys are from auth.gg and you cannot share it.
                4. For any help please visit discord.gg/acio
                5. If you want to resell dm me.
                6. Made with Python code.
                """)
                    input()
                    clear()
                    pass


success()