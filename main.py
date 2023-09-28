#Combat vs monsters w/ dices dnd style
import random
niveau_vie = 20
nombre_defaite = 0
nombre_victoire = 0

print("Vous vous retrouvez devant une porte, avec curiosité vous decidez de l'ouvrir")
#Continue jusqua que l'utilisateur n'a plus de vie.
while niveau_vie > 0:
    ############FAIRE MARCHER LE TRUC DE BOSSCHECK####################
    if nombre_victoire % 3 == 0 and nombre_victoire != 0:

        print("A la place d'un adversaire normal vous vous retrouvez devant un BOSS.")
        exit()
    force_adv = random.randint(1, 5)
    print("Vous tombez face à face avec un adversaire de difficulté : ", force_adv)
    print("Que voulez-vous faire? \n1- Combattre cet adversaire\n2- Contourner cet adversaire et aller ouvrir une autre porte"
          "\n3- Afficher les regles du jeu\n4- Quitter le jeu")
    def choix():
        # change la value des variable a global dans la fonction
        global niveau_vie
        global nombre_defaite
        global nombre_victoire
        x = str.strip(input("Votre choix: "))
        if x == "1":
            print("Vous avez ", niveau_vie, " vie et le monstre a ", force_adv, " de force, êtes vous certain? o/n ")
            y = str.strip(input("Votre choix: "))
            if y == "n":
                choix()
            else:
                score_de = random.randint(1, 6)
                print("Vous scorez un ", score_de, "!")

                if score_de <= force_adv:
                    print("Vous perdez contre l'adversaire!")
                    print("Vous perdez", force_adv, "niveaux de vie")
                    niveau_vie = niveau_vie - force_adv
                    nombre_defaite += 1
                    print("Vous avez perdu et avez ", niveau_vie, " niveaux de vie et ouvrez la porte devant vous")
                elif score_de > force_adv:
                    print("Vous gagnez contre l'adversaire!!!")
                    print("Vous recevez", force_adv, "niveaux de vie")
                    niveau_vie = niveau_vie + force_adv
                    nombre_victoire += 1
                    print("Vous avez gagné contre le monstre et ouvrez la porte devant vous avec ", niveau_vie,
                          " niveaux de vie")


        elif x == "2":
            print("Vous contournez l'adversaire et ouvrez la porte devant vous")
            niveau_vie -= 1
            print("Vous perdez 1 niveau de vie, vous avez maintenant: ", niveau_vie)



        elif x == "3":
            print("Les règles sont facile: \nVous commencez avec 20 niveaux de vie (Vous en avez ", niveau_vie, "maintenant) "
                "Vous allez vous battre contre un monstre d'une force entre 1 et 5. \nPour l'attaquer vous allez lancer un dé"
                 " de 1 - 6. \nSi vous scorez en dessous de son nombre de force, vous allez perdre le meme nombre de niveaux de vie"
                " qu'il a de force. \nSi vous gagnez, vous allez recevoir le nombre de force de l'enemi en tant que niveaux de vie"
                "\nLorsque vous recontrez un adversaire vous pouver choisir entre 4 options: \n1 pour le combattre, 2 pour l'éviter mais en perdant un point de vie,"
                " 3 pour revoir ces règles et 4 pour quitter le jeux" )
            choix()


        elif x == "4":
            print("Merci et au revoir")
            niveau_vie = 0



        else:
            print("Pas un choix valide, veuillez recommencer")
            choix()

    choix()





print("Vous êtes mort... Vous avez eu ", nombre_victoire, " victoires et ", nombre_defaite, " défaites")
exit()