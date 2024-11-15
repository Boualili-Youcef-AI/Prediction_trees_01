class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
    
    def affichage(self):
        print(f"Marque {self.marque}")
        print(f"Modele {self.modele}")

v1 = Voiture("Merco","AMG")
v1.affichage()