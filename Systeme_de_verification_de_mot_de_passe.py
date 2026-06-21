# Systeme de verification de mot de passe
password = input("Entrez votre mot de passe : ")
passwordlenght = len(password)

# Verification de la longueur du mot de passe
if passwordlenght < 8:
    print("Le mot de passe est trop court.")
elif 8 < passwordlenght <= 20:
    print("Le mot de passe est valide.")
else:
    print("Le mot de passe est trop long.")