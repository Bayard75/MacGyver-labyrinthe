# -*- coding:utf-8 -*
import pygame
from pygame.locals import*
import os 
from random import randrange

os.chdir(r"C:\Users\mbaya\OneDrive\Documents\python\Projet_3")

class Maze():
    """Class that will define a maze object it will take in the background image and a list"""

    def __init__(self,background,wall,liste): #2 attributs background and liste, which contains the maze squeleton
        self.window = pygame.display.set_mode((570,545)) #600 by 600 window
        self.background = pygame.image.load(background).convert()
        self.window.blit(self.background,(0,0))
        self.liste = liste
        self.wall = wall

    def generate_maze(self):
        """Methode that generate and displays a maze based on the list squeleton"""
        x = 0 #We start at the top left corner (0,0)
        y = 0
        
        self.tile = pygame.image.load(self.wall).convert_alpha() #Our walls

        for i in range(0,225): #The game is always 15 by 15 sprites so we gonna iterate our loop 15*15 times
            if self.liste[y][x] == '1': #If the value is 1 we put up a wall
                self.window.blit(self.tile,(x*36,y*36))
            x +=1 #move left without moving down

            if x == 15: #when we it the limits of the maze
                x =0 #go back to the first sprite left
                y +=1 #move down
        pygame.display.flip() #actualisation of the display.

    def refresh_maze(self,object_to_display):
        """Method that refreshes the window to display all relevent images"""
        i = 0
        self.window.blit(self.background,(0,0))
        self.generate_maze()
        while i < len(object_to_display):
            self.window.blit(object_to_display[i].image,(object_to_display[i].position_x*36,object_to_display[i].position_y*36))
            i+=1
        pygame.display.flip()

    def win (self,win):
        win = pygame.image.load("win.jpg").convert() 
        self.window.blit(win,(0,0))
        pygame.display.flip()

class Characters():
    """Class that will create characters object it will take in 2 attributs the image
       the y position and the x position of the character 
    """
    def __init__(self,image,lettre,liste):
        self.image = pygame.image.load(image).convert_alpha()
        self.inventory = []
        self.lettre = lettre
        for i, e in enumerate(liste):
            try: #The following line of code doesn't work if not un a try/expect catch
                self.position_y, self.position_x = i, e.index(lettre)  
            except ValueError:
                pass

    def move(self,direction,liste): 
        """ This method allows us to move the character it takes in 2 parametres
        The first is the direction in which the character is to be moved
        The second is the maze squeleton neccessery to validate the movement.
        """

        if direction == "RIGHT": #if the character wants to move right
            if self.position_x !=14 and liste[self.position_y][self.position_x+1] !="1":
               
                """ Here if there is still place to move right AND if the next sprite 
                right is not a wall than we can move. To always keep in mind our liste 
                is as such laby[y][x] and not laby[x][y]
                """
                self.position_x = self.position_x+ 1 #We move one sprite right
        if direction =="LEFT": #Same principal than before
            if self.position_x != 0 and liste[self.position_y][self.position_x -1] !="1":
                self.position_x -=1
        if direction =="UP":
            if self.position_y != 0 and liste[self.position_y-1][self.position_x] !="1":
                self.position_y -=1
        if direction =="DOWN":
            if self.position_y !=14 and liste[self.position_y+1][self.position_x]  !="1":
                self.position_y +=1
        
    def verify_inventory(self,character,item1,item2,item3):
            """ Method that checks if mcGyver has all 3 elements"""
            if item1 and item2 and item3 in character.inventory:
                return True 
            else:
                return False 

    def pick_up(self,artefact):
        """ Method that will pick up an objet put it in the character inventory
        and move the object image to the top right corner of ths screen to keep track of the object picked up"""
        self.inventory.append(artefact)
        
        if artefact.name =="ether": 
            artefact.position_x = 15
            artefact.position_y = 0
        if artefact.name =="tube plastique":
            artefact.position_x =15
            artefact.position_y =1
        if artefact.name =="aiguille":
            artefact.position_x =15
            artefact.position_y =2


class Artefact():
    """Class that create an artefact objet with 4 attributs its name, image, position x and y 
    we need a list which will eneable us to place the artefact in any empty spot of the said list"""

    def __init__(self,name,image,liste):
        self.name = name
        self.image = pygame.image.load(image).convert_alpha()
        self.liste = liste
        not_found = True    
        while not_found == True:
            x = randrange(0,14)
            y = randrange(0,14)
            if self.liste[y][x] =="0": # If our randomly generated position gives us a empty spot :
                self.position_y = y # We give our artefact said positions !
                self.position_x = x
                not_found = False
            else:
                continue
            #If not we try again and again...
            