# donnee de variables wallet et computer 
wallet = 5000
computer = 1200

# condition pour vérifier si l'achat de l'ordinateur est possible ou pas
if computer <= wallet and computer > 1300:
    print("L'achat est possible.")
    wallet-= computer
    print("Il vous reste " + str(wallet) + " euros dans votre portefeuille.")
else:
    print("L'ordinateur est trop cher.")
    text = ("L'ordinateur est trop cher.", "L'ordinateur est abordable.") [wallet >= computer]
    print(text)