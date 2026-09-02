import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

# load data and convert '?' to NaN
food = pd.read_csv("foods.csv", na_values="?")

# example active user preferences (from your frontend UI or session)
user_pref = {
    "is_vegan": True,
    "is_vegetarian": True,
    "has_dairy_allergy": True,
    "has_gluten_allergy": False,
    "current_time": "Lunch",
}

def evaluate_food_match(row, user):
    # Rule 1: Strict Vegan / Vegetarian checks
    if user["is_vegan"] and row["Vegan?"] not in [1, True, "Yes"]:
        return 0
    if user["is_vegetarian"] and row["Vegetarian?"] not in [1, True, "Yes"]:
        return 0

    # Rule 2: Allergen checks (If food contains allergen user is allergic to)
    if user["has_dairy_allergy"] and row["Allergy: dairy?"] in [1, True, "Yes"]:
        return 0
    if user["has_gluten_allergy"] and row["Allergy: gluten?"] in [1, True, "Yes"]:
        return 0

    # Rule 3: Time of day match (allow missing values or matching strings)
    if (
        pd.notna(row["Time of day"])
        and row["Time of day"] != user["current_time"]
    ):
        return 0

    return 1  # Food matches all preference criteria


# Generate the 'y' target column
food["Target"] = food.apply(evaluate_food_match, user=user_pref, axis=1)

y = food["Target"]
print(f"Target distribution:\n{y.value_counts()}")

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