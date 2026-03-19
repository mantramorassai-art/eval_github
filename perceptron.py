"""
PROJET : PERCEPTRON COLLABORATIF
EQUIPE : 6 DEVELOPPEURS
"""

# --- PERSONNE 2 : feature activation function ---
def hs(x):
    """
    TODO: Retourner 1 si x > 0, sinon 0.
    """
    pass

def relu(x):
    """
    TODO: Retourner x si x > 0, sinon 0.
    """
    pass


# --- PERSONNE 1 : feature input ---
def get_data(filename):
    """
    TODO: Lire le fichier filename.
    Retourner une liste de points [[x1, x2], ...] et une liste de labels [y, ...].
    """
    pass


# --- PERSONNE 3 : feature prediction ---
def predict(point, w1, w2, b):
    """
    TODO: Calculer la somme pondérée z = w1*x1 + w2*x2 + b.
    Passer z dans la fonction hs() de la Personne 2 et retourner le résultat.
    """
    pass


# --- PERSONNE 5 : feature output ---
def print_predict_all(points, labels, w1, w2, b):
    """
    TODO: Pour chaque point, afficher "Attendu: y | Prédit: y_hat".
    Afficher les poids finaux w1, w2 et b arrondis à 4 décimales.
    """
    pass


# --- MAIN ENGINE (PERSONNE 4 : feature train) ---
if __name__ == "__main__":
    # Paramètres d'apprentissage
    lr = 0.1
    epochs = 20
    
    # 1. Chargement des données (Utilisé par P4, codé par P1)
    # points, labels = get_data("data.txt")
    
    # 2. Initialisation des poids (w1, w2, b à 0.0)
    w1, w2, b = 0.0, 0.0, 0.0

    print("Début de l'entraînement...")

    # TODO PERSONNE 4 : Coder la boucle d'apprentissage ici
    # Indice : Pour chaque époque et chaque point :
    #   y_hat = predict(...)
    #   error = target - y_hat
    #   Mise à jour de w1, w2 et b selon la formule apprise
    
    print("Entraînement terminé.")

    # 3. Affichage des résultats (Appel de la fonction de P5)
    # print_predict_all(points, labels, w1, w2, b)
