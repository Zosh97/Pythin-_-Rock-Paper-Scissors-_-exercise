import random
import urllib.request
from PIL import Image

#
def display_image(chemin_image):
    img = Image.open(chemin_image)
    img.show()
    return 0



liste = ["Pierre", "Papier", "Ciseaux"]

coup = "Oui"
while coup == "Oui":
    for x in liste:
        print(x)

    print("Bonjour, vous jouez le chifoumi avec l'ordinateur.Choisissez un objet entre les objets au-dessus. ")
    choix_J = input("Tapez correctement l'objet que vous choisissez: ").capitalize()
    score_J = 0
    score_ordi = 0

    while choix_J not in liste:
        print("Votre choix n'est dans le jeu. Tapez correctement s'il vous plaît. ")
        choix_J = input("Tapez correctement l'objet que vous choisissez: ").capitalize()


    if choix_J == "Pierre":
        img_url_pierre = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Rock-paper-scissors_%28rock%29.png/150px-Rock-paper-scissors_%28rock%29.png'
        urllib.request.urlretrieve(img_url_pierre, "pierre.png")
        display_image("pierre.png")

    elif choix_J == "Papier":
        img_url_papier = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Rock-paper-scissors_%28paper%29.png/150px-Rock-paper-scissors_%28paper%29.png'
        urllib.request.urlretrieve(img_url_papier, "papier.png")
        display_image("papier.png")

    elif choix_J == "Ciseaux":
        img_url_ciseaux = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Rock-paper-scissors_%28scissors%29.png/150px-Rock-paper-scissors_%28scissors%29.png'
        urllib.request.urlretrieve(img_url_ciseaux, "ciseaux.png")
        display_image("ciseaux.png")

    choix_ordi = random.choice(liste)

    if choix_ordi == "Pierre":
        img_url_pierre = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Rock-paper-scissors_%28rock%29.png/150px-Rock-paper-scissors_%28rock%29.png'
        urllib.request.urlretrieve(img_url_pierre, "pierre.png")
        display_image("pierre.png")

    elif choix_ordi == "Papier":
        img_url_papier = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Rock-paper-scissors_%28paper%29.png/150px-Rock-paper-scissors_%28paper%29.png'
        urllib.request.urlretrieve(img_url_papier, "papier.png")
        display_image("papier.png")

    elif choix_ordi == "Ciseaux":
        img_url_ciseaux = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Rock-paper-scissors_%28scissors%29.png/150px-Rock-paper-scissors_%28scissors%29.png'
        urllib.request.urlretrieve(img_url_ciseaux, "ciseaux.png")
        display_image("ciseaux.png")

    print(f"Le choix de l'ordinateur est {choix_ordi}")
    if choix_J == choix_ordi:
        print("Personne n'a gagné.")

    elif (choix_J == "Pierre" and choix_ordi == "Ciseaux") or (choix_J== "Papier" and choix_ordi == "Pierre") or (choix_J == "Ciseaux" and choix_ordi == "Papier"):
        score_J+= 1
        print(f"Votre choix est {choix_J} et le choix de l'odinateur est {choix_ordi}. Vous avez gagné.")

    else:
        score_ordi +=1
        print(f"Votre choix est {choix_J} et le choix de l'odinateur est {choix_ordi}. L'ordinateur a gagné. ")


    coup = input("Vous voulez continuer à jouer?(Oui ou Non)").capitalize()
    while coup != "Oui" and coup != "Non":
        coup = input("Vous voulez continuer à jouer?(Oui ou Non)").capitalize()

    print("Bonne journée. A bientôt")
