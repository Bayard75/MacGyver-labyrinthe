# -*- coding: utf-8 -*
import os

laby =[] #We create a empty list

with open("constantes\levels.txt") as levels: 
    for line in levels: #For every line in our file
        level = [] #We create a another list
        for x in line: 
            if x !='\n':
                level.append(x) #We add every character of each line expect \n
        laby.append(level) #Then we add our first level to the laby list and so on

mur = "ressources\\mur.png"
background = "ressources\\background.jpg"
aiguille_image = "ressources\\aiguille.png"
ether_image = "ressources\\ether.png"
gardien_image = "ressources\\Gardien.png"
tube_plastique_image = "ressources\\tube_plastique.png"
win_image = "ressources\\win.jpg"
mcGyver_image = "ressources\\MacGyver.png"