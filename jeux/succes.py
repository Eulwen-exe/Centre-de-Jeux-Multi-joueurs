liste_succes = [
    ["gg (premiere victoire)"],
    ["apprentit puant (10 parties joués)"],
    ["puant ultime (50 parties joués)"],
    ["tryhardeur (atteindre les 1000 points)"],
    ["encore en vie ! (gagner au pendue)"],
    ["maitre du calcul débutant (mode facile)"],
    ["maitre du calcul vétéran (mode moyen)"],
    ["maitre du calcul ultime (mode difficile)"],
    ["petit veinard (trouver le chiffre en moins de 5 essaies en mode facile)"],
    ["veinard (trouver le chiffre en moins de 8 essaies en mode moyen)"],
    ["veinard ultime (trouver le chiffre en moins de 15 essaies en mode difficile)"],
    ["gros golem (Gagner avec la pierre)"],
    ["maître du parchemin (Gagner avec le papier)"],
    ["bourreau affûté (Gagner avec le ciseau)"]
]


def verifier_succes():
    """
    affiche la liste des succès du joueur.

    fonctionnement :
        - demande le prénom
        - charge <prenom>.json
        - affiche la liste profil["succes"]
    """
    nom = input("Quel est ton nom ? : ")
    profil_informations = charger_profil(f"{nom}.json")
    print(f"Voici tous tes succès : {profil_informations['succes']}")


def succes_jeu(nom_fichier):
    """
    ajoute automatiquement certains succès en fonction des stats du joueur.

    paramètres :
        nom_fichier (str) : fichier profil du joueur (ex: "Elouan.json")

    succès gérés ici :
        - 10 parties jouées
        - 50 parties jouées
        - 1000 points cumulés
    """
    profil_information = charger_profil(nom_fichier)
    succes_1 = "apprentit puant (10 parties joués)"
    succes_2 = "puant ultime (50 parties joués)"
    succes_3 = "tryhardeur (atteindre les 1000 points)"

    if succes_1 not in profil_information["succes"]:
        if profil_information["parties"] >= 10:
            profil_information["succes"].append(succes_1)

    if succes_2 not in profil_information["succes"]:
        if profil_information["parties"] >= 50:
            profil_information["succes"].append(succes_2)

    if succes_3 not in profil_information["succes"]:
        if profil_information["score_total"] >= 1000:
            profil_information["succes"].append(succes_3)

    sauvegarder(nom_fichier, profil_information)