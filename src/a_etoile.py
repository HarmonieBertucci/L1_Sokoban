from map0 import nb
from map0 import allSprites

if nb==1:
    ordre_c_o={(1,2):(1,1),(3,5):(1,3),(5,2):(5,4)}
elif nb==2:
    ordre_c_o={(4,6):(8,5),(7,2):(1,4)}

def qualite(point,objectif):
    #cette fonction va définir la qualité d'un point selon sa distance de l'objectif


for objet in allSprites :
    #parcours de allSprites pour avoir la caisse et son objectif pour pouvoir utiliser A*
    if type(objet).__name__=="Caisse" :
        (xcaisse,ycaisse)=(objet.posx,objet.posy)
        obj=ordre_c_o[(xcaisse,ycaisse)]
        print("l'objectif de la caisse",(xcaisse,ycaisse), "est à la position :",obj)

        listeouverte=[]
        #la liste ouverte contiendra les points étudiés dans la recherche du chemin le plus court
        listefermee=[]
        #la liste fermée contiendra les points pouvant faire partit de la solution




