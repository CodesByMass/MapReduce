#!/usr/bin/env python3
import sys

tab_users = []


indice = 0
totalCalls = 0
sumDuration = 0
duration= 0
indice = 0
average = 0.0


for line in sys.stdin:
    
    line = line.strip()
    record = line.split()

    #Le tout premier élement
    if len(tab_users) == 0:
        tab_users.append(record[0])
        duration = int(record[1])
        sumDuration = sumDuration + duration
        totalCalls += + 1
    #La on vérifie si on est encore entrain de traiter un seul user 
    for user in tab_users:
         if record[0] == user:
            i = tab_users.index(user)
            duration = int(record[1])
            #On ajoute l'appel à la somme
            sumDuration = sumDuration + duration
            totalCalls = totalCalls + 1
    else:
         #La liste étant triée, on passe à un nouvel appelant
        if record[0] != user:
            #Calcul la moyenne de l'utilisateur actuel
            average = float(sumDuration/totalCalls)
            average = float(int(average*10000))/10000
            result = [tab_users[i], round(average,2)]
            print(result)
            #On passe au nouvel utilisateur
            tab_users.append(record[0])
            duration = int(record[1])
            sumDuration = duration
            totalCalls = 1

#Le dernier élement.
average = float(sumDuration/totalCalls)
average = float(int(average*10000))/10000
result = [tab_users[i], round(average,2)]
print (result)    
