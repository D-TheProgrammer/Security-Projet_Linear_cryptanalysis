from random import randint
sbox = [9, 11, 12, 4, 10, 1, 2, 6, 13, 7, 3, 8, 15, 14, 0, 5]
xobs = [14, 5, 6, 10, 3, 15, 7, 9, 11, 0, 4, 1, 2, 8, 13, 12]

def enc (m, key):
    t = sbox[m ^ key[0]]
    c = sbox[t ^ key[1]]
    return c

def dec (c, key):
    t = xobs[c] ^ key[1]
    m = xobs[t] ^ key[0]
    return m


def parite(X,Y): #X (entier) = x4x2x1x0
    res = 0
    mask=1
    for i in range (0,4):
        x = X & mask #on essaie de reccuperer les bit allant de poids faible de X 
        y = Y & mask
        res =res  ^ x ^ y

        X = X>>1 #on decale chaque bit de X sur la droite afinde faire le calcul avec le mask au tour suivant
        Y= Y>>1
    return res #retourne 0 ou 1


def compte_lineaire():
    tab=[[0]*16 for i in range (16)] #rempli une liste AVEC 16 zero et le fait 16 fois
    
    for maski in range (16): #on cree le mask i qui quand sera a 2 , tois les autres mask 0 seront fait
        for mask0 in range (16): #on cree le mask 0 qui tourne plus vite que le maski afin de faire toutes les combinaison
            compteur=0 # Compteur de parité
            for x in range (len(sbox)) : #On parcours la sbox afin davoir les Y 
                y = sbox[x]
                X_masker= x & maski #on masque la partie de gauche
                Y_masker= y & mask0 #on masque la partie de droite
                if (parite(X_masker,Y_masker) == 0): #si la parite donc le nombre de bit a 1 est paire donc ici egal 0 on augmente le compteur
                    compteur +=1
            tab[maski][mask0] = compteur #et on place le compteur

    for ligne in tab: #print du tabelau
        print(ligne)

    return tab
            
tableau_de_paire= compte_lineaire()



def meilleure_paire(tab):
    le_compteur_max = 0
    nombre_bit_1_max=0
    meilleur_maski = 0
    meilleur_mask0 = 0

    #trouver le max par ligne de tableau 
    for maski in range(16): #on cree le mask i qui quand sera a 2 , tois les autres mask 0 seront fait
        for mask0 in range(16): #on cree le mask 0 qui tourne plus vite que le maski afin de faire toutes les combinaison
            if (maski != 0 or mask0 != 0): #Car on veut pas de la toute premiere case du tableau qui aura en resultat 16
               
                compteur_parite = tab[maski][mask0]

                # Si le compteur de parite est plus grand que ceux quon a stocker 
                #on reccupere son maski et mask0
                if ( (compteur_parite >= le_compteur_max) and (bin(mask0).count('1') +  bin(maski).count('1')) > nombre_bit_1_max ):

                    le_compteur_max = compteur_parite
                    nombre_bit_1_max = bin(mask0).count('1') +  bin(maski).count('1')
                    meilleur_maski = maski
                    meilleur_mask0 = mask0

    return meilleur_maski, meilleur_mask0

# Appel de la fonction pour obtenir la meilleure paire de masques
meilleur_maskS = meilleure_paire(tableau_de_paire)
print("\nMeilleure paire de masques (maski, mask0):", meilleur_maskS[0], meilleur_maskS[1])






def generer_liste_paire(nb_paire,key):
    liste_paire=[]
    i=0
    #for i in range (nb_paire):
    while i < nb_paire:
        alea=randint(0,15)
        #print("alea :",alea)

        temp=[alea,enc(alea,key)]
        unique = 1
        for paire in liste_paire:
            if temp == paire:
                unique = 0
                break
        if unique==1:
            liste_paire.append(temp)
            i += 1 

    return liste_paire
    

nb_paire=16
cle= (11,3)
print("Cle utiliser : ",cle)
print("Nombre de paire alea geneer : ",nb_paire)
liste_de_paire_alea= generer_liste_paire(nb_paire,cle)
print(liste_de_paire_alea)



#Fonction pour conserve les potentiel K0
def score_k0 ( liste_m_et_chiffre , maskS):
    #ON rempli de 0 pour pouvoir incrementer un compteur plus tard 
    compteur_score_masque = [0 for i in range (16)]
    liste_masque_garde=[]
    for i in range (16):
        score_masque0 = 0
        for message_ou_chiffre in liste_m_et_chiffre : 
            t = sbox[message_ou_chiffre[0] ^i]  #on XOR par chaque masque 0 

            #Verification de lapproximation lineaire pour valide le second tour
            #on reprend la logique du calcul de parite de lautre focntion
            if (parite ( ( t & maskS[0]) , (message_ou_chiffre[1]  & maskS[1]) ) == 0):
                
                score_masque0 += 1
                
        compteur_score_masque[i] = score_masque0

        #on garde seulement les mask0 qui fonction avec la condition que le k1 peut inverser le resultat
        if  (compteur_score_masque[i] < 4 or compteur_score_masque[i] > 10) :
            liste_masque_garde.append(i)
    
    return liste_masque_garde


liste_masque_reduite=score_k0 ( liste_de_paire_alea , meilleur_maskS)
print("Liste des KO concervé ", liste_masque_reduite)



#Fonction pour retrouver la cle a partir des potentiel K0
def cryptAttaqueLin ( liste_m_et_chiffre , liste_masque_reduite):
    #pour chaque k0 precedemment retunu
    for k0_proto in liste_masque_reduite:
        resultat=0

        #on  boucle car ya 16 couple clair-chiffre
        for i in range (16) :
            
            #on calcule le premier tour et le dernier tour en partant de la fin 
            #donc en sens inversé 
            clair_xore= liste_m_et_chiffre[i][0] ^ k0_proto
            t1 = sbox[clair_xore]
            tour_inverse =xobs[liste_m_et_chiffre[i][1]]
            
            #donc pour la clé 1 il faut XOR les resultat
            k1_proto = t1 ^ tour_inverse

            for clair_chiffre in liste_m_et_chiffre :
                if (dec(clair_chiffre[1], (k0_proto, k1_proto))  !=  clair_chiffre[0]):
                    #print("pas decodé")
                    resultat=1
                    break
        
        if (resultat == 0):
            cle=(k0_proto,k1_proto)
            return cle



print("La clé retrouver apres attaque est : ", cryptAttaqueLin(liste_de_paire_alea , liste_masque_reduite ) )