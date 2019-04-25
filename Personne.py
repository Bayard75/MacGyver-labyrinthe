import pygame
from pygame.locals import *
from os import chdir
chdir(r"C:\Users\mbaya\OneDrive\Documents\python\Projet 3")

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("mur.png").convert_alpha()
position_perso = perso.get_rect()
position_perso.center = 25,325
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:	#Si "flèche bas"
				#On descend le perso
				position_perso = position_perso.move(0,3)
	
	#Re-collage
	fenetre.blit(fond, (0,0))	
	fenetre.blit(perso, position_perso)
	#Rafraichissement
	pygame.display.flip()
