# -*- coding: utf-8 -*
import os
os.chdir(r"C:\Users\mbaya\OneDrive\Documents\python\Projet_3")

laby =[] #We create a empty list

with open("levels.txt") as levels: 
    for line in levels: #For every line in our file
        level = [] #We create a another list
        for x in line: 
            if x !='\n':
                level.append(x) #We add every character of each line expect \n
        laby.append(level) #Then we add our first level to the laby list and so on

