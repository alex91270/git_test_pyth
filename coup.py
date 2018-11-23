# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class coup:

    """Classe représentant un labyrinthe."""

    def __init__(self, jeu, direction, nbr_cases):
        self.jeu = jeu
        self.direction = direction
        self.nbr_cases = nbr_cases

    def jouer (self, retour):
        
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
        
