"""
PROJET : PERCEPTRON COLLABORATIF
EQUIPE : 6 DEVELOPPEURS
"""

# --- PERSONNE 2 : feature activation function ---
def hs(x):
   return 1 if x>0 else 0
   

def relu(x):
   return x if x>0 else 0 

# --- PERSONNE 1 : feature input ---
def get_data(filename):
    """
    TODO: Lire le fichier filename.
    Retourner une liste de points [[x1, x2], ...] et une liste de labels [y, ...].
    """
    pass


# --- PERSONNE 1 : feature input ---
def get_data(filename):
    points = []
    labels = []
    with open(filename, 'r') as f: 
        for line in f:
            values = line.strip().split()
            x1 = int(values[0])
            x2 = int(values[1])
            y = int(values[2])
            points.append([x1, x2])
            labels.append(y)
    return points, labels 
    


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

    for i in range(len(points)):
        y_hat = predict(point[i], w1, w2, b)
        print(f"Attendu: {labels[i]} | Prédit: {y_hat}")

    print(f"Les poids finaux sont w1 = {w1:.4f}, w2 = {w2:.4f} et le biais est b = {b:.4f}. ")

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

    for iteration in range(10000) :
        y_hat = predict(points, w1, w2, b)
        error = target - y_hat
        
        grads_w2 = []
        for j in range(len(points)):
            w_temp = w2[j] + epochs
            y_temp = predict(points, w1, w_temp, b)
            error_temp = y_temp - y_true
            grad = (error_temp - error) / epochs
            grads_w2.append(grad)

        for j in range(len(points)):
            w2[j] -= lr * grads_w2[j]
    
    print("Entraînement terminé.")

    # 3. Affichage des résultats (Appel de la fonction de P5)
    # print_predict_all(points, labels, w1, w2, b)
