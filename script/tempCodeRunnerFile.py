# -*- coding: utf-8 -*
import pygame
from pygame.locals import*
from Classes import*
from constantes_and_fonctions import*

pygame.init() #Pygame is initialized

labyrinth = Maze(background,mur,laby) # We create a instance labyrinth with 2 attributs
labyrinth.generate_maze() # We generate the maze and display it

object_to_display =[]

mcGyver = Characters(mcGyver_image,"m",laby) # We create mcGyver 
warden = Characters(gardien_image, "g",laby) #creation of the warden

ether = Artefact("ether",ether_image,laby)
aiguille = Artefact("aiguille",aiguille_image,laby)
tube_plastique = Artefact("tube plastique",tube_plastique_image,laby)

#Add all our objects to display list.
object_to_display.append(ether)
object_to_display.append(aiguille)
object_to_display.append(tube_plastique)
object_to_display.append(mcGyver)
object_to_display.append(warden)

labyrinth.refresh_maze(object_to_display)

win_or_lose_loop = 1
game_loop = 1

while game_loop == 1: #in this loop conteins the game movements and pick-up interacions
        for event in pygame.event.get(): 
            if event.type == QUIT:
                win_or_lose_loop = 0
                game_loop = 0
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    mcGyver.move("RIGHT", laby)
                if event.key == K_UP:
                    mcGyver.move("UP", laby)
                if event.key == K_DOWN:
                    mcGyver.move("DOWN", laby)
                if event.key == K_LEFT:
                    mcGyver.move("LEFT", laby)
                            
                            # Checking if our new positions are occupied by other objects
                            
                if (mcGyver.position_x, mcGyver.position_y) == (ether.position_x, ether.position_y):
                        mcGyver.pick_up(ether)
                           
                if (mcGyver.position_x, mcGyver.position_y) == (aiguille.position_x, aiguille.position_y):
                        mcGyver.pick_up(aiguille)

                if (mcGyver.position_x, mcGyver.position_y) == (tube_plastique.position_x, tube_plastique.position_y):
                        mcGyver.pick_up(tube_plastique)

                labyrinth.refresh_maze(object_to_display)

                if (mcGyver.position_x,mcGyver.position_y) == (warden.position_x,warden.position_y):
                        game_loop = 0 #We stop the game if mcGyver and the warden have the same position and go second loop to the if we won
    
while win_or_lose_loop == 1:
    for event in pygame.event.get(): 
        if event.type == QUIT:
                win_or_lose_loop = 0
                
        if warden.verify_inventory(mcGyver,ether,tube_plastique,aiguille) == True:
            labyrinth.win(win_image)
        elif warden.verify_inventory(mcGyver,ether,tube_plastique,aiguille) == False:
            win_or_lose_loop = 0