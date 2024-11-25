fichier = "fichier.txt"
try:
    with open(fichier, "r") as files:
        for ligne in files:
            print(ligne.rstrip())
except FileNotFoundError as erreur:
    print(f"The file {fichier} has been not found")
except IOError as erreur:
    print(f"The file {fichier} has occured an error while opening")
except FileExistsError as erreur:
    print(f"The file {fichier} you want to create, already exist")
except PermissionError as erreur:
    print(f"The file {fichier} Permission Denied")
