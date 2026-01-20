import random

theme_pendu = [
    [
        "chien", "chat", "lion", "tigre", "elephant", "girafe", "singe", "lapin",
        "cheval", "loup", "ours", "renard", "requin", "dauphin", "serpent", "aigle",
        "hibou", "panda", "koala", "kangourou", "zebre", "rhinoceros", "hippopotame",
        "crocodile", "alligator", "panthere", "leopard", "guepard", "baleine",
        "phoque", "otarie", "tortue", "pingouin", "manchot", "corbeau", "perroquet",
        "moineau", "souris", "rat", "hamster", "ecureuil", "herisson", "blaireau",
        "sanglier", "cerf", "biche", "chamois", "bouquet"
    ],
    [
        "pizza", "hamburger", "fromage", "pates", "riz", "poulet", "boeuf", "porc",
        "poisson", "chocolat", "gateau", "pomme", "banane", "fraise", "orange",
        "raisin", "poire", "ananas", "mangue", "pasteque", "salade", "tomate",
        "carotte", "brocoli", "courgette", "aubergine", "oignon", "ail", "pain",
        "baguette", "croissant", "sandwich", "soupe", "glace", "yaourt", "beurre",
        "creme", "lait", "oeuf", "omelette", "lasagne", "tacos", "kebab", "sushi",
        "ramen", "couscous", "paella", "quiche", "gratin"
    ],
    [
        "france", "espagne", "italie", "allemagne", "portugal", "belgique",
        "suisse", "autriche", "pologne", "grece", "suede", "norvege", "finlande",
        "danemark", "irlande", "royaumeuni", "islande", "canada", "etatsunis",
        "mexique", "bresil", "argentine", "chili", "perou", "colombie", "venezuela",
        "japon", "chine", "coree", "vietnam", "thailande", "inde", "pakistan",
        "nepal", "indonesie", "australie", "nouvellezelande", "egypte", "maroc",
        "algerie", "tunisie", "senegal", "nigeria", "kenya", "ethiopie",
        "afriquedusud", "turquie", "israel", "iran"
    ],
    [
        "ordinateur", "clavier", "souris", "ecran", "serveur", "reseau", "internet",
        "logiciel", "programme", "algorithme", "donnees", "base", "python", "java",
        "javascript", "html", "css", "sql", "linux", "windows", "macos", "processeur",
        "memoire", "disque", "stockage", "cloud", "securite", "parefeu", "cryptage",
        "hash", "motdepasse", "authentification", "api", "backend", "frontend",
        "framework", "bibliotheque", "debug", "compilation", "virtualisation",
        "conteneur", "docker", "git", "github", "commit", "branche", "merge",
        "bug", "latence"
    ],
    [
        "medecin", "enseignant", "ingenieur", "developpeur", "pompier", "policier",
        "avocat", "boulanger", "cuisinier", "journaliste", "architecte", "infirmier",
        "chirurgien", "dentiste", "pharmacien", "psychologue", "psychiatre",
        "electricien", "plombier", "menuisier", "charpentier", "maçon", "peintre",
        "decorateur", "designer", "graphiste", "photographe", "videaste",
        "realisateur", "acteur", "musicien", "compositeur", "chanteur", "professeur",
        "chercheur", "scientifique", "technicien", "administrateur", "analyste",
        "consultant", "comptable", "auditeur", "economiste", "banquier",
        "assureur", "courtier", "vendeur", "commercial", "manager"
    ],
    [
        "table", "chaise", "lampe", "telephone", "sac", "stylo", "cahier", "montre",
        "cle", "porte", "bouteille", "lunettes", "ordinateur", "telecommande",
        "television", "radio", "horloge", "miroir", "canape", "fauteuil", "lit",
        "oreiller", "couverture", "tapis", "rideau", "fenetre", "etagere", "armoire",
        "tiroir", "placard", "four", "microonde", "refrigerateur", "congelateur",
        "mixeur", "grillepain", "bouilloire", "aspirateur", "balai", "serpillere",
        "seau", "marteau", "tournevis", "perceuse", "scie", "clou", "vis",
        "chargeur", "batterie"
    ]
]

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
    """
    retourne l'affichage du mot du pendu avec des '_' pour les lettres non trouvées.

    paramètres :
        mot (str) : mot secret
        lettres (list[str]) : lettres déjà trouvées

    retourne :
        str : affichage du mot (avec espaces)
    """
    return " ".join([l if l in lettres else "_" for l in mot])


def jeu_pendu():
    """
    lance une partie du pendu, met à jour le score, les parties et certains succès.
    """
    prenom = input("Quel est votre prénom ? : ")
    compte = charger_profil(f"{prenom}.json")
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
        succes_1 = "gg (premiere victoire)"
        succes_2 = "encore en vie ! (gagner au pendue)"
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
                if succes_1 not in compte["succes"]:
                    compte["succes"].append(succes_1)
                if succes_2 not in compte["succes"]:
                    compte["succes"].append(succes_2)
                compte["parties"] += 1
                compte["score_total"] += 100
                sauvegarder(f"{prenom}.json", compte)
                succes_jeu(f"{prenom}.json")
                break
        else:
            print(pendu[erreur])
            print("Tu as perdu !")
            compte["parties"] += 1
            compte["score_total"] += 20
            sauvegarder(f"{prenom}.json", compte)
            succes_jeu(f"{prenom}.json")
    except ValueError:
        print("Erreur : vous devez entrer un nombre entier.")