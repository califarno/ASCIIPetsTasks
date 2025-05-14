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
    

    time.sleep(1/60)
    clear_term()

url = 'https://app-pets.azurewebsites.net'

def trigger_next_animal(value):
    requests.put(url + "/values/0", json={ "value": str(value)} )

if __name__ == '__main__':

    trigger_next_animal(0)
    for i in range(165):
        print_aardvark(i)

    trigger_next_animal(1)



    

while True:
    response = requests.get(url + '/values/0')
    value = json.loads(response.content)
    time.sleep(1/40)
    if value == "0":
        for i in range(200):
            print_aardvark(i)
        
