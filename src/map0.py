from Grille import *
from personnage import *
from Caisse import *
from Mur import *
from objectif import *

listeCaisses=[]
listeMurs=[]
listeObjectif=[]

#nb=2


def map(nbmap):
    if nbmap==0:
        caisse1=Caisse("caisse.png",7,2)
        caisse2=Caisse("caisse.png",2,7)
        listeCaisses.append(caisse1)
        listeCaisses.append(caisse2)

        mur1=Mur("wall.jpeg",1,6)
        mur2=Mur("wall.jpeg",2,6)
        mur3=Mur("wall.jpeg",4,4)
        mur4=Mur("wall.jpeg",5,4)
        mur5=Mur("wall.jpeg",5,7)
        mur6=Mur("wall.jpeg",5,8)
        mur7=Mur("wall.jpeg",6,4)
        mur8=Mur("wall.jpeg",7,4)
        mur9=Mur("wall.jpeg",8,4)
        mur10=Mur("wall.jpeg",1,2)
        mur11=Mur("wall.jpeg",2,1)
        mur12=Mur("wall.jpeg",1,1)
        mur13=Mur("wall.jpeg",8,5)
        listeMurs.append(mur1)
        listeMurs.append(mur2)
        listeMurs.append(mur3)
        listeMurs.append(mur4)
        listeMurs.append(mur5)
        listeMurs.append(mur6)
        listeMurs.append(mur7)
        listeMurs.append(mur8)
        listeMurs.append(mur9)
        listeMurs.append(mur10)
        listeMurs.append(mur11)
        listeMurs.append(mur12)
        listeMurs.append(mur13)

        objectif1=Objectif("Trou.png",7,8)
        objectif2=Objectif("Trou.png",2,2)
        listeObjectif.append(objectif1)
        listeObjectif.append(objectif2)

        for i in range (0,10):

            mur14=Mur("wall.jpeg",i,0)

            mur15=Mur("wall.jpeg",0,i)

            mur16=Mur("wall.jpeg",9,i)

            mur17=Mur("wall.jpeg",i,9)

            listeMurs.append(mur14)
            listeMurs.append(mur15)
            listeMurs.append(mur16)
            listeMurs.append(mur17)

    if nbmap==2:
        del listeCaisses[:]
        del listeMurs[:]
        del listeObjectif[:]
        caisse1=Caisse("caisse.png",1,2)
        caisse2=Caisse("caisse.png",3,5)
        caisse3=Caisse("caisse.png",5,2)
        listeCaisses.append(caisse1)
        listeCaisses.append(caisse2)
        listeCaisses.append(caisse3)

        mur1=Mur("wall.jpeg",3,1)
        mur2=Mur("wall.jpeg",3,2)
        mur3=Mur("wall.jpeg",2,3)
        mur4=Mur("wall.jpeg",3,3)
        mur5=Mur("wall.jpeg",3,4)
        mur6=Mur("wall.jpeg",4,1)
        mur7=Mur("wall.jpeg",4,2)
        mur8=Mur("wall.jpeg",4,3)
        mur9=Mur("wall.jpeg",3,6)
        #mur10=Mur("wall.jpeg",6,5)
        #mur11=Mur("wall.jpeg",6,4)
        mur12=Mur("wall.jpeg",6,6)
        mur13=Mur("wall.jpeg",5,6)
        mur18=Mur("wall.jpeg",4,6)



        listeMurs.append(mur1)
        listeMurs.append(mur2)
        listeMurs.append(mur3)
        listeMurs.append(mur4)
        listeMurs.append(mur5)
        listeMurs.append(mur6)
        listeMurs.append(mur7)
        listeMurs.append(mur8)
        listeMurs.append(mur9)
        #listeMurs.append(mur10)
        #listeMurs.append(mur11)
        listeMurs.append(mur12)
        listeMurs.append(mur13)
        listeMurs.append(mur18)

        objectif1=Objectif("Trou.png",1,1)
        objectif2=Objectif("Trou.png",1,3)
        objectif3=Objectif("Trou.png",6,5)
        listeObjectif.append(objectif1)
        listeObjectif.append(objectif2)
        listeObjectif.append(objectif3)

        for i in range (0,8):

            mur14=Mur("wall.jpeg",i,0)

            mur15=Mur("wall.jpeg",0,i)

            mur16=Mur("wall.jpeg",7,i)

            mur17=Mur("wall.jpeg",i,7)

            listeMurs.append(mur14)
            listeMurs.append(mur15)
            listeMurs.append(mur16)
            listeMurs.append(mur17)

    if nbmap==1:
        del listeCaisses[:]
        del listeMurs[:]
        del listeObjectif[:]
        caisse1=Caisse("caisse.png",7,2)
        caisse2=Caisse("caisse.png",4,6)
        listeCaisses.append(caisse1)
        listeCaisses.append(caisse2)

        mur1=Mur("wall.jpeg",5,7)
        mur2=Mur("wall.jpeg",4,7)
        mur3=Mur("wall.jpeg",3,7)
        mur4=Mur("wall.jpeg",2,6)
        mur5=Mur("wall.jpeg",3,3)
        mur6=Mur("wall.jpeg",7,7)
        mur7=Mur("wall.jpeg",2,7)
        mur8=Mur("wall.jpeg",5,1)
        #mur9=Mur("wall.jpeg",5,3)
        mur10=Mur("wall.jpeg",5,4)
        mur11=Mur("wall.jpeg",6,4)
        mur12=Mur("wall.jpeg",7,4)
        mur13=Mur("wall.jpeg",8,4)
        mur48=Mur("wall.jpeg",2,3)
        listeMurs.append(mur1)
        listeMurs.append(mur2)
        listeMurs.append(mur3)
        listeMurs.append(mur4)
        listeMurs.append(mur5)
        listeMurs.append(mur6)
        listeMurs.append(mur7)
        listeMurs.append(mur8)
        #listeMurs.append(mur9)
        listeMurs.append(mur10)
        listeMurs.append(mur11)
        listeMurs.append(mur12)
        listeMurs.append(mur13)
        listeMurs.append(mur48)

        objectif1=Objectif("Trou.png",1,4)
        objectif2=Objectif("Trou.png",8,5)
        listeObjectif.append(objectif1)
        listeObjectif.append(objectif2)

        for i in range (0,10):

            mur14=Mur("wall.jpeg",i,0)

            mur15=Mur("wall.jpeg",0,i)

            mur16=Mur("wall.jpeg",9,i)

            mur17=Mur("wall.jpeg",i,9)

            listeMurs.append(mur14)
            listeMurs.append(mur15)
            listeMurs.append(mur16)
            listeMurs.append(mur17)

###############
###############

