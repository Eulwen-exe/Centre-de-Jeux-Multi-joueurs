import json
from datetime import datetime
import os

profil = {"prenom": "",
          "date_creation": "",
          "parties": 0,
          "score_total": 0,
          "succes": []}


def sauvegarder(nom_fichier, dictionnaire):
    """
    sauvegarde un dictionnaire python dans un fichier json.

    paramètres :
        nom_fichier (str) : nom du fichier (ex: "Elouan.json")
        dictionnaire (dict) : données à enregistrer
    """
    with open(nom_fichier, "w", encoding="utf-8") as f:
        json.dump(dictionnaire, f, indent=4)


def charger_profil(nom_fichier):
    """
    charge un profil depuis un fichier json.

    paramètre :
        nom_fichier (str) : nom du fichier json à ouvrir

    retourne :
        dict : contenu du fichier json
    """
    with open(nom_fichier, "r", encoding="utf-8") as f:
        return json.load(f)


def voir_profil_joueur():
    """
    demande le prénom d'un joueur et affiche son profil depuis <prenom>.json.
    """
    nom_joueur = input("Saisi le nom du joueur dont tu veux voir le profil : ")
    profil_joueur = charger_profil(f"{nom_joueur}.json")
    print(profil_joueur)


def creer_profil():
    """
    crée un nouveau profil joueur.

    fonctionnement :
        - demande le prénom
        - crée le fichier <prenom>.json
        - initialise le profil et ajoute la date de création
        - sauvegarde le tout dans le fichier
    """
    prenom = input("Entrez votre prénom : ")
    with open(f"{prenom}.json", "x"):
        pass
    sauvegarder(f"{prenom}.json", profil)
    temp = charger_profil(f"{prenom}.json")
    temp["prenom"] = prenom
    temp["date_creation"] = datetime.now().strftime("%d/%m/%Y %H:%M")
    sauvegarder(f"{prenom}.json", temp)

def recupere_info_joueur():
    """
    récupère tous les profils (fichiers .json) présents dans le dossier courant.

    retourne :
        list[dict] : liste des profils trouvés
    """
    profils = []
    fichiers = os.listdir()
    for fichier in fichiers:
        if fichier.endswith(".json"):
            with open(fichier, "r", encoding="utf-8") as f:
                profil = json.load(f)
                profils.append(profil)
    return profils


def classement():
    """
    affiche un classement trié par score_total décroissant.
    """
    profils = recupere_info_joueur()
    profils.sort(key=lambda p: p["score_total"], reverse=True)
    for index, profil in enumerate(profils, start=1):
        print(index, profil["prenom"], ":", profil["score_total"])