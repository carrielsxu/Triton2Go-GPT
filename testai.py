import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
    provider="auto"
)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Hello! You are Triton2Go GPT. Say hello to me."
        }
    ]
)

print(response.choices[0].message.content)