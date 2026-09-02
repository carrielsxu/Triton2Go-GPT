import pandas as pd
from sklearn.tree import DecisionTreeClassifier

food_df = pd.read_csv("foods.csv")

is_vegan_list = []
for item in food_df["Vegan?"]:
    if str(item).lower() == "yes":
        is_vegan_list.append(1)
    else:
        is_vegan_list.append(0)

no_dairy_list = []
for item in food_df["Allergy: dairy?"]:
    if str(item).lower() == "yes":
        no_dairy_list.append(0) 
    else:
        no_dairy_list.append(1) 

food_df["is_vegan"] = is_vegan_list
food_df["no_dairy"] = no_dairy_list

X = food_df[["is_vegan", "no_dairy"]]
y = [1] * len(food_df)

clf = DecisionTreeClassifier()
clf.fit(X, y)


def get_recommendation(text):
    text = text.lower()
    is_vegan = 1 if "vegan" in text else 0
    no_dairy = 1 if "dairy" in text else 0

    user_features = pd.DataFrame([[is_vegan, no_dairy]], columns=["is_vegan", "no_dairy"])
    clf.predict(user_features)

    name_column = "Name" 

    if "vegan" in text:
        match = food_df[food_df["is_vegan"] == 1][name_column].dropna().unique()
    elif "dairy" in text:
        match = food_df[food_df["no_dairy"] == 1][name_column].dropna().unique()
    else:
        match = food_df[name_column].dropna().unique()

    if len(match) > 0:
        return "I recommend: " + ", ".join(match[:3])
    else:
        return "No items found."