# coding : utf-8
jeu_lance = True
print(" ")

"""
Boucles : while / for
mots-clés : break (casse la boucle) / continue (revient au début de la boucle)

"""
while jeu_lance :
    # Fais des instructions en rapport avec le jeu
    choixMenu = input(" >")

    if choixMenu == "again":
        continue
    elif choixMenu == "quit":
        jeu_lance = False
    elif choixMenu == "hello":
        print("Bonjour :) !")
    else:
        print("Commande introuvable")
print("A bientot....")
## exemple for
sentence = "Bonjour tout le monde :) !"

for letter in sentence:
    print(letter)
print("A bientot")
