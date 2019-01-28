# textadventure

Copyright (c) 2019 Grady O'Connell

Licensed under MIT License

A VERY minimal text adventure template for python, inspired by the way I programmed
them when I was a kid.

Each location is represented as a function.  You return another function to
move to that location.

Here's a few features:

- choice() menu
- clear() screen
- Location loop: Locations are functions, and returning another function takes you to that location.
- Returning to the previous location
- Auto-colorizing keywords in print function
- Add your own default choices like "use item" and "quit"
- Pass parameters to locations by returning a tuple instead of function (good for using keys with doors)
- Detect automatic coloring based on a string

