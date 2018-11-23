# -*-coding:Latin-1 -*

""" Fichier comportant les fonctions:
- creer labyrinthe: Prend le chemin du fichier d'une carte et renvoit une liste des lignes.
- quitter: Quitte le jeu. Si partie finie, supprime la sauvegarde eventuelle,
si partie en cours, l'enregistre.
- jouer: Prend le jeu actuel, la direction du mouvement, le nombre de cases,
et renvoit le nouveau jeu après mouvement."""

import os
import sys
import pickle


def bonjour():
        print("bonjour")

def auRevoir():
        print("au revoir")
        
def creer_labyrinthe(chemin):

        with open(chemin, "r") as fichier:
            contenu = fichier.read()
        jeu=[]
        jeu = contenu.split("\n")
        return jeu

def quitter(jeu):
        if os.path.exists('cartes\sauvegarde') == True:
                os.remove('cartes\sauvegarde')# s'il y a un fichier de sauvegarde, on le supprime
                
        if jeu[0]!= "fini":                        
                with open('cartes\sauvegarde', 'xb') as fichier:# si la partie n'est pas finie, on l'enregistre dans un fichier
                        mon_pickler = pickle.Pickler(fichier)
                        mon_pickler.dump(jeu)
                print ("**********************************")
                print ("**      Partie sauvegardée      **")
                print ("**********************************")
                sys.exit(0)
        else:
                print ("**********************************")
                print ("**      Youpi c'est gagné!      **")
                print ("**********************************")
                sys.exit(0)
                


def jouer(jeu, direction, nbr_cases):

        for n, ligne in enumerate(jeu):    
            index = jeu[n].find('X')
            if index != -1:
                ligneX = n
                indexX = index

        etap = 0
        current_line = 0
        current_index = 0
        ligne_modif = ""

        if direction == "n":    
            while etap < nbr_cases:

                if ((jeu[ligneX - 1])[indexX]) == "U":                        
                        jeu[0] = "fini"
                        etap = nbr_cases
            
                if ((jeu[ligneX - 1])[indexX]) == " " or ((jeu[ligneX - 1])[indexX]) == ".":           
                    ligne_modif = ((jeu[ligneX - 1])[0:indexX]) + "X" + ((jeu[ligneX - 1])[indexX+1:len(jeu[ligneX - 1])])            
                    jeu[ligneX - 1] = ligne_modif
                    ligne_modif = ((jeu[ligneX])[0:indexX]) + " " + ((jeu[ligneX])[indexX+1:len(jeu[ligneX])])
                    jeu[ligneX] = ligne_modif            
                    etap += 1
                    ligneX = ligneX - 1
                    
                else:            
                    etap = nbr_cases
            
        if direction == "s":    
            while etap < nbr_cases:
        
                if ((jeu[ligneX + 1])[indexX]) == "U":
                    jeu[0] = "fini"
                    etap = nbr_cases
            
                if ((jeu[ligneX + 1])[indexX]) == " " or ((jeu[ligneX + 1])[indexX]) == ".":           
                    ligne_modif = ((jeu[ligneX + 1])[0:indexX]) + "X" + ((jeu[ligneX + 1])[indexX+1:len(jeu[ligneX + 1])])           
                    jeu[ligneX + 1] = ligne_modif
                    ligne_modif = ((jeu[ligneX])[0:indexX]) + " " + ((jeu[ligneX])[indexX+1:len(jeu[ligneX])])
                    jeu[ligneX] = ligne_modif            
                    etap += 1
                    ligneX = ligneX + 1         
        
                else:            
                    etap = nbr_cases

        if direction == "e":
            while etap < nbr_cases:        

                if ((jeu[ligneX])[indexX+1]) == "U":
                    jeu[0] = "fini"
                    etap = nbr_cases           
            
                if ((jeu[ligneX])[indexX+1]) == " " or ((jeu[ligneX])[indexX+1]) == ".":                       
                    ligne_modif = ((jeu[ligneX])[0:indexX]) + " X" + ((jeu[ligneX])[indexX+2:len(jeu[ligneX])])            
                    jeu[ligneX] = ligne_modif            
                    etap += 1
                    indexX += 1            
        
                else:           
                    etap = nbr_cases
           

        if direction == "o":
            while etap < nbr_cases:
       
                if ((jeu[ligneX])[indexX-1]) == "U":
                    jeu[0] = "fini"
                    etap = nbr_cases            
            
                if ((jeu[ligneX])[indexX-1]) == " " or ((jeu[ligneX])[indexX-1]) == ".":                                  
                    ligne_modif = ((jeu[ligneX])[0:indexX-1]) + "X " + ((jeu[ligneX])[indexX+1:len(jeu[ligneX])])            
                    jeu[ligneX] = ligne_modif            
                    etap += 1
                    indexX -= 1           
        
                else:            
                    etap = nbr_cases

    

        return jeu

        
    
