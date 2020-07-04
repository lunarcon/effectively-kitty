import os
from colorama import Fore, Back, Style
import numpy as np
from PIL import Image
import sys
from time import sleep

location=[15,15]
os.system("mode con cols=153")
os.system("mode con lines=38")
try:
    height = os.get_terminal_size().lines - 3
    width = os.get_terminal_size().columns - 2
except:
    height=100
    width=100

def get_ansi_color_code(r, g, b):
    if r == g and g == b:
        if r < 8:
            return 16
        if r > 248:
            return 231
        return round(((r - 8) / 247) * 24) + 232
    return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)


def get_color(r, g, b):
    return "\x1b[48;5;{}m \x1b[0m".format(int(get_ansi_color_code(r,g,b)))

city=[]

def show_image(img_path):
    try:
        img = Image.open(img_path)
    except FileNotFoundError:
        exit('Image not found.')

    h = height
    w = int((img.width / img.height) * h)

    img = img.resize((w,h), Image.ANTIALIAS)
    img_arr = np.asarray(img)
    h,w,c = img_arr.shape
    for x in range(h):
        tim=""
        for y in range(w):
            pix = img_arr[x][y]
            tim += str((get_color(pix[0], pix[1], pix[2])))
        city.append(tim)



#show_image("roadasc.jpg")

city='''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓████
░░░▄██▄▄░░░░░▐█░░░░▐██░░░░██░░██████░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄█████▓█▒
░▄█▀░░░█▌░░░┌██▌░░░▐██░░░███░░█░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄██████▀▒▒▓
░█▌░░░,,,░░,█▀░█▄░░▐█▀█░▐█▐█░░██████░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████▀▒▒▒
░██░░░░██░░█▀▀▀▀█▄░▐█░███░▐█░░█░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▌▒▒▒▒▒▒▒▒▒▒▒▒▒╢╢▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████▒▒▒▒▒▒▒▒
░░▀▀▀▀▀▀█░█▀░░░░▐█░▐█░░█▀░▐█░░██████░░██▓████████████████████▓███████▓███████▓███▓████████████▓▓███▒╢▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄████████▒▒▒▒▒▒▒▒▒
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███████████████████████████████████████████████████████████████▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄████████████▒▒▒▒▒▒▒
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀██████▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████▀▒▒███████▄▒▒▒▒
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌╢▒▒▒▒╢▒▒▒▒▒▒▒▒▒▒▀███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢▒█▓█████▀▒▒▒▒▒▒▀███████   
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐██████████▓██▒╢▒▒▒▒▒▒▒▒▒███████▒╢▒▒▒▒▒▒▒▒▒▒▒▒▒▄█▓███▓█▒▒▒▒▒▒▒▒▒▒▒▀█████ E 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐███████████████▒▒▒▒▒▒▒▒▒▒▒█▓█████▄╢▒╢▒▒▒▒╢▒▒▄██████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓█ N 
░░░░░░░░░░░░░░░,,,,░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▓▀▒▒▒▒▀█████▒▒▒▒▒▒▒▒▒▒▒▒▀███████████▓████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█ D 
░░░░░░░░░░,∞"░░░░░░░░"N,░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒? ▒▒█████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▀████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█   
░░░░░░░░▄▀░░░░░░░░░░░░░░▀▄░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐███▓█▄▒▒▒▒▄█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▀▒▒▒▀██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░░▄░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐█▓████▓██▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╟████▌▒▒? ▒▒█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░▐░░░░░░░░░░░░░░░░░░░░▌░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐███▓███████▓█▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐█████▄▒▒▒▒▄████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░█░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████▓████▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░▐░░░░░░░░░░░░░░░░░░░░▌░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄████▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░░█░░░░░░░░░░░░░░░░░░▄░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒╢▒█▓██████████▒╢▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄█████▓█▒▒▒▒▀▀▒▒▒▒█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░░░▀░░░░░░░░░░░░░░░░█░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒╢███████▀▀███████╢▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄██████▀▒▒▒▒▒▒▒▒▒▒▒▒╢▒▀██████▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░░░░░▀▄░░░░░░░░░░▄▀░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▐█████▒▒▒▒▒▒█████Ü▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▓█▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░░░░░░░░ "ⁿ══ⁿ"`░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▐█████╢▒▒? ▒█████▌▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒▒█████▌▄▄▄▄▄▄▄▄▄█████▌▄▄▄▄▄▄▄▄▄▄▄▄▄███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢▒█▀▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░collect the '?'s for bonuses! ░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▀███████████████████████████████████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢▒▀░█▓█▓█▄▒▒▒▒▒▒▒▒▒▒
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀█████▓█▓█▓▓███████████▓▓▓▓████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▄▒▒▒▒▒▒▒▒
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▌▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀███████▒▒▒▒▒▒
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓█▓▓▌▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢▒███████▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢▒█▓█████▒╢▒▒
░░░░HELP KITTY REACH THE END!░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▌▒▒▒▒▒▒▒▒▒▐███▓▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢▒▀▓████████████████████████████████████████████████
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████M▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀█▓█████████████████████████████████████████████
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ███████████████████████████▀╢▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢▒▒▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀█▀▀▀▀▀▀█▀▀▀▀▀▀▀█▀▀▀▀▀▀█▀▀▀▀▀
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░START░  ██████████████████████▓▓█▀▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░Use as many moves as possible░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░in a single command for best score░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐████▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒'''.replace("▓","█").split("\n")

chara='''
 /\\_/\\ 
( o.o )
 > ^ < 
'''.replace("▓","░").split("\n")

youwin='''

 ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
 ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
  ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
   ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
    ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
    ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
    SCORE 000 | RESTARTING...
'''.split("/n")
youlose='''

██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝
   SCORE 000 | RESTARTING...
'''.split("\n")

bck=[]
bkg=[]

score=0

def print_center(s):
    print(' ' * ((width + 2 - len(s))//2) + s)

    
ba = "░"*(width)
for i in range(0, height):
    bck.append(ba)
    
cloc = [0,0]
for y in range(0,len(city)):
    bck[y+cloc[1]] = " " + bck[y+cloc[1]][0:cloc[0]].strip(" ") + city[y] + bck[y+cloc[1]][cloc[0] + len(city[y]):].strip(" ")
    
for i in bck:
    bkg.append(i)

def goto_pos():
    for y in range(0,len(chara)):
        bkg[y+location[1]] = bck[y+location[1]]
        bkg[y+location[1]] = " " + bkg[y+location[1]][0:location[0]].strip(" ") + Fore.CYAN + chara[y] + Style.RESET_ALL + bkg[y+location[1]][location[0] + len(chara[y]):].strip(" ")
    os.system("cls")
    print("")
    for k in bkg:
        print_center(k)
    print("")
    
goto_pos()

def mbox(msg):
    os.system("cls")
    if msg=="YOU WIN":
        for b in youwin:
            if score==999:
                print_center(b.replace("000",(str(score)+ " | hmmm. did you use the code?")))
            else:
                print_center(b.replace("000",str(score)))
    else:
        for i in youlose:
            print_center(i.replace("000",str(score)))
    sleep(3)

while True:
    delta=input(" move me around! (you can input lots of characters and repeat characters) w/a/s/d> ").strip(" ")
    if delta.strip():
        if delta != "wwssadadba":
            score += len(delta)-5
            for tp in delta:
                if tp == "w":
                    if location[1] > 2:
                        location[1] -= 1
                elif tp == "a":
                    if location[0] > 2:
                        location[0] -= 2
                elif tp == "s" and location[1] <= height-1:
                    location[1] += 1
                elif tp == "d" and location[0] <= width-len(chara[0])-10:
                    location[0] += 2
                else:
                    if location[1] in [6,7,8,9,10,11,12,13,14] and tp not in "qertyuiopfghjklzxcvbm":
                        mbox("YOU WIN")
                    else:
                        mbox("YOU LOSE")
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                try:
                    goto_pos()
                    bkg[8] = bkg[8].replace("000", "0" + str(score))
                    print(" SCORE", score)
                except:
                    print(" out of bounds!")
                    os.system("cls")
        elif delta == "wwssadadba":
            score= 999
            mbox("YOU WIN")
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    else:
        score -= 5
        os.system("cls")
        print(" SCORE", score)
        goto_pos()
