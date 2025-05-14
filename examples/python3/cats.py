#  pip3 install requests   
import sys
import os
import time
import json

url = 'https://app-pets.azurewebsites.net'

if sys.platform in ('linux', 'darwin'):
    CLEAR = 'clear'
elif sys.platform == 'win32':
    CLEAR = 'cls'
else:
    print('platform not supported', file=sys.stderr)
    exit(1)

def clear_term() -> None:
    os.system(CLEAR)

def hide_cursor():
    sys.stdout.write(f"\033[{40};{0}H")
    sys.stdout.flush()

def print_at_location(col,row,text):
    sys.stdout.write(f"\033[{row};{col}H")
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

def animate_cat():
    width = os.get_terminal_size().columns
    # draw the pet