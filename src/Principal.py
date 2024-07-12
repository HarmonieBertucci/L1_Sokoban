import sys
sys.path.append('/usr/local/lib/python3.7/site-packages/')
from Grille import *
from personnage import *
from random import *
import pygame
from pygame.locals import *
from math import *
from objectif import *
from map0 import *


pygame.init()
pygame.display.set_caption("Sokoban") #nom du jeu

mainClock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 1000),0,32) #taille de la fenêtre du jeu

font = pygame.font.SysFont(None, 20)
ka=1
nbmap=0 #numéro de la map à lancer
map(nbmap)

for caisse in listeCaisses:
    allSprites.add(caisse)

for hole in listeObjectif:
    allSprites.add(hole)

for mur in listeMurs:
    allSprites.add(mur)

Perso=Personnage(1,"Pseudo", "M","perso.png")



def draw_text(text, font, color, surface, x, y):
    #cette fonction sert à écrire du texte dans le menu
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    print('aaa')
    while True:

        screen.fill((66,66,66)) #couleur
        draw_text('Menu', font, (102, 224, 255), screen, 480, 20)
        draw_text('Mode Histoire', font, (102, 224, 255), screen, 390, 117)
        draw_text('Genre :', font, (102, 224, 255), screen, 400, 210)

        mx, my = pygame.mouse.get_pos()
        #endroit où se trouve le curseur de la souris

        button_2 = pygame.Rect(480, 200, 50, 50)


        if Perso.genre=="M":
            pygame.draw.rect(screen, (20, 75, 178), button_2)
        else :
            pygame.draw.rect(screen, (238, 54, 185), button_2)

        if button_2.collidepoint((mx, my)):
            if click:
                Personnage.set_genre(Perso)
                #if Perso.genre=="M":
                    #Perso.genre="F"
                #else:
                    #Perso.genre="M"
            #devrait changer le genre



        im1=pygame.image.load("perso.png")
        im1=pygame.transform.scale(im1,(200,200))
        im2=pygame.image.load("caisse.png")
        im2=pygame.transform.scale(im2,(200,200))
        im3=pygame.image.load("fille.png")
        im3=pygame.transform.scale(im3,(200,200))
        screen.blit(im1,(200,400))
        screen.blit(im2,(400,400))
        screen.blit(im3,(600,400))
        #trois images de la partie basse du menu


        button_1 = pygame.Rect(480, 100, 50, 50)
        nbmap=0



        if button_1.collidepoint((mx, my)): #si il y a collistion entre le curseur de la souris et le bouton
            if click: # click donné plus bas
                game(nbmap)
                #lance le jeu

        pygame.draw.rect(screen, (255, 0, 0), button_1)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)



def game(nbmap):
    running = True
    while running:
        screen.fill((0,0,0))
        #allSprites.empty() : efface tout ce qu'il y a dans allSprites
        print(nbmap,"c nbmap")
        map(nbmap) #est sensé lancer la map n°'nbmap'
        test=Main(10,listeMurs,listeCaisses)

        #Perso=Personnage(1,"Pseudo", genre,"perso.png")
        print(Perso.get_pseudo()) #récupère le pseudo
        allSprites.add(Perso)

        Perso.set_pseudo("Pseudo2") #change le pseudo
        print(Perso.get_pseudo())

        test.placer(Perso,6,1) #place le "P" dans la console
        Perso.posx=6
        Perso.posy=1


        for Caisse in listeCaisses: #parcours de listeCaisses
            test.grille[Caisse.posx][Caisse.posy]="C" #affiche les caisses dans la grille sur la console

        for Mur in listeMurs: #parcours de listeMurs
            test.grille[Mur.posx][Mur.posy]="#" #affiche les murs dans la grille sur la console

        for hole in listeObjectif: #parcours de listeObjectif
            test.grille[hole.posx][hole.posy]="0" #affiche les objectifs dans la grille sur la console



        pygame.display.flip()

        for objet in allSprites :
            if  (type(objet).__name__!="Mur"):
                print(type(objet).__name__,(objet.posx,objet.posy)," - ", (150+objet.posx*70, 120+objet.posy*70), " : ",objet.rect  )
                # Affiche les obstacles autres que les murs (leurs type, position en console et sur l'interface) en console


        MVT=False #update la console (ligne 158)
        continuer = True
        while continuer:
            test.ecran.fill((80,149,179))


            if MVT==True :
                (x,y)=(Perso.posx,Perso.posy)
                test.affiche()

                MVT=False

            clock = pygame.time.Clock()

            for event in pygame.event.get(): #réagit s'il y a un évènement au clavier ou à la souris
                if event.type == pygame.QUIT:
                        continuer = False
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:

                    test.grille[Perso.posx][Perso.posy]=0 #remplace le personnage par un endroit vide

                    if event.key == pygame.K_RIGHT: #si la flèche 'droite' est enfoncée
                        MVT=True
                        Perso.sens=0

                    elif event.key == pygame.K_LEFT: #si la flèche 'gauche' est enfoncée
                        MVT=True
                        Perso.sens=2

                    elif event.key == pygame.K_UP: #si la flèche 'haut' est enfoncée
                        MVT=True
                        Perso.sens=1

                    elif event.key == pygame.K_DOWN: #si la flèche 'bas' est enfoncée
                        MVT=True
                        Perso.sens=3

                    allSprites.update() #lance le update de tous les sprites

                    test.grille[Perso.posx][Perso.posy]="P" #met le personnage à sa nouvelle position

                    c=1
                    nbfin=0
                    nombretothole=0
                    if nbmap==1 :
                        le=2
                    elif nbmap==2:
                        le=3
                    elif nbmap==0:
                        le=2
                    for Caisse in listeCaisses:
                        if (c<=le):
                            print(type(Caisse).__name__,(Caisse.posx,Caisse.posy))
                            print("caisse à",Caisse.posx,Caisse.posy)
                            test.grille[Caisse.posx][Caisse.posy]="C"
                            c+=1

                    for hole in listeObjectif:
                        test.grille[hole.posx][hole.posy]="0"
                        boxRect=pygame.Rect(150+hole.posx*70, 120+hole.posy*70, 70,70)
                        for objet in allSprites :
                            if objet.rect.colliderect(boxRect) and type(objet).__name__ =="Caisse" :
                                test.grille[hole.posx][hole.posy]="X"
                        nombretothole+=1

                    for hole in listeObjectif:
                        if test.grille[hole.posx][hole.posy]=="X":
                            nbfin+=1
                        if nbfin==nombretothole:
                            suite(nbmap)
                    nbfin=0

                    #Personnage.set_genre(Perso) #change le genre/l'image du personnage


            for objet in allSprites:
                test.ecran.blit(objet.image,(120+(objet.posy*70),150+(objet.posx*70)))
                #affiche sur pygame les sprites

            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
        test.affiche() #affiche le jeu en console à chaque mouvement

def suite(nbmap):
    allSprites.empty()
    print("nbmap avant",nbmap)
    nbmap+=1
    if nbmap==3:
        fin()
    print("nbmap après", nbmap)
    map(nbmap)
    for caisse in listeCaisses:
        allSprites.add(caisse)

    for hole in listeObjectif:
        allSprites.add(hole)

    for mur in listeMurs:
        allSprites.add(mur)

    #test=Main(10,Mur,listeCaisses)
    for objet in allSprites :
        if  (type(objet).__name__!="Mur"):
            print(type(objet).__name__,(objet.posx,objet.posy)," - ", (150+objet.posx*70, 120+objet.posy*70), " : ",objet.rect  )
    game(nbmap)

def fin():
    pass
    while True:

        screen.fill((35,240,54)) #couleur
        mx, my = pygame.mouse.get_pos()


##
        im0=pygame.image.load("win.png")
        im0=pygame.transform.scale(im0,(200,200))
        screen.blit(im0,(400,150))
##
        im1=pygame.image.load("perso.png")
        im1=pygame.transform.scale(im1,(200,200))
        im2=pygame.image.load("caisse.png")
        im2=pygame.transform.scale(im2,(200,200))
        im3=pygame.image.load("fille.png")
        im3=pygame.transform.scale(im3,(200,200))
        screen.blit(im1,(200,400))
        screen.blit(im2,(400,400))
        screen.blit(im3,(600,400))
        #trois images de la partie basse
##
##
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu() #lance le menu au démarage du jeu


