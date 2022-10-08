import python

"""
ce code python a pour but de 
generer un code sql automatiquement et
faciliter l'insertion des 
donnees dans les tables
"""

print("entrer la table dans laquelle vous voulez ajouter des donnees")
nomTable = input('nom table:--') #nom table
list_propriete = list()

#on rempli la liste des proprietes
while True:
  print("\n entrez les propriete de la table a renseigner")   
  propriete = input('<--')
  if propriete == '1':
         break
  else:       
     list_propriete.append(propriete)

first_sql_syntax = f"insert into {nomTable}("

#on implement le code sql

#on ajoute les proprietes
for i in range(len(list_propriete)):
     if i == len(list_propriete) - 1:
          first_sql_syntax += list_propriete[i] + ")"
     else:     
         first_sql_syntax += list_propriete[i] + ","


first_sql_syntax += "\nVALUE\n"

print("combien de valeur souhaiter vous enregistrer dans votre table?")
nombre_enregistrement = int(input("<--"))


#on rempli les valeurs
for i in range(nombre_enregistrement):
   
   enregistrer = "("
   for i  in range(len(list_propriete)):
      val = input(f"val{i}: ")

      if python.IsIn(val) is True:
          val = "\"" + val + "\""   

      if i == len(list_propriete) - 1:
            enregistrer += val + ")\n" 
      else:      
            enregistrer += val + ","   


   first_sql_syntax += enregistrer
   """
   delete from table where some_colum = some_value
   """

first_sql_syntax += ";"   
print(first_sql_syntax)

mon_fichier = open("regions.sql", 'w')
mon_fichier.write(first_sql_syntax)
