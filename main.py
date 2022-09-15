import requests
import random
import shutil

from colorama import init, Fore
from PyTerm import Console

width = shutil.get_terminal_size().columns
init(autoreset=True)
Console.clear()

print(f"""{Fore.LIGHTMAGENTA_EX}

                 '
            *          .
                   *       '
              *                *
      _ _|_  _   _. ._ _    ._   _  |
     _>  |_ (/_ (_| | | |   |_) (_) |<
                            |
       '*
           *
                *
                       *
               *
                     *
\n""")


webhook = input('Webhook: ')
length = input('Length: ')


while True:
    id = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(int(length)))
    r = requests.get(f'https://steamcommunity.com/id/{id}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'},)

    if 'The specified profile could not be found.' in r.text:
        print(f'{Fore.LIGHTGREEN_EX}ID: {id} is available!')
        requests.post(webhook, json={'content': f'\🌠 New ID available "[`{id}`](<https://steamcommunity.com/id/{id}>)"\n\nremember that it may be **blacklisted**'})
    else:
        print(f'{Fore.LIGHTRED_EX}ID: {id} is taken!')
