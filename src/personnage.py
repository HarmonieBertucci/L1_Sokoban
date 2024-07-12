import pygame
from Mur import *
from Grille import *
from map0 import *


class Personnage(pygame.sprite.Sprite) :

    def __init__(self,ide,pseudo,genre,image):
        pygame.sprite.Sprite.__init__(self)
        self.ide=ide
        self.pseudo=pseudo
        self.genre=genre

        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image,(70,70))
        self.rect=self.image.get_rect()
        (posx,posy)=(self.rect.x,self.rect.y)
        self.posx=posx
        self.posy=posy

        self.sens=-1


    def possible(self):
        #définit si la case devant le personnage est libre, si il peut s'y déplacer
        (x,y)=(self.posx,self.posy)
        (dx,dy)=(0,0) #dx et dy sont les coordonnées où sera le personnage le coup suivant si la fonction retourne (0,0) il ne se déplacera pas,
                        #sinon, il se déplacera à cet endroit
        if self.sens == 0: #vers la 'droite'
            (x,y)=(self.posx,self.posy+1)
            (dx,dy)=(0,1)

        elif self.sens == 1: #vers le 'haut'
            (x,y)=(self.posx-1,self.posy)
            (dx,dy)=(-1,0)

        elif self.sens == 2: # vers la 'gauche'
            (x,y)= (self.posx,self.posy-1)
            (dx,dy)=(0,-1)

        elif self.sens == 3: #vers le 'bas'
            (x,y)=(self.posx+1,self.posy)
            (dx,dy)=(1,0)

        boxRect=pygame.Rect(150+x*70, 120+y*70, 70,70)

        for objet in allSprites :
            if objet.rect.colliderect(boxRect) and type(objet).__name__ !="Personnage" :

                print("collision entre Personnage et : ",type(objet).__name__)

                if (type(objet).__name__=="Mur"):
                    return(0,0)

                elif(type(objet).__name__=="Caisse"):
                    objet.sens=self.sens # sens de deplacement de caisse = sens de depl. de perso

                    (dxc,dyc)=objet.possible()

                    if (dxc,dyc) !=(0,0):
                        objet.update()

                    else :
                        return(0,0) # Si collision entre deux caisses, pas de mvt de perso.

                    return(dx,dy)

        return(dx,dy)

    def update(self):

        (dx,dy)=self.possible()
        #si déplacement possible, les positions du personnage changent :
        self.posx +=dx
        self.posy +=dy

        self.rect.x=150+self.posx*70
        self.rect.y=120+self.posy*70

        self.sens=-1


    def get_ide(self): #permet de récupérer l'identifiant
        return(self.ide)

    def get_pseudo(self): #permet de récupérer le pseudo
        return(self.pseudo)

    def set_pseudo(self,newpseudo): #permet de changer le pseudo
        self.pseudo=newpseudo

    def set_genre(self): #permet de changer le genre
        if self.genre=="M":
            self.genre="F"
            self.image=pygame.image.load("Fille.png")
            self.image=pygame.transform.scale(self.image,(70,70))
        else:
            self.genre="M"
            self.image=pygame.image.load("perso.png")
            self.image=pygame.transform.scale(self.image,(70,70))

    def get_genre(self): #permet de récupérer le genre
        return(self.genre)

    def get_center(self): #permet de récupérer le centre du rect du perso
        return(self.rect.center)


    def set_center(self,x,y):#permet de changer le centre du rect du perso
        self.rect.center=(x,y)
