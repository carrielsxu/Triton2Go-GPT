from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score 
import pandas as pd
import numpy as np

# make a list
food = pd.read_csv("foods.csv")
menu = []
ratemyfood = {}
for name in food["Name"]:
    menu.append(name)
for foodname in menu: 
    ratemyfood[foodname] = 0
print("hi Jing")
dairy_allergy = input("Are you allergic to dairy? yes/no: ")
if dairy_allergy == "yes":
    for index, row in food.iterrows():
        name = row["Name"]
        if row["Allergy: dairy?"] or row["Allergy: eggs?"] or row["Allergy: gluten?"] or row["Allergy: soy?"] or row["Allergy: wheat?"] or row["Allergy: sesame?"] or row["Allergy: fish?"] == "yes":
            del ratemyfood[name]
    print(ratemyfood)


# print(ratemyfood)
# # test button,don't use it except need
# # print(menu)
# print(ratemyfood)

#rate calculate function


# X = food[[
#     "Calories",
#     "Protein",
#     "Sodium",
#     "Fat",
#     "Carbs",
#     "Vegetarian?",
#     "Major allergens?",
#     "Vegan?"
# ]]


# y = []
# print(X.shape)

# food_features = X 
# favourite_labels = y

# # Logistic Regression

# favourite_prediction_accuracies = []

# food_train, food_test, favourite_train, favourite_test = train_test_split(
#     food_features,
#     favourite_labels,
#     test_size=0.2,
#     random_state=5
#     )

  
# scaler = StandardScaler()
# food_train = scaler.fit_transform(food_train)
# food_test = scaler.transform(food_test)
# food_preference_model = LogisticRegression(max_iter=1000)
# food_preference_model.fit(food_train, favourite_train)
# prediction_accuracy = food_preference_model.score(
#         food_test,
#         favourite_test
# )

# favourite_prediction_accuracies.append(prediction_accuracy)

# print(np.mean(favourite_prediction_accuracies))