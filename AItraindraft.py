from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score 
from sklearn.tree import DecisionTreeRegressor
import pandas as pd 
import numpy as np
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

from binaryrecomendfoodfunction import wantcalories,wantfat,wantprotein,wantCholesterol,wantSodium,wantCarbs,wantFiber,wantSugar,hasAllergy
# make a list
food = pd.read_csv("foods.csv")
menu = []
ratemyfood = {}
for name in food["Name"]:
    menu.append(name)
for foodname in menu: 
    ratemyfood[foodname] = 0

#basic set up
food["Fat"] = pd.to_numeric(food["Fat"], errors="coerce")
food["Fat"] = food["Fat"].fillna(0)
food["Calories"] = pd.to_numeric(food["Calories"], errors="coerce")
food["Calories"] = food["Calories"].fillna(0)
food["Cholesterol"] = pd.to_numeric(food["Cholesterol"], errors="coerce")
food["Cholesterol"] = food["Cholesterol"].fillna(0)
food["Sodium"] = pd.to_numeric(food["Sodium"], errors="coerce")
food["Sodium"] = food["Sodium"].fillna(0)
food["Carbs"] = pd.to_numeric(food["Carbs"], errors="coerce")
food["Carbs"] = food["Carbs"].fillna(0)
food["Fiber"] = pd.to_numeric(food["Fiber"], errors="coerce")
food["Fiber"] = food["Fiber"].fillna(0)
food["Sugar"] = pd.to_numeric(food["Sugar"], errors="coerce")
food["Sugar"] = food["Sugar"].fillna(0)
food["Protein"] = pd.to_numeric(food["Protein"], errors="coerce")
food["Protein"] = food["Protein"].fillna(0)


food_unique = food.drop_duplicates(subset=["Name"])

Allergytype = (input("do you have any allergy?tell it by yes/no")).lower()
while Allergytype == "yes":
    hasAllergy(ratemyfood,food_unique) 
    Allergytype = (input("do you have any allergy?tell it by yes/no")).lower()
    allowed_foods = list(ratemyfood.keys())


wantcalories(ratemyfood,food_unique)
wantfat(ratemyfood,food_unique)
wantprotein(ratemyfood,food_unique)
wantCholesterol(ratemyfood,food_unique)
wantSodium(ratemyfood,food_unique)
wantCarbs(ratemyfood,food_unique)
wantFiber(ratemyfood,food_unique)
wantSugar(ratemyfood,food_unique)

topchoice = []
for i in range(5):
    highest_score = -1
    highest_food = ""
    for name in ratemyfood:
        if name not in topchoice:
            if ratemyfood[name] > highest_score:
                highest_score = ratemyfood[name]
                highest_food = name
    topchoice.append(highest_food)
print(topchoice)

#############################################
# Choose the nutrition information that will be used to train the model
X = food[[
    "Calories",
    "Protein",
    "Sodium",
    "Fat",
    "Carbs",
   ]]

# Create a new column to store whether the user likes each food
# Ask the user to rate some foods as like or dislike
# Change the user's answer into 1 for like and 0 for dislike
# Store the user's like/dislike answers as the target values
# Keep only the foods that the user has already rated
# Store the user's like/dislike answers as the target values
#test value
food["Target"] = -1

ratemyfood = list(food["Name"].head(20))

for name in ratemyfood:
    answer = input("Do you like " + name + "? yes/no: ").lower()
    if answer == "yes":
        food.loc[food["Name"]==name,"Target"] = 1
    if answer == "no":
        food.loc[food["Name"]==name,"Target"] = 0   

ratemyfood = food[food["Target"]!= -1]
y = ratemyfood["Target"]


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
        if user["is_vegan"] and row["Vegan?"] not in [1, True, "yes"]:
            return 0
        if user["is_vegetarian"] and row["Vegetarian?"] not in [1, True, "yes"]:
            return 0

        # Rule 2: Allergen checks (If food contains allergen user is allergic to)
        if user["has_dairy_allergy"] and row["Allergy: dairy?"] in [1, True, "yes"]:
            return 0
        if user["has_gluten_allergy"] and row["Allergy: gluten?"] in [1, True, "yes"]:
            return 0

        # Rule 3: Time of day match (allow missing values or matching strings)
        if (
            pd.notna(row["Time of day"])
            and row["Time of day"] != user["current_time"]
        ):
            return 0

        return 1  # Food matches all preference criteria



# print(f"Target distribution:\n{y.value_counts()}")

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
    "Dining hall",]

accuracy_list = []
for i in range(10):
    # X = food[feature_cols].copy()
    X = ratemyfood[feature_cols].copy()

    # one-hot encode categorical strings ('time of day', 'dining hall', etc.)
    X = pd.get_dummies(X, drop_first=True)

    # split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size = 0.2, random_state = i
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


accuracy = accuracy_score(y_test, y_pred)
accuracy_list.append(accuracy)
print("Accuracy:", accuracy)
print("Average Accuracy:", np.mean(accuracy_list)) 

# Train the model again using all rated foods
X = ratemyfood[feature_cols].copy()
X = pd.get_dummies(X, drop_first=True)

X = X.fillna(X.median(numeric_only=True))

clf = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

clf.fit(X, y)


# Find foods that the user has not rated
unrated_food = food[
    (food["Target"] == -1) &
    (food["Name"].isin(allowed_foods))
].copy()

# Get the same features from unrated foods
unrated_X = unrated_food[feature_cols].copy()
unrated_X = pd.get_dummies(unrated_X, drop_first=True)


# Make sure unrated_X has exactly the same columns as training X
unrated_X = unrated_X.reindex(
    columns=X.columns,
    fill_value=0)

# Fill missing values
unrated_X = unrated_X.fillna(
    X.median(numeric_only=True))


# Predict whether the user will like each unrated food
unrated_predictions = clf.predict(unrated_X)


# Save prediction
unrated_food["Prediction"] = unrated_predictions


# Keep foods predicted as liked
recommended_food = unrated_food[
    unrated_food["Prediction"] == 1
].head(5)


print("Machine Learning Recommendations:")
for name in recommended_food["Name"]:
    print(name)