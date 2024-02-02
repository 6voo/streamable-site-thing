import random
import requests
import string
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
    # for mac and linux
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
            return True
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

def add_keyword(text, keyword):
    return f"{keyword}{text}"

def generateCode():

    password = []
    for i in range(6):
        random_char = random.choice(characterList)
        password.append(random_char)
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
