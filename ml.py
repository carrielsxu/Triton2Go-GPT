import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

# load data and convert '?' to NaN
food = pd.read_csv("foods.csv", na_values="?")

# define target column 'y'
y = food["liked"]

# define feature columns 'X'
feature_cols = [
    "Calories",
    "Protein",
    "Sodium",
    "Fat",
    "Carbs",
    "Allergy: dairy?",
    "Allergy: eggs?",
    "Allergy: gluten?",
    "Allergy: soy?",
    "Allergy: wheat?",
    "Allergy: sesame?",
    "Allergy: fish?",
    "Vegetarian?",
    "Vegan?",
    "Time of day",
    "Kind of product?",
    "Dining hall",
]

X = food[feature_cols].copy()

# one-hot encode categorical strings ('time of day', 'dining hall', etc.)
X = pd.get_dummies(X, drop_first=True)

# split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 42
)

# initialize and fit classifier
X_train = X_train.fillna(X_train.median(numeric_only = True))
X_test = X_test.fillna(X_train.median(numeric_only = True))

clf = DecisionTreeClassifier(criterion = "gini", max_depth = 3, random_state = 42)
clf.fit(X_train, y_train)

# predict and evaluate
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# plot tree visualization
plt.figure(figsize = (12, 8))
plot_tree(
    clf,
    feature_names = X.columns.tolist(),
    class_names = [str(c) for c in clf.classes_],
    filled = True,
)
plt.show()