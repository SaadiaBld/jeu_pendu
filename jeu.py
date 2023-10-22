print ("BIENVENUE AU HANGMAN GAME!\n\nSOYEZ PRÊTS POUR TROUVER LE MOT MYSTERE...\n\n")



#on définit deux liste de mots dans lesquelles notre programme piochera un mot au hasard, les mots sont en 
#minuscule sans accents
liste_hard= ["incongru", 'pragmatique', "eloquent", "equivoque", "perspicace", "mélancolie", "paradoxe", "ephemere", "ethique", "eclectique", "procrastination", "ambiguite", "réticent", "ingenuité", "exuberance"]
liste_easy= ["montagne", "robinet", "boulangerie", "vacances", "super-heros", "bracelet", "transport", "chaussure", "chapeau", "discussion", "courrier"]


choix_liste = int(input ("Choisissez votre niveau de difficulte:\n\nFacile: tapez 1\nDifficile: tapez 2\n ---> "))

import random

if choix_liste == 1:
   index_liste_pif = random.randint(0,len(liste_easy)-1)  #random.randint genere un nombre au hasard
   solution = liste_easy[index_liste_pif]

elif choix_liste == 2:
   index_liste_pif = random.randint(0,len(liste_hard)-1)
   solution = liste_hard[index_liste_pif]

else:
   choix_liste = input ("Choisissez votre niveau de difficulte:\n\nFacile: tapez 1\nDifficile: tapez 2\n ---> ")

def dessin_pendu(fautes): #chaque etape du dessin correspond à 1 indice dans la liste
    pendu = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    
    return pendu[fautes]


tentatives = 7
fautes = 0
mot = "_" * len(solution)  # Initialise mot avec des underscores

while mot != solution and tentatives > 0:
    ask = input("Proposez une lettre : ")

    if ask in solution:
        # Trouver les indices de la lettre dans la solution
        liste_index = [ind for ind, letter in enumerate(solution) if letter == ask]

        # Mettre à jour le mot avec la lettre correcte aux bons indices
        l = list(mot)
        for i in liste_index:
            l[i] = ask
        mot = "".join(l)

        print(mot)
    else:
        tentatives -= 1
        print(f"Il vous reste {tentatives} essais.")
        print(dessin_pendu(fautes))
        fautes = fautes + 1

        
if mot == solution:
    print("C'est gagné!!")
else:
    print(f"Désolé, le mot était '{solution}'.")


