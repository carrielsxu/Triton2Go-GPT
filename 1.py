from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score 
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
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

# Allergytype = (input("do you have any allergy?tell it by yes/no")).lower()
# while Allergytype == "yes":
#     hasAllergy(ratemyfood,food_unique) 
#     Allergytype = (input("do you have any allergy?tell it by yes/no")).lower()


# wantcalories(ratemyfood,food_unique)
# wantfat(ratemyfood,food_unique)
# wantprotein(ratemyfood,food_unique)
# wantCholesterol(ratemyfood,food_unique)
# wantSodium(ratemyfood,food_unique)
# wantCarbs(ratemyfood,food_unique)
# wantFiber(ratemyfood,food_unique)
# wantSugar(ratemyfood,food_unique)

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

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

X = food[[
    "Calories",
    "Protein",
    "Sodium",
    "Fat",
    "Carbs",
    "Allergy: dairy?",
    "Allergy: eggs?",
    "Allergy: gluten?",
    "Allergy: wheat?",
    "Allergy: sesame?",
    "Allergy: fish?",
    "Vegetarian?",
    "Vegan?"]]
food["Like"] = -1


# Ask the user to rate the recommended foods
for name in topchoice:

    answer = input("Do you like " + name + "? yes/no: ").lower()

    # Change yes into 1
    if answer == "yes":
        food.loc[food["Name"] == name, "Like"] = 1

    # Change no into 0
    if answer == "no":
        food.loc[food["Name"] == name, "Like"] = 0


# Keep only the foods that the user has already rated
rated_food = food[food["Like"] != -1]


# Choose the nutrition information that will be used to train the model
X = rated_food[[
    "Calories",
    "Protein",
    "Sodium",
    "Fat",
    "Carbs",
    "Fiber",
    "Sugar"
]]


# Store the user's like/dislike answers as the target values
y = rated_food["Like"]


# Check the training data
print(X)
print(y)


# Split the rated foods into training data and testing data
train_X, val_X, train_y, val_y = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)


# Create a Decision Tree Classifier model
model = DecisionTreeClassifier(random_state=0)


# Train the Decision Tree using the training data
model.fit(train_X, train_y)


# Use the trained model to predict the testing data
val_predictions = model.predict(val_X)


# Compare the predictions with the user's real answers
print("Prediction:")
print(val_predictions)

print("Actual answer:")
print(val_y)


# Calculate and print the accuracy of the Decision Tree
accuracy = accuracy_score(val_y, val_predictions)

print("Accuracy:")
print(accuracy)


# Find the foods that the user has not rated yet
unrated_food = food[food["Like"] == -1]


# Get the same nutrition features from the unrated foods
unrated_X = unrated_food[[
    "Calories",
    "Protein",
    "Sodium",
    "Fat",
    "Carbs",
    "Fiber",
    "Sugar"
]]


# Use the trained Decision Tree to predict the unrated foods
unrated_predictions = model.predict(unrated_X)


# Save the predictions into the DataFrame
unrated_food = unrated_food.copy()
unrated_food["Prediction"] = unrated_predictions


# Keep only foods that the model predicts the user will like
recommended_food = unrated_food[unrated_food["Prediction"] == 1]


# Print the predicted food recommendations
print("Machine Learning Recommendations:")

for name in recommended_food["Name"]:
    print(name)

unrated_food = food[food["Like"] == -1]
unrated_X = unrated_food[[
    "Calories",
    "Protein",
    "Sodium",
    "Fat",
    "Carbs",
    "Fiber",
    "Sugar"
]]

unrated_predictions = model.predict(unrated_X)