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

suffixes = '.?!,;:)]'

# set default choices
def choices(ch):
    global CHOICES
    if ch:
        CHOICES += ch
    return CHOICES

# clear the screen
def clear():
    if platform == "windows":
        os.system('cls')
    else:
        os.system('clear')

# take an entire message and extract the first automatic color, or return RESET
def color_of(msg):
    words = msg.split() # break our message into words
    msg = ''
    for i in range(len(words)):
        suffix = ''
        repeat = False
        while True:
            # don't include certain symbols (periods, commas, etc.) as part of word
            for suf in suffixes:
                if words[i].endswith(suf):
                    suffix = suf + suffix # append suffix to our combined suffix string
                    words[i] = words[i][:-1] # cut suffix symbol from word
                    repeat = True
                    break
            if repeat: # allow more than one suffix symbol (ex. '...')
                continue
            break
            
        try:
            return COLORS[words[i]]
        except KeyError:
            pass
    return RESET

# auto-colorize words based on colors()
def colorize(msg):
    words = msg.split() # break our message into words
    msg = ''
    for i in range(len(words)):
        suffix = ''
        col = ''
        repeat = False
        while True:
            # don't include certain symbols (periods, commas, etc.) as part of word
            for suf in suffixes:
                if words[i].endswith(suf):
                    suffix = suf + suffix # append suffix to our combined suffix string
                    words[i] = words[i][:-1] # cut suffix symbol from word
                    cont = repeat
                    break
            if repeat: # allow more than one suffix symbol (ex. '...')
                continue
            break
            
        word = words[i]
        try:
            word = COLORS[words[i]] + words[i] + RESET
        except KeyError:
            pass
        word = word.replace('_', ' ')
        words[i] = word + suffix # put the non-colored suffix string back on the word
    return ' '.join(words)

# print with colorization
def out(msg):
    print(colorize(msg))

# a colorized choice menu
def choice(choices):
    choices += CHOICES # append default choices, like use item and quit
    for ch in choices:
        # color the character choice based on color of associated text
        col = color_of(ch[1])
        out('(' + col + ch[0] + RESET + ') ' + ch[1])
            
    # append character choices for prompt
    letters = '/'.join(map(lambda x: color_of(x[1]) + x[0] + RESET, choices))

    # repeat the choice until we get something valid
    while True:
        c = input('Choice ('+letters+'): ')
        for ch in choices:
            if c == ch[0]:
                return ch[2]

# main room loop, pass in a function to start
def start(room):
    last_room = None
    args = {}
    while room:
        clear()
        back = last_room
        last_room = room

        # call the current room function
        args['back'] = back
        args['room'] = room
        room = room(**args)

        # if the returned room is a tuple, extract the room and args from it
        if isinstance(room,tuple):
            # args contain certain information we need while entering the room,
            # such as the previous room and used items
            args = room[1] if room[1] else {}
            room = room[0]
        else:
            args = {}

# set magic word colors
def colors(**colordict):
    global COLORS
    COLORS = colordict

# Previous room function, can be used to return to the previous room when
# returned from a room.
# Only works once since there is only a single room history contained in a room's
# keyword args ('kwargs')
def back(args, **kwargs):
    if kwargs:
        return (args.get('back'), kwargs)
    else:
        return args.get('back')

def pause(msg=None): 
    if msg==None:
        print("Press ENTER to continue...")
        input()
        return
    input(msg)

