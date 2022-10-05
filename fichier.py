import os

for i in range(4):
   first_name = input('region_name<--:')
#    last_name = input("last_name<--:")
   if i < 3:
        requete = "(\"" + first_name +"\"),\n"
   else:
        requete = "(\"" + first_name +"\");"
    
   print('\n')
   
   mon_fichier = open("regions.sql","a")
   
   mon_fichier.write(requete)
   mon_fichier.close()

   """
   delete from table where some_colum = some_value
   """
   

   # Je fais un petit nouveau test