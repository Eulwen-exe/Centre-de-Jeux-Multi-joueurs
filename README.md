# 🎮 mini-arcade python (profils, mini-jeux, succès, classement)

## 📌 description
ce projet est une mini-arcade en python avec :
- gestion de profils joueurs via fichiers `.json`
- 3 mini-jeux (pendu, deviner le nombre, calcul mental)
- un système de score total + nombre de parties
- un système de succès (débloqués automatiquement)
- un classement basé sur le score total

⚠️ le mode “calcul mental avec timer” utilise `msvcrt`, donc c’est **windows uniquement**.

---

## ✨ fonctionnalités

### 👤 profils joueurs
- création d’un profil (fichier `<prenom>.json`)
- affichage d’un profil existant
- date de création enregistrée automatiquement

### 🕹️ mini-jeux
1. **pendu**
   - choix d’un thème
   - 6 erreurs maximum
   - met à jour score + parties + succès

2. **deviner le nombre**
   - choix difficulté (facile / moyen / difficile)
   - l’ordinateur tire un nombre aléatoire
   - indications “plus grand / plus petit”
   - score + parties + succès selon performance

3. **calcul mental**
   - 5 questions
   - 30 secondes max par question
   - opérations aléatoires (+, -, *)
   - score + parties + succès selon difficulté et résultat

### 🏆 succès
- succès stockés dans la clé `succes` du profil (liste)
- ajout automatique selon :
  - nombre de parties jouées
  - score total atteint
  - performances dans les jeux

### 📊 classement
- lit tous les fichiers `.json` du dossier
- trie par `score_total` décroissant
- affiche le classement des joueurs

---

## ⚙️ prérequis
- python 3.13
- windows recommandé (à cause de `msvcrt`)

---

## 🚀 installation
1. placer le fichier python dans un dossier
2. lancer le programme dans un terminal :

```bash
python centre_de_jeu_multi-joueur.py
