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


if __name__ == "__main__":
    # essai = Sub_string("Toko est mon nom.",0, index_fin = 4)
    # print(essai)
    chaine  = input("<==")
    print(len(chaine))