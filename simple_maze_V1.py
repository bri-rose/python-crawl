#!/usr/bin/env python3
#
#  simple_maze_V1.py
#  
#  Copyright 2025 brielle <brielle@antix1>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.



import sys


def main(args):	
    return 0

## maze map
#     *
#     |
#    -
#   |
#   @

## building the maze
room_one = {
  "north": 1,
  "south": -1,
  "east": 0,
  "west": 0
}

room_two = {
  "north": 0,
  "south": -1,
  "east": 1,
  "west": 0
}

room_three = {
  "north": 1,
  "south": 0,
  "east": 0,
  "west": -1
}

print("Welcome to Brielle's Maze!")

print("what is your name?")

user_id = input()

print("So then, you are " + user_id +".")
print("Welcome.")

## building user profile
player = {
  "name": user_id,
  "room": 0
}


print("")
print("~~~")
print ("")

loc = player.get("room")

if loc == 0:
  print("Here you are, at the beginning. Go through.");
  player = {
    "room": 1
  }
print(player.get("room")

# function to establish current room exits
def room_exits():
	
# function to interpret and respond directional input


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:])) 
