import discord
from discord.ext import commands
import colorama 
import os
from colorama import Fore
client = commands.Bot(command_prefix = 'Mareczekkk Skid', help_command = None)

print('Please enter your username')
username = input()
if username == 'root':
    print('Welcome back! ' + username + ' Please enter your password')
    password = input()
    if password == 'root':
        print('ACCESS GRANTED')
    else:
        print('Incorrect Password!')
        print('ACCESS DENIED')
        exit()
else:
    print('Username not found')
    print('ACCESS DENIED')
    exit()

colorama.init()
token = input("Input Token>>")
@client.event
async def on_ready():
 os.system('cls')
 print(f'''
{Fore.LIGHTMAGENTA_EX}|  \/  |             |  __ \            |__   __|        | |
{Fore.LIGHTMAGENTA_EX}| \  / | __ _ ___ ___| |  | |_ __ ___      | | ___   ___ | |
{Fore.LIGHTMAGENTA_EX}| |\/| |/ _` / __/ __| |  | | '_ ` _ \     | |/ _ \ / _ \| |
{Fore.LIGHTMAGENTA_EX}| |  | | (_| \__ \__ \ |__| | | | | | |    | | (_) | (_) | |
{Fore.LIGHTMAGENTA_EX}|_|  |_|\__,_|___/___/_____/|_| |_| |_|    |_|\___/ \___/|_|
{Fore.RED} By ENDERMANQ
{Fore.LIGHTRED_EX} MassDM Tool = 1
''')
 fuck = input(f"{Fore.GREEN}Select : ")
 if fuck == '1':
  input2 = input(f"{Fore.RED}What Should I Send? : ")
  for user in client.user.friends:                
   await user.send(f"{input2}")
   print(f"{Fore.GREEN}[+] Successfully Sent{Fore.WHITE} {input2} To {user}")

client.run(token, bot = False)