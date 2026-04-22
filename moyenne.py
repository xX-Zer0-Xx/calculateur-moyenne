# ============================================================
# CALCULATEUR DE MOYENNE
# Un petit programme tout simple pour calculer ta moyenne
# ============================================================

def afficher_menu():
    """Affiche le menu"""
    print("\n" + "="*40)
    print("      CALCULATEUR DE MOYENNE")
    print("="*40)
    print("1. Calculer ma moyenne")
    print("2. Quitter")
    print("-"*40)


def calculer_moyenne():
    """Demande les notes et calcule la moyenne"""

    print("\n" + "-"*40)
    print("Entrez vos notes une par une")
    print("Quand vous avez fini, appuyez sur Entrée")
    print("-"*40 + "\n")

    # Liste pour stocker les notes
    notes = []

    # Boucle pour entrer les notes
    while True:
        note_input = input(f"Note {len(notes)+1} : ")

        # Si l'utilisateur appuie sur Entrée sans rien écrire
        if note_input == "":
            break

        # Convertir en nombre (avec gestion d'erreur si c'est pas un chiffre)
        try:
            note = float(note_input)
        except ValueError:
            print("Entrez un nombre valide !")
            continue

        # Vérifier que la note est valide
        if note < 0 or note > 20:
            print("Une note c'est entre 0 et 20 normalement...")
        else:
            notes.append(note)

    # Vérifier qu'il y a au moins une note
    if len(notes) == 0:
        print("\nT'as rien entré !")
        return

    # Calculer la somme des notes
    somme = 0
    for n in notes:
        somme = somme + n

    # Calculer la moyenne
    moyenne = somme / len(notes)

    # Afficher les résultats
    print("\n" + "="*40)
    print("            RESULTAT")
    print("="*40)
    print(f"Nombre de notes : {len(notes)}")
    print(f"Tes notes : {notes}")
    print(f"Moyenne : {moyenne:.2f}/20")

    # Petit commentaire
    if moyenne >= 16:
        print("Bravo ! T'es un boss !")
    elif moyenne >= 14:
        print("Bien joué !")
    elif moyenne >= 12:
        print("Pas mal, tu peux mieux faire")
    elif moyenne >= 10:
        print("Juste passer... faut bosser un peu")
    else:
        print("Là il faut vraiment travailler...")

    print("="*40)


# ============================================================
# LE PROGRAMME COMMENCE ICI
# ============================================================
print("\n" + "="*40)
print("     SALUT ! JE CALCULE TES MOYENNES")
print("="*40)

while True:
    afficher_menu()

    choix = input("Tu veux faire quoi ? ")

    if choix == "1":
        calculer_moyenne()
    elif choix == "2":
        print("\nAllez bon courage pour tes exams !")
        break
    else:
        print("\nJ'ai pas compris, choisis 1 ou 2")