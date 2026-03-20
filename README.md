# 🧠 Perceptron Collaboratif

Projet réalisé en groupe de 6 développeurs dans le cadre d'une évaluation. L'objectif était d'implémenter un **perceptron simple** (réseau de neurones à une couche) capable d'apprendre à classifier des points 2D à partir d'un fichier de données.

---

## 👥 Répartition des tâches

| Personne | Feature | Rôle |
|---|---|---|
| P1 | `feature input` | Lecture des données depuis un fichier (`get_data`) |
| P2 | `feature activation function` | Fonctions d'activation : Heaviside (`hs`) et ReLU (`relu`) |
| P3 | `feature prediction` | Calcul de la prédiction pour un point (`predict`) |
| P4 | `feature train` | Boucle d'entraînement principale (mise à jour des poids) |
| P5 | `feature output` | Affichage des résultats et des poids finaux (`print_predict_all`) |

---

## ⚙️ Fonctionnement

Le programme implémente un **perceptron monocouche** entraîné par la règle de Hebb/perceptron classique :

1. **Chargement des données** — lecture d'un fichier `data.txt` (deux features `x1`, `x2` et un label `y`)
2. **Initialisation** — poids `w1`, `w2` et biais `b` à `0.0`
3. **Entraînement** — 20 époques, taux d'apprentissage `lr = 0.1`  
   Pour chaque point : `error = y - ŷ`, puis mise à jour des poids :
   ```
   w1 = w1 + lr * error * x1
   w2 = w2 + lr * error * x2
   b  = b  + lr * error
   ```
4. **Prédiction** — activation Heaviside : `ŷ = 1 si z > 0, sinon 0`, avec `z = w1*x1 + w2*x2 + b`
5. **Affichage** — comparaison entre les labels attendus et prédits, + poids finaux

---

## 📁 Format du fichier `data.txt`

Chaque ligne contient trois valeurs séparées par des espaces :

```
x1 x2 label
```

Exemple :
```
1 2 1
3 4 1
0 0 0
```

---

## ▶️ Exécution

```bash
python perceptron.py
```

> Assurez-vous que `data.txt` se trouve dans le même dossier que le script.

---

## 🧪 Exemple de sortie

```
Début de l'entraînement...
Entraînement terminé.
Attendu: 1 | Prédit: 1
Attendu: 1 | Prédit: 1
Attendu: 0 | Prédit: 0
...
Les poids finaux sont w1 = 0.1000, w2 = 0.2000 et le biais est b = 0.1000.
```

---

## 🛠️ Pré-requis

- Python 3.x (aucune bibliothèque externe requise)

---

## 📌 Notes

- La fonction `relu` est définie mais non utilisée dans la version actuelle — elle pourrait remplacer `hs` pour d'autres expérimentations.
- Le modèle converge uniquement sur des données **linéairement séparables**.
