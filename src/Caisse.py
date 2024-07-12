import pygame
from Grille import *
from personnage import *

allSprites=pygame.sprite.Group()

class Caisse(pygame.sprite.Sprite):
    def __init__(self,image,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image,(70,70))
        self.posx=posx
        self.posy=posy
        self.rect=self.image.get_rect()
        self.rect.x=self.posx
        self.rect.y=self.posy
        self.rect= pygame.Rect(150+posx*70, 120+posy*70, 70,70)

        self.sens=-1


    def possible(self):
        (x,y)=(self.posx,self.posy)
        (dx,dy)=(0,0)
        if self.sens == 0:
            (x,y)=(self.posx,self.posy+1)
            (dx,dy)=(0,1)

        elif self.sens == 1:
            (x,y)=(self.posx-1,self.posy)
            (dx,dy)=(-1,0)

        elif self.sens == 2:
            (x,y)= (self.posx,self.posy-1)
            (dx,dy)=(0,-1)

        elif self.sens == 3:
            (x,y)=(self.posx+1,self.posy)
            (dx,dy)=(1,0)


        boxRect=pygame.Rect(150+(x)*70, 120+(y)*70, 70,70)

        for objet in allSprites :
            if(type(objet).__name__=="Caisse"):
                if objet !=self and objet.rect.colliderect(boxRect) :
                    print("Collision entre caisses : ",objet.rect,boxRect  )
                    return(0,0) # on decide de pas bouger sinon ...

            elif(type(objet).__name__=="Mur"):
                if objet.rect.colliderect(boxRect) :
                    print("Collision entre caisse et Mur : ",objet.rect,boxRect  )
                    return(0,0)


            elif(type(objet).__name__=="Objectif"):
                if objet.rect.colliderect(boxRect) :
                    print("Collision entre caisse et holle : ",objet.rect,boxRect  )





        return(dx,dy)

    def update(self):

        (dx,dy)=self.possible()
        self.posx +=dx
        self.posy +=dy
        self.rect.x=150+self.posx*70
        self.rect.y=120+self.posy*70

        self.sens=-1


