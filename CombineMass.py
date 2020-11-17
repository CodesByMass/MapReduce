#!/usr/bin/env python3

import sys

tabUsersKey = []
tabUsersvalue = []

phone = 0
duration = 0

for line in sys.stdin:
    line = line.strip()
    record = line.split()

    # On regarde si la valeur est un nom ou une durée d'appel
    if record[1].isnumeric() == False:
        tabUsersKey.append(record[0])
        tabUsersvalue.append(record[1])
    else:
        #Pour tous les numéros dans la table utilisateurs
        for phones in tabUsersKey:
            #Si le numéro est dans la ligne actuel
            if phones in record:
                # On recupère le numéro de la table users
            	phone = tabUsersKey.index(phones)
                #On recupère la durée de l'appel
            	duration = int(record[1])
                # On affiche le nom de l'appelant et la durée de l'appel
            	print(tabUsersvalue[phone], duration)
