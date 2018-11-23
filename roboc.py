# -*-coding:Latin-1 -*

"""Code principal du jeu"""

import os
import sys
import pickle

from fonctions import *

sauv = False

# On charge les cartes existantes
cartes = []
NbrOptions = 0
for nom_fichier in os.listdir("cartes"):    
    if nom_fichier.endswith(".txt"):        
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].lower()
        cartes.append(nom_carte)
        NbrOptions+=1
        

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print (i+1, " - ", cartes[i])

if os.path.exists('cartes\sauvegarde') == True:
    sauv = True
    print ("Pour reprendre la partie sauvegardée, entrez R")
else:
    print ("pas de sauvegarde")
        
trap = 0
while trap == 0:
    try:
        choix = input("Faites votre choix:")
        
        if sauv == True and (choix == "r" or choix == "R"):            
            trap = 1
            with open('cartes\sauvegarde', 'rb') as fichier:
                mon_depickler = pickle.Unpickler(fichier)
                jeu = mon_depickler.load()
                
        if choix == "q" or choix == "Q":
            print("Au revoir")
            trap = 1
            sys.exit(0)
            
        if int(choix) >0 and int(choix) <= NbrOptions:            
            chemin = os.path.join("cartes", cartes[int(choix)-1]+".txt")
            jeu = creer_labyrinthe(chemin)
            trap = 1
            
        else:
            print ("Entrez Q pour quitter, ou un chiffre entre 1 et ", NbrOptions)
            if sauv == True:
                print ("Ou encore R pour reprendre la partie sauvegardée")
                  
    except ValueError:
        print ("Entrez Q pour quitter, ou un chiffre entre 1 et ", NbrOptions)
        if sauv == True:
            print ("Ou encore R pour reprendre la partie sauvegardée")
        
print('\n' * 50)

partie_en_cours = True

for n, ligne in enumerate(jeu):
        print(jeu[n])

while partie_en_cours == True:

    trap = 0
    while trap == 0:
        try:
            choix = input("Mouvement:")
        
            if choix == "q" or choix == "Q":
                trap = 1
                quitter(jeu)
                sys.exit(0) 
            if choix[0].lower() in ["n", "e", "s", "o"]:
                direction = choix[0].lower()
                trap = 1
                nbr_cases = 1
            if len(choix)>1:
                if choix[1].isdecimal() == True:
                    nbr_cases = int(choix[1])
                    if nbr_cases < 1:
                        nbr_cases = 1
                    if nbr_cases > 3:
                        nbr_cases = 3
        except ValueError:
            print ("Entrez la direction (N, S, E, O), suivi ou non d'un nombre de cases (Maximum 3 seront pris en compte)")


    jeu = jouer(jeu, direction, nbr_cases)

    if jeu[0] == "fini":
        partie_en_cours = False        
        quitter(jeu)
    
    print('\n' * 50)
    
    for n, ligne in enumerate(jeu):
        print(jeu[n])
    
        index = jeu[n].find('X')
        if index != -1:
            ligneX = n
            indexX = index    


            
   


