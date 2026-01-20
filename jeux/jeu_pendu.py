import random

theme_pendu = [[
    "chien", "chat", "lion", "tigre", "elephant", "girafe",
    "singe", "lapin", "cheval", "loup", "ours", "renard",
    "requin", "dauphin", "serpent", "aigle"
], [
    "pizza", "hamburger", "fromage", "pates", "riz", "poulet",
    "chocolat", "gateau", "pomme", "banane", "fraise",
    "sandwich", "soupe", "glace"
], [
    "france", "espagne", "italie", "allemagne", "portugal",
    "canada", "bresil", "argentine", "japon", "chine",
    "australie", "inde", "egypte"
], [
    "python", "ordinateur", "clavier", "souris", "ecran",
    "reseau", "serveur", "internet", "logiciel",
    "programme", "algorithme", "donnees"
], [
    "medecin", "enseignant", "ingenieur", "developpeur",
    "pompier", "policier", "avocat", "boulanger",
    "cuisinier", "journaliste", "architecte"
], [
    "table", "chaise", "lampe", "telephone", "sac",
    "stylo", "cahier", "montre", "cle", "porte",
    "bouteille", "lunettes"
]]

pendu = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """
]

def afficher_mot(mot, lettres):
    return " ".join([l if l in lettres else "_" for l in mot])


def jeu_pendu():
    menu = """
    1 - animaux
    2 - nourriture
    3 - pays
    4 - informatique
    5 - metiers
    6 - objets
    """
    try:
        index = int(input(menu))
        theme = theme_pendu[index - 1]
        mot_secret = random.choice(theme)
        lettre_trouve = []
        erreur = 0
        erreur_max = 6
        while erreur < erreur_max:
            print(f"Mot : {afficher_mot(mot_secret, lettre_trouve)}")
            lettre = input("Choisis une lettre : ")
            print(f"Lettre proposé : {lettre}")
            if lettre in lettre_trouve:
                print("Tu as déjà trouvé cette lettre")
                continue
            if lettre in mot_secret:
                lettre_trouve.append(lettre)
                print("Tu as trouvé une lettre !")
            else:
                print("La lettre n'est pas dans le mot")
                print(pendu[erreur])
                erreur += 1
            if "_" not in afficher_mot(mot_secret, lettre_trouve):
                print("tu as gagné !")
                break
        else:
            print(pendu[erreur])
            print("Tu as perdu !")
    except ValueError:
        print("Erreur : vous devez entrer un nombre entier.")