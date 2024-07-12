import pygame

from random import *

DEPLACEMENT=pygame.USEREVENT

class Main:

    def __init__(self,n,Mur,LCaisse):
        self.ecran = pygame.display.set_mode((1000,1000))
        self.ecran.fill((80,149,179))
        self.taille=n

        self.grille=self.creegrille()

        self.Mur=Mur

        self.perso=pygame.image.load("perso.png")
        self.perso=pygame.transform.scale(self.perso,(70,70))
        self.Caisse=LCaisse




    def creegrille(self):

        res=[0]*self.taille

        for i in range(self.taille):

            res[i]= [0]*self.taille

        return res



    def affiche(self):


        for i in range (self.taille):

            for j in range (self.taille):

                if self.grille[i][j]==0:

                    print(".",end=" ")

                else :

                    print(self.grille[i][j],end=" ")

            print()

    def permis(self,x,y):

        if self.grille[x][y]==0:

            return True

        else:
            if self.grille[x][y]=="C" :
                return True
            else :

                return False




    def placer(self,perso,x,y):

        if self.permis (x,y):

            self.grille[x][y]="P" #perso.genre
            perso.rect= pygame.Rect(150+x*70, 120+(y*70), 70,70)

        else:
            print("Pas permis")




    def placement_mur(self):

        for i in range (self.taille):

            self.grille[i][0]="#"
            self.ecran.blit(self.mur,(150,120+(i*70)))

            self.grille[0][i]="#"
            self.ecran.blit(self.mur,(150+(i*70),120))

            self.grille[self.taille-1][i]="#"
            self.ecran.blit(self.mur,(780,120+(i*70)))

            self.grille[i][self.taille-1]="#"
            self.ecran.blit(self.mur,(150+(i*70),750))

        for m in (self.Mur):

            x= m[0]

            y= m[1]

            self.grille[x][y]="#"
            self.ecran.blit(self.mur,(150+(y*70),120+(x*70)))

        pygame.display.flip()

    def placement_Caisse(self):

        for i in (self.Caisse):

            x= i[0]
            y= i[1]

            self.grille[x][y]="C"
            self.ecran.blit(self.caisse,(150+(y*70),120+(x*70)))







    def mouvement(self,Perso,direction):
        for k in range(len(self.grille)):
            for t in range(len(self.grille)):
                if self.grille[k][t]=="P":
                    x=k
                    y=t
                    print("x=",x,"et y=",y)
##
##
        if direction=="d":
            if self.permis(x,y+1):
                print("x=",x,"et y=",y+1)
                Perso.rect=Perso.rect.move(70,0)
                self.ecran.blit(Perso.image,(Perso.rect))
                self.placer(Perso,x,y+1)
                self.grille[x][y]=0
##
##
        elif direction=="q":
            if self.permis(x,y-1):
                print("x=",x,"et y=",y-1)
                Perso.rect=Perso.rect.move(-70,0)
                self.placer(Perso,x,y-1)
                self.grille[x][y]=0
##
        elif direction=="z":
            if self.permis(x-1,y):
                print("x=",x-1,"et y=",y)
                Perso.rect=Perso.rect.move(0,70)
                self.placer(Perso,x-1,y)
                self.grille[x][y]=0
##
        elif direction=="s":
            if self.permis(x+1,y):
                print("x=",x+1,"et y=",y)
                Perso.rect=Perso.rect.move(0,-70)
                self.placer(Perso,x+1,y)
                self.grille[x][y]=0
##
        self.affiche()





    def deplace_perso(self,Perso,x,y,position):
##
        for event in pygame.event.get():
            if position=="d":
                if self.permis(x,y+1):
                    if self.grille[x][y+1]=="C":
                        if self.permis(x,y+2) and self.grille[x][y+2]!="C":
                            self.grille[x][y+2]="C"
                            self.placer(Perso,x,y+1)
                            self.grille[x][y]=0
                        elif self.grille[x][y+2]==".": ########points
                            self.grille[x][y+2]=0
                            self.placer(Perso,x,y+1)
                            self.grille[x][y]=0
                        else:
                            pass
                    else:
                        self.placer(Perso,x,y+1)
                        self.grille[x][y]=0


            if position =="q":
                if self.permis(x,y-1):
                    if self.grille[x][y-1]=="C":
                        if self.permis(x,y-2) and self.grille[x][y-2]!="C":
                            self.grille[x][y-2]="C"
                            self.placer(Perso,x,y-1)
                            self.grille[x][y]=0
                        elif self.grille[x][y-2]==".": ########points
                            self.grille[x][y-2]=0
                            self.placer(Perso,x,y-1)
                            self.grille[x][y]=0
                        else:
                            pass
                    else:
                        self.placer(Perso,x,y-1)
                        self.grille[x][y]=0
##
            if position =="z":
                if self.permis(x-1,y):
                    if self.grille[x-1][y]=="C":
                        if self.permis(x-2,y) and self.grille[x-2][y]!="C":
                            self.grille[x-2][y]="C"
                            self.placer(Perso,x-1,y)
                            self.grille[x][y]=0
                        elif self.grille[x-2][y]==".": ########points
                            self.grille[x-2][y]=0
                            self.placer(Perso,x-1,y)
                            self.grille[x][y]=0
                        else:
                            pass
                    else:
                        self.placer(Perso,x-1,y)
                        self.grille[x][y]=0

            if position =="s":
                if self.permis(x+1,y):
                    if self.grille[x+1][y]=="C":
                        if self.permis(x+2,y) and self.grille[x+2][y]!="C":
                            self.grille[x+2][y]="C"
                            self.placer(Perso,x+1,y)
                            self.grille[x][y]=0
                        elif self.grille[x+2][y]==".": ########points
                            self.grille[x+2][y]=0
                            self.placer(Perso,x+1,y)
                            self.grille[x][y]=0
                        else:
                            pass
                    else:
                        self.placer(Perso,x+1,y)
                        self.grille[x][y]=0

