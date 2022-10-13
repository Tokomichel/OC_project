import re 

#Je veux concevoir des petits code en python

class Id_property():
    def __init__(nom: str, index: int, compteur: int = 0):
        self.nom = nom
        self.index = index
        self.compteur = compteur
    
    def Incrementation(pas: int):
       self.compteur += pas
       return self.compteur

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

def Contenue(text: str):
    if re.match(r"[A-Za-z0-9 -]*(id)[A-Za-z0-9 _]*", "Je cherche un id"):
        return True
    else:
        return False




if __name__ == "__main__":
    # texte = "Ma fonction doit chercher le mot id"
    # pattern = "id"
    # print(MyOwnRegex(texte,pattern))
    Tuple = (1,"toko")
    print(Tuple)
  

     