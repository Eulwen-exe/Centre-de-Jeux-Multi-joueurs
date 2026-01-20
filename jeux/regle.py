regle_calcul = (
    "Regles du jeu Calcul Mental :\n"
    "- Vous devez resoudre un maximum d'operations en 30 secondes.\n"
    "- Les operations peuvent etre des additions, soustractions, multiplications ou divisions.\n"
    "- Chaque bonne reponse rapporte 1 point.\n"
    "- Le chrono demarre des la premiere question.\n"
    "- Le but est d'obtenir le meilleur score possible avant la fin du temps."
)

regle_devine = (
    "Regles du jeu Devine le Nombre :\n"
    "- Le but est de trouver le nombre choisi aleatoirement par l'ordinateur.\n"
    "- Vous choisissez un niveau de difficulte :\n"
    "    * Facile : nombre entre 1 et 10\n"
    "    * Moyen : nombre entre 1 et 100\n"
    "    * Difficile : nombre entre 1 et 500\n"
    "-A chaque tentative, l'ordinateur indique si le nombre est plus grand ou plus petit.\n"
    "- Vous gagnez lorsque vous trouvez le bon nombre."
)

regle_pendu = (
    "Regles du jeu du Pendu :\n"
    "Trouvez le mot cache en proposant des lettres.\n "
    "Chaque erreur complete le dessin du pendu.\n "
    "Vous avez droit Ã 6 erreurs.\n "
    "Trouvez toutes les lettres avant la fin pour gagner.\n"
)


def afficher_regle():
    """
    affiche les règles des trois jeux (calcul mental, deviner le nombre, pendu).
    """
    print(regle_calcul)
    print(regle_devine)
    print(regle_pendu)