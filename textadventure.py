#!/usr/bin/python

import os, colorama
from sys import platform
colorama.init(autoreset=True)

# class Stats:
#     def __init__(self):
#         self.inventory = set()
#         self.room = {}

FG = colorama.Fore
BG = colorama.Back
STYLE = colorama.Style
COLORS = {}
# stats = Stats()
room = None
RESET = BG.RESET + FG.RESET
CHOICES = []

suffixes = '.?!'

def choices(ch):
    global CHOICES
    if ch:
        CHOICES += ch
    return CHOICES

def clear():
    if platform == "windows":
        os.system('cls')
    else:
        os.system('clear')

# take an entire message an extract the first automatic color, or RESET
def color_of(msg):
    words = msg.split()
    msg = ''
    for i in range(len(words)):
        suffix = ''
        repeat = False
        while True:
            for suf in suffixes:
                if words[i].endswith(suf):
                    suffix = suf + suffix
                    words[i] = words[i][:-1]
                    cont = repeat
                    break
            if repeat:
                continue
            break
            
        try:
            return COLORS[words[i]]
        except KeyError:
            pass
    return RESET

# auto-colorize words
def colorize(msg):
    words = msg.split()
    msg = ''
    for i in range(len(words)):
        suffix = ''
        repeat = False
        while True:
            for suf in suffixes:
                if words[i].endswith(suf):
                    suffix = suf + suffix
                    words[i] = words[i][:-1]
                    cont = repeat
                    break
            if repeat:
                continue
            break
            
        try:
            words[i] = COLORS[words[i]] + words[i] + RESET + suffix
        except KeyError: 
            words[i] = words[i] + suffix
    return ' '.join(words)

def out(msg):
    print(colorize(msg))

def choice(room, choices):
    choices += CHOICES
    for ch in choices:
        col = color_of(ch[1])
        out('(' + col + ch[0] + RESET + ') ' + ch[1])
            
    letters = '/'.join(map(lambda x: color_of(x[1]) + x[0] + RESET, choices))
    while True:
        c = input('Choice ('+letters+'): ')
        for ch in choices:
            if c == ch[0]:
                return ch[2]

def start(start):
    room = start
    last_room = None
    args = {}
    while room:
        clear()
        back = last_room
        last_room = room
        room = room(back=back)
        if isinstance(room,tuple):
            args = room[1]
            room = room[0]

def colors(**colordict):
    global COLORS
    COLORS = colordict

def back(args, **kwargs):
    if kwargs:
        return (args.get('back'), kwargs)
    else:
        return args.get('back')

