import random
import time
import requests
import string
import re
import os
from bs4 import BeautifulSoup
from colorama import Fore
from os import system, name

working = []


link = "https://streamable.com/"
length = 6
ctTag = 'h1'
ctText = 'Oops!'
characterList = string.ascii_lowercase + string.digits
workingFile = open('working.txt', 'a')

def mainLogo():
    print(Fore.MAGENTA)
    print("""
                                                                                          ,-,
                                                                                    _.-=;~ /_
                                                                                _-~   '     ;.
                                                                            _.-~     '   .-~-~`-._
                                                                        _.--~~:.             --.____88
                                                    ____.........--~~~. .' .  .        _..-------~~
                                            _..--~~~~               .' .'             ,'
                                        _.-~                        .       .     ` ,'
                                    .'                                    :.    ./
                                    .:     ,/          `                   ::.   ,'
                                .:'     ,(            ;.                ::. ,-'
                                .'     ./'.`.     . . /:::._______.... _/:.o/
                                /     ./'. . .)  . _.,'               `88;?88|
                            ,'  . .,/'._,-~ /_.o8P'                  88P ?8b
                            _,'' . .,/',-~    d888P'                    88'  88|
                        _.'~  . .,:oP'        ?88b              _..--- 88.--'8b.--..__
                        :     ...' 88o __,------.88o ...__..._.=~- .    `~~   `~~      ~-._ Seal _.
                        `.;;;:='    ~~            ~~~                ~-    -       -   -
                                              PrivacyInvaderPro+    
                                              (PLS DONT SUE ME)    
                                              @llumix on discord                                                                         
""")

def endLogo():
    print(Fore.MAGENTA)
    print("""
            _,-='"-.__               /\_/\\
            `-.}       `=._,.-==-._.,  @ @._,
                `-.__   _,-.   )       _,.-'
                    `"     G..m-"^m`m'     BYE BYE! Click ENTER to end.   

""")

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def checkForCt(url, content_tag, content_text):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        element = soup.find(f"{content_tag}.{content_text}")

        #  the entire html for inspection
        soup.prettify()

        # chek if the element is present and contains the expected text
        if element and content_text.lower() in element.text.strip().lower():
            # print("Username unavailable")
            return False
        else:
            # print("Username available")
            return True
    except requests.exceptions.RequestException as e:
        # print(f"Error: {e}")
        return False

def add_keyword(text, keyword):
    return f"{keyword}{text}"

def generateCode():

    password = []
    for i in range(6):
        randomchar = random.choice(characterList)
        password.append(randomchar)
        code = ''.join(password)
        final_link = add_keyword(code, link)
        idk = checkForCt(final_link, ctTag, ctText)

    if idk:
        print(Fore.GREEN)
        print("[Valid]", final_link)
        working.append(final_link)

        workingFile.write(str(final_link))
        workingFile.write('\n')
        workingFile.close()
    else:
        print(Fore.RED)
        print("[Invalid] ", final_link) 

clear()
mainLogo()
print(Fore.YELLOW)

amount = input("Amount of Streamable links to generate: ")

if amount.lower() != "inf":
    try:
        amount = int(amount)
        for _ in range(amount):
            generateCode()
    except ValueError:
        print("Please enter a valid number or 'inf' for infinite links.")
else:
    while True:
        generateCode()

print(Fore.YELLOW)
print("             WORKING")
print("            ---------")
print("\n".join(working))



input()
clear()

endLogo()
input()

clear()
workingFile.close()
"""
def test_link(linky):
    try:
        response = requests.get("https://" + linky)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        return False

def check_oops(linky):
    response = requests.get("https://" + linky)
    headers = response.headers
    if "oops" in headers["Content-Type"]:
        return True
    else:
        return False

working = []
workingamt = 0
at = 0
for linky in gen():
    print(f"https://streamable.com/{linky}", end = ' | ')
    at = at + 1
    print( f"{at}/{amount}", end = " | ")
    if test_link(linky) and not check_oops(linky):
        print("The link works")
        working = working + [linky]
        workingamt = workingamt + 1
    else:
        print("The link does not work")

print(f"Generated: {amount}\n Working: {workingamt}")
print(working)
input("Press ENTER to close.")
"""
