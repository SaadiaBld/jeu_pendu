"""Bienvenue dans le jeu du pendu"""

print ("BIENVENUE AU HANGMAN GAME!\n\nSOYEZ PRÊTS POUR TROUVER LE MOT MYSTERE...\n\n")

#on définit liste de mots dans lesquelles notre programme piochera un mot au hasard, les mots sont en 
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

