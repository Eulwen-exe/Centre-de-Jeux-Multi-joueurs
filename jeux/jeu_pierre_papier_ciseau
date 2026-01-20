def jeu_pierre_papier_ciseau():
    prenom = input("Quel est votre prénom ? : ")
    compte = charger_profil(f"{prenom}.json")
    succes_1 = "gros golem (Gagner avec la pierre)"
    succes_2 = "maître du parchemin (Gagner avec le papier)"
    succes_3 = "bourreau affûté (Gagner avec le ciseau)"
    joueur = input("Choisi, pierre, papier ou ciseau ? : ")
    ordinateur = random.choice(pierre_papier_ciseau)
    if joueur == ordinateur:
        print("égalité")
    elif joueur == "pierre" and ordinateur == "ciseau":
        print("tu as gagné !")
        compte["parties"] += 1
        compte["score_total"] += 50
        if succes_1 not in compte["succes"]:
            compte["succes"].append(succes_1)
    elif joueur == "papier" and ordinateur == "pierre":
        print("tu as gagné !")
        compte["parties"] += 1
        compte["score_total"] += 50
        if succes_2 not in compte["succes"]:
            compte["succes"].append(succes_2)
    elif joueur == "ciseau" and ordinateur == "papier":
        print("tu as gagné !")
        compte["parties"] += 1
        compte["score_total"] += 50
        if succes_3 not in compte["succes"]:
            compte["succes"].append(succes_3)
    elif joueur == "pierre" and ordinateur == "papier":
        print("tu as perdu !")
        compte["parties"] += 1
        compte["score_total"] += 20
    elif joueur == "papier" and ordinateur == "ciseau":
        print("tu as perdu !")
        compte["parties"] += 1
        compte["score_total"] += 20
    elif joueur == "ciseau" and ordinateur == "pierre":
        print("tu as perdu !")
        compte["parties"] += 1
        compte["score_total"] += 20
    sauvegarder(f"{prenom}.json", compte)
    succes_jeu(f"{prenom}.json")