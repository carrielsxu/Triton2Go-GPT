from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score 
import pandas as pd
import numpy as np
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


# print(ratemyfood)
# print("after protein")
# print(ratemyfood["Turkey Meatball Sub"])

#test method
# for name1 in ratemyfood:
#     print(name1,ratemyfood[name1])
# print(ratemyfood)

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



# # test button,don't use it except need
# # print(menu)
# print(ratemyfood)

#rate calculate function


# food = pd.read_csv("foods.csv")
# X = food[[
#     "Calories",
#     "Protein",
#     "Sodium",
#     "Fat",
#     "Carbs",
#     "Allergy: dairy?",
#     "Allergy: eggs?",
#     "Allergy: gluten?",
#     "Allergy: soy?",
#     "Allergy: wheat?",
#     "Allergy: sesame?",
#     "Allergy: fish?",
#     "Vegetarian?",
#     "Vegan?",
#     "Time of day",
#     "Kind of product?",
#     "Dining hall",
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