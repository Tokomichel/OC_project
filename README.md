# SQL generator project

Utilisation des fichier pythons pour generer automatiquement des scripts sql

## Utilisation

- Il faudra d'abors renseigner le nom de la table a remplir
- En suite renseigner le nom des colonnes a renseigner 
- Continuer en enregistrent les valeurs

'''
# on implement le code sql

# on ajoute les proprietes

''' 
for i in range(len(list_propriete)):
     if i == len(list_propriete) - 1:
          first_sql_syntax += list_propriete[i] + ")"
     else:     
         first_sql_syntax += list_propriete[i] + ","


first_sql_syntax += "\nVALUE\n"
'''
