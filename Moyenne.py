def main():
    # recuperer la première note 
     note1 = int (input("Entrez la première note : "))
     # recuperer la deuxième note
     note2 = int (input("Entrez la deuxième note : "))
     # recuperer la troisième note
     note3 = int (input("Entrez la troisième note : "))
     # calculer la moyenne des trois notes
     moyenne = (note1 + note2 + note3) / 3
     # afficher la moyenne des trois nombres
     print("La moyenne des trois notes est :" + str(moyenne))
    
    #appel de la fonction main
if __name__ == "__main__":
    main()