#Je veux concevoir des petits code en python

def Sub_string(chaine: str, index_depart, index_fin):
    chaine_finale = ""
    okay = bool()

    for i in range(index_fin):
        if i == index_depart:
           okay = True

        if okay:
            chaine_finale += chaine[i]

    return chaine_finale

def IsIn(caract):
    liste = ['0','1','2','3','4','5','6','7','8','9']
    for elt in liste:
        if caract[0] == elt:
            return False

    return True    

if __name__ == "__main__":
    # essai = Sub_string("Toko est mon nom.",0, index_fin = 4)
    # print(essai)
 nomTable = "Toko"
 first_sql_syntax = f"insert into {nomTable}("
 list_propriete = ["first_name", "last_name", "birth_date"]
 #on implement le code sql

#  print(len(list_propriete))
 for i in range(len(list_propriete)):
    #  print(i)
     if i == len(list_propriete) - 1:
          first_sql_syntax += list_propriete[i] + ")"
     else:     
         first_sql_syntax += list_propriete[i] + ","
 print(first_sql_syntax)