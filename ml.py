import os
import re
import pandas as pd
from huggingface_hub import InferenceClient


# Load the food data
food_df = pd.read_csv("foods.csv")


# Connect to Hugging Face
client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
    provider="auto"
)


def get_recommendation(text, history):

    text_lower = text.lower()

    # Start with every food in the CSV
    matches = food_df.copy()


    # VEGAN
    if "vegan" in text_lower:
        matches = matches[matches["Vegan?"].str.lower() == "yes"]


    # VEGETARIAN
    elif "vegetarian" in text_lower:
        matches = matches[matches["Vegetarian?"].str.lower() == "yes"]


    # GLUTEN-FREE
    if "gluten-free" in text_lower or "gluten free" in text_lower:
        matches = matches[
            matches["Allergy: gluten?"].str.lower() == "no"
        ]


    # DAIRY-FREE
    if "dairy-free" in text_lower or "dairy free" in text_lower:
        matches = matches[
            matches["Allergy: dairy?"].str.lower() == "no"
        ]


    # CALORIE LIMIT
    calorie_match = re.search(
        r"(?:under|below|less than|maximum of|max|<=|≤)\s*(\d+)\s*(?:calories|cal|kcal)?",
        text_lower
    )

    if calorie_match:

        calorie_limit = int(calorie_match.group(1))

        matches = matches[
            pd.to_numeric(
                matches["Calories"],
                errors="coerce"
            ) <= calorie_limit
        ]


    # PROTEIN MINIMUM
    protein_match = re.search(
        r"(?:at least|minimum of|minimum|more than|over|>=|≥)\s*(\d+)\s*(?:g|grams)?\s*protein",
        text_lower
    )

    if protein_match:

        protein_minimum = int(protein_match.group(1))

        matches = matches[
            pd.to_numeric(
                matches["Protein"],
                errors="coerce"
            ) >= protein_minimum
        ]


    # DINING HALL
    dining_halls = food_df["Dining hall"].dropna().unique()

    for hall in dining_halls:

        if hall.lower() in text_lower:

            matches = matches[
                matches["Dining hall"] == hall
            ]


    # NO MATCHES
    if len(matches) == 0:

        return (
            "I couldn't find any foods in my dataset "
            "that match those requirements."
        )


    # Shuffle the matching foods so different foods appear each time
    matches = matches.sample(frac=1).reset_index(drop=True)

    # Send up to 100 matching foods to the AI
    matches = matches.head(100)


    # Turn the matching CSV rows into text
    food_information = matches.to_string(index=False)


    # Ask the AI
    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[

            {
                "role": "system",

                "content": """
You are Triton2Go GPT, a friendly AI food assistant for UCSD students.

IMPORTANT:

You may ONLY recommend foods that appear in the FOOD DATA provided by the program.

The FOOD DATA comes directly from foods.csv.

DO NOT invent foods.

DO NOT use foods from your general knowledge.

DO NOT make up dining halls.

DO NOT make up calories.

DO NOT make up protein amounts.

DO NOT make up allergy information.

DO NOT make up dietary information.

If a food does not appear in the FOOD DATA, DO NOT mention it.

The FOOD DATA is your ONLY source of food information.

Use the exact food names provided.

When recommending foods, use a short bullet list with one food per line.

Include calories, protein, and dining hall in EVERY SINGLE ANSWER provided that it is available.

Keep responses conversational and relatively short.

If there are no matching foods in the FOOD DATA, say that no matching foods were found.

Never ask the user to provide the CSV.

Remember the previous conversation when answering follow-up questions.

ALWAYS randomize every single answer option's foods and do not respond with the same first few foods at the beginning of the list.

Carefully look at every single item in the given file.

An example of a good answer:

Signature Cheese Pizza - Calories: 745, Cholesterol: 71 mg, Sodium: 1359 mg, Carbs: 99 g, Fiber: 1 g, Sugar: 1g, Protein: 35 g, Dining Hall: Scholar's Pizza

"""
            },

            # previous conversation
            *history,

            # current question and matching foods
            {
                "role": "user",

                "content": f"""
The user is asking:

{text}

Here are the matching foods found directly in foods.csv:

{food_information}

IMPORTANT:
You may ONLY recommend foods from the FOOD DATA above.
Do not mention any other foods.
"""
            }

        ]
    )


    return response.choices[0].message.content


# # import pandas as pd
# # from sklearn.tree import DecisionTreeClassifier

# # food_df = pd.read_csv("foods.csv")

# # is_vegan_list = []
# # for item in food_df["Vegan?"]:
# #     if str(item).lower() == "yes":
# #         is_vegan_list.append(1)
# #     else:
# #         is_vegan_list.append(0)

# # no_dairy_list = []
# # for item in food_df["Allergy: dairy?"]:
# #     if str(item).lower() == "yes":
# #         no_dairy_list.append(0) 
# #     else:
# #         no_dairy_list.append(1) 

# # food_df["is_vegan"] = is_vegan_list
# # food_df["no_dairy"] = no_dairy_list

# # X = food_df[["is_vegan", "no_dairy"]]
# # y = [1] * len(food_df)

# # clf = DecisionTreeClassifier()
# # clf.fit(X, y)


# # def get_recommendation(text):
# #     text = text.lower()
# #     is_vegan = 1 if "vegan" in text else 0
# #     no_dairy = 1 if "dairy" in text else 0

# #     user_features = pd.DataFrame([[is_vegan, no_dairy]], columns=["is_vegan", "no_dairy"])
# #     clf.predict(user_features)

# #     name_column = "Name" 

# #     if "vegan" in text:
# #         match = food_df[food_df["is_vegan"] == 1][name_column].dropna().unique()
# #     elif "dairy" in text:
# #         match = food_df[food_df["no_dairy"] == 1][name_column].dropna().unique()
# #     else:
# #         match = food_df[name_column].dropna().unique()

# #     if len(match) > 0:
# #         return "I recommend: " + ", ".join(match[:3])
# #     else:
# #         return "No items found."

# import os
# from huggingface_hub import InferenceClient

# client = InferenceClient(
#     api_key=os.environ["HF_TOKEN"],
#     provider="auto"
# )


# def get_recommendation(text):

#     response = client.chat.completions.create(
#         model="openai/gpt-oss-120b",
#         messages=[
#             {
#                 "role": "system",
#                 "content": """
# You are Triton2Go GPT, a friendly AI food assistant for UCSD students.

# Help users find food and answer questions about food. Every single food that comes from your answer should already have been provided in the code that has been written for this program.

# Your responses should feel like a natural conversation with a helpful chatbot.

# IMPORTANT RESPONSE STYLE:
# - Keep responses relatively short and easy to read.
# - Do not write long essays.
# - Do not create large tables unless the user specifically asks for a table.
# - When recommending multiple foods, use a short bullet list.
# - Put each food recommendation on its own line.
# - Use bold text for food names and important information.
# - Use emojis occasionally when appropriate.
# - Use short paragraphs with blank lines between them.
# - Answer the user's actual question directly.
# - Provide every single information given per food item, including and not limiting to calorie count, dining hall information, etc.
# - Ask a short follow-up question when it would help continue the conversation.
# - Do not include unnecessary nutrition advice unless the user asks for it.
# - Only use the food data that has been provided. Do not use outside information when formulating an answer.
# - The answers cannot contain items that are not from foods.csv. Only give foods provided from the data given already.

# Example of a good response:

# Absolutely! Here are a few options that fit:

# 🥪 **Plant-Based Chickn Sandwich** — 435 calories

# 🥣 **Acai Bowl** — 476 calories

# 🥯 **Gluten-Free Bagel** — 410 calories

# If you're looking for something savory, I'd recommend the Plant-Based Chickn Sandwich!

# Want me to find something from a specific dining hall?
# """
#             },
#             {
#                 "role": "user",
#                 "content": text
#             }
#         ]
#     )

#     return response.choices[0].message.content