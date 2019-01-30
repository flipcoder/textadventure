#!/usr/bin/env python
from textadventure import *

colors(
    Outside = FG.GREEN,
    House = FG.RED,
    Garage = FG.YELLOW,
    Basement = FG.CYAN,
    Car = FG.LIGHTRED_EX,
    Quit = BG.RED + FG.BLACK,
)

def welcome(**kwargs):
    out("Welcome!\n")
    pause()
    return house

def use(**kwargs):
    # TODO: get item to use
    clear()
    item = input('Which item? ')
    input()
    return (back(kwargs), {use: item})

basement_locked = True
def basement(**kwargs):
    if basement_locked:
        out("Basement is locked.")
        input()
        return back(kwargs)
    return back(kwargs)

# house_coin = True
def house(**kwargs):
    use_item = kwargs.get('item', None)
    out("You are in your House.")
    # if house_coin:
    #     out("You found a Coin!")
    #     house_coin = False
    #     coins += 1
    # else:
    #     out("There is nothing special here.")
    out("What would you like to do?")
    return choice([
        ('o', 'Go Outside', outside),
        ('g', 'Go to Garage', garage),
        ('b', 'Go to Basement', basement),
    ])

car_locked = True
def car(**kwargs):
    if car_locked:
        out("Your Car is locked.")
        input()
        return back(kwargs)
    return back(kwargs)

def quit(**kwargs):
    ch = input('Are you sure you want to quit (y/n)? ')
    if ch=='y' or ch=='Y':
        return None
    return back(kwargs)

def outside(**kwargs):
    out("You are Outside.")
    input()
    return None
    
def garage(**kwargs):
    out("You are in the Garage. You see a Car.")
    return choice([
        ('c', 'Get in Car', car),
        ('h', 'Go inside House', house),
    ])
    
choices([
    ('u', 'Use Item', use),
    ('q', 'Quit', quit)
])

if __name__=='__main__':
    start(welcome)

