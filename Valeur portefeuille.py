def main():
    # demander à l'utilisateur d'entrer la valeur de son portefeuille
    wallet_value = float(input("Entrez la valeur de votre portefeuille : "))
    
    # enterer la valeur du téléphone
    phone_value = 500
    
    # calculer la nouvelle valeur du portefeuille 
    new_wallet_value = (wallet_value + phone_value)
    
    # afficher la nouvelle valeur du portefeuille après l'achat du téléphone
    print("La nouvelle valeur de votre portefeuille après l'achat du téléphone est : " + str(new_wallet_value))


if __name__ == "__main__":
    main()