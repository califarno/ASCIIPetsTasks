import os
import sys
import time
import json
import requests

if sys.platform in ('linux', 'darwin'):
    CLEAR = 'clear'
elif sys.platform == 'win32':
    CLEAR = 'cls'
else:
    print('platform not supported', file=sys.stderr)
    exit(1)

def clear_term() -> None:
    os.system(CLEAR)


def print_aardvark(number_of_spaces):
    spaces = ' ' *  number_of_spaces
    print(spaces + "       _.---._    /\\")
    print(spaces + "    ./'       ""--`\//")
    print(spaces + "  ./              o \ ")     
    print(spaces + " /./\  )______   \__ \ ")
    print(spaces + "   / /  \ \  | |\ \ \ \ ")
    print(spaces + "   --    --  --  --  \ \ ")
    

    time.sleep(1/15)
    clear_term()
  

if __name__ == '__main__':

    for i in range(200):
        print_aardvark(i)

    trigger_next_animal()

url = 'https://app-pets.azurewebsites.net'

def trigger_next_animal():
    requests.put(url + "/values/0", json={ "value": "0"} )
    

while True:
    response = requests.get(url + '/values/0')
    value = json.loads(response.content)
    time.sleep(1/40)
    if value == "1":
        for i in range(200):
            print_aardvark(i)
        
