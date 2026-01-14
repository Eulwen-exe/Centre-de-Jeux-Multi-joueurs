def deviner_nombre(nombre_a_deviner):
    nombre_utilisateur = int(input("Saisi un nombre entre 10 et 20 : "))
    while not nombre_utilisateur == nombre_a_deviner:
        if nombre_utilisateur < nombre_a_deviner:
            print("Plus grand !")
        else:
            print("Plus petit !")
        nombre_utilisateur = int(input("Saisi un nombre entre 10 et 20 : "))
    print("Gagné !")