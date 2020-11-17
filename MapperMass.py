#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    record = line.split(",")
    
    # On récupère toutes les lignes où la ville est Paris.
    #Ca veut dire que nous sommes dans le fichier users si l'enregistrement a 5 colonnes. 
    if len(record) == 5 :
        if record[4] == "Paris":
            # Numero de Telephone + Nom du user
            print(record[2], record[1])
        else :
            continue
        #Ici pour le fichier calls.txt, on récupère le numéro appelant et la durée de l'appel.
    else:
        #Numero de l'appelant + la durée de l'appel
        print(record[0], record[2])

