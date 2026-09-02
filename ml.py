# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier

# food_df = pd.read_csv("foods.csv")

# is_vegan_list = []
# for item in food_df["Vegan?"]:
#     if str(item).lower() == "yes":
#         is_vegan_list.append(1)
#     else:
#         is_vegan_list.append(0)

# no_dairy_list = []
# for item in food_df["Allergy: dairy?"]:
#     if str(item).lower() == "yes":
#         no_dairy_list.append(0) 
#     else:
#         no_dairy_list.append(1) 

# food_df["is_vegan"] = is_vegan_list
# food_df["no_dairy"] = no_dairy_list

# X = food_df[["is_vegan", "no_dairy"]]
# y = [1] * len(food_df)

# clf = DecisionTreeClassifier()
# clf.fit(X, y)


# def get_recommendation(text):
#     text = text.lower()
#     is_vegan = 1 if "vegan" in text else 0
#     no_dairy = 1 if "dairy" in text else 0

#     user_features = pd.DataFrame([[is_vegan, no_dairy]], columns=["is_vegan", "no_dairy"])
#     clf.predict(user_features)

#     name_column = "Name" 

#     if "vegan" in text:
#         match = food_df[food_df["is_vegan"] == 1][name_column].dropna().unique()
#     elif "dairy" in text:
#         match = food_df[food_df["no_dairy"] == 1][name_column].dropna().unique()
#     else:
#         match = food_df[name_column].dropna().unique()

#     if len(match) > 0:
#         return "I recommend: " + ", ".join(match[:3])
#     else:
#         return "No items found."

import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
    provider="auto"
)


def get_recommendation(text):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": """
You are Triton2Go GPT, a friendly AI food assistant for UCSD students.

Help users find food and answer questions about food.

Your responses should feel like a natural conversation with a helpful chatbot.

IMPORTANT RESPONSE STYLE:
- Keep responses relatively short and easy to read.
- Do not write long essays.
- Do not create large tables unless the user specifically asks for a table.
- When recommending multiple foods, use a short bullet list.
- Put each food recommendation on its own line.
- Use bold text for food names and important information.
- Use emojis occasionally when appropriate.
- Use short paragraphs with blank lines between them.
- Answer the user's actual question directly.
- Ask a short follow-up question when it would help continue the conversation.
- Do not include unnecessary nutrition advice unless the user asks for it.

Example of a good response:

Absolutely! Here are a few options that fit:

🥪 **Plant-Based Chickn Sandwich** — 435 calories

🥣 **Acai Bowl** — 476 calories

🥯 **Gluten-Free Bagel** — 410 calories

If you're looking for something savory, I'd recommend the Plant-Based Chickn Sandwich!

Want me to find something from a specific dining hall?
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content