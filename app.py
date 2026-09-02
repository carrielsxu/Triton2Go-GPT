from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# 1. Load your foods file
food_data = pd.read_csv("foods.csv")


@app.route("/get-recommendations", methods=["POST"])
def get_recommendations():
    # Get the food name the user liked from the website
    user_input = request.json  # Example: {"liked_food": "Black Coffee"}
    liked_item_name = user_input.get("liked_food")

    # Find that food in your CSV file
    liked_food_row = food_data[food_data["Name"] == liked_item_name]

    if liked_food_row.empty:
        # If no food was picked yet, just show the first 3 foods
        suggestions = food_data["Name"].head(3).tolist()
    else:
        # Get the dining hall or time of day of the liked food
        dining_hall = liked_food_row["Dining hall"].values[0]

        # Find other foods from the same dining hall
        matching_foods = food_data[food_data["Dining hall"] == dining_hall]

        # Get up to 3 food names (excluding the one they already picked)
        suggestions = matching_foods[matching_foods["Name"] != liked_item_name][
            "Name"
        ].head(3).tolist()

    return jsonify({"recommended_foods": suggestions})


if __name__ == "__main__":
    app.run(port=5000)