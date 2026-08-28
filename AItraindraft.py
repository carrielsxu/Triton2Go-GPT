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
food["Protein"] = pd.to_numeric(food["Protein"], errors="coerce")
food["Protein"] = food["Protein"].fillna(0)
food_unique = food.drop_duplicates(subset=["Name"])

allergy = input("Are you allergic to any? please type: dairy/ eggs / gluten / soy / wheat / sesame / fish/ no?")
for index, row in food_unique.iterrows():
    name = row["Name"]
    if row["Allergy: dairy?"] == "yes" and allergy == "dairy":
        del ratemyfood[name]
    if row["Allergy: eggs?"]  == "yes" and allergy == "egg":
        del ratemyfood[name]
    if row["Allergy: gluten?"]  == "yes" and allergy == "gluten":
        del ratemyfood[name]
    if row["Allergy: soy?"]  == "yes" and allergy == "soy":
        del ratemyfood[name]
    if row["Allergy: wheat?"]  == "yes" and allergy == "wheat":
        del ratemyfood[name]
    if row["Allergy: sesame?"]  == "yes" and allergy == "sesame":
        del ratemyfood[name]
    if row["Allergy: fish?"] == "yes" and allergy == "fish":
        del ratemyfood[name]
    else: 
        continue
for name1 in ratemyfood:
    print(name1,ratemyfood[name1])
# print(ratemyfood)


proteinchoice = input("Do you want high protein? yes/no: ")
Proteinlist = [] 
if proteinchoice == "yes":
    score = len(ratemyfood)
    while score > 0:
        highest_protein = -1
        highest_food = " "
        for index, row in food_unique.iterrows():
            if row["Name"] not in Proteinlist and row["Name"] in ratemyfood:
                if int(row["Protein"]) >= highest_protein:
                    highest_protein = int(row["Protein"])
                    highest_food = row["Name"]
        Proteinlist.append(highest_food)
        ratemyfood[highest_food] += score
        score -= 1
# print("after protein")
# print(ratemyfood["Turkey Meatball Sub"])

calorieschoice = input("Do you want high calories? yes/no: ")
calorieslist = [] 
if calorieschoice == "yes":
    score = len(ratemyfood)
    while score > 0:
        highest_calories = -1
        highest_food = " "
        for index, row in food_unique.iterrows():
            if row["Name"] not in calorieslist and row["Name"] in ratemyfood:
                if int(row["Calories"]) >= highest_calories:
                    highest_calories = int(row["Calories"])
                    highest_food = row["Name"]
        calorieslist.append(highest_food)
        ratemyfood[highest_food] += score
        score -= 1

Fatchoice = input("Do you want high calories? yes/no: ")
Fatlist = [] 
if Fatchoice == "yes":
    score = len(ratemyfood)
    while score > 0:
        highest_fats = -1
        highest_food = " "
        for index, row in food_unique.iterrows():
            if row["Name"] not in Fatlist and row["Name"] in ratemyfood:
                if int(row["Fat"]) >= highest_fats:
                    Fates = int(row["Fat"])
                    highest_food = row["Name"]
        Fatlist.append(highest_food)
        ratemyfood[highest_food] += score
        score -= 1

#test method
for name1 in ratemyfood:
    print(name1,ratemyfood[name1])
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