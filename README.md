# Triton2Go GPT

**Find your next campus meal with a conversation.**

Triton2Go GPT is an AI-powered food recommendation web app for UC San Diego students. Tell it what you're looking for, such as a vegan meal, a protein goal, or food from a specific dining location, and get suggestions based on a dataset of Triton2Go menu items.

The goal is simple: make deciding what to eat on campus easier, especially when you have dietary preferences or nutrition goals to consider.

## Features

- **Chat-based recommendations:** Ask for food suggestions in plain language.
- **Dietary filters:** Find vegan, vegetarian, gluten-free, and dairy-free options based on the dataset's labels.
- **Nutrition filters:** Set a calorie limit or minimum protein amount.
- **Location preferences:** Request items from a dining location included in the dataset.
- **Food details:** See available nutrition, dietary, allergen, and dining location information alongside recommendations.
- **Conversation history:** Ask follow-up questions within the same browser session. Refreshing the page resets the conversation.

## How it works

1. You enter a request in the web interface.
2. The JavaScript frontend sends your message and conversation history to Flask through `POST /chat`.
3. The backend filters `foods.csv` using supported dietary keywords, nutrition thresholds, and dining location names.
4. Matching rows are shuffled, and up to 100 are sent to a language model through Hugging Face's `InferenceClient`.
5. The model is instructed to recommend only foods from those rows, and its response is displayed in the chat.

The current model is `openai/gpt-oss-120b`, configured in [`ml.py`](ml.py). The web app uses dataset filtering and model inference; the separate decision-tree experiments are not part of its recommendation flow.

## Tech stack

| Part | Technology |
| --- | --- |
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask, Flask-CORS |
| Food data and filtering | CSV, pandas, regular expressions |
| AI responses | Hugging Face Hub / Inference Providers |
| Response formatting | Marked.js |

## Getting started

### Prerequisites

- Python 3 with `pip` and virtual environment support
- Git
- A Hugging Face access token with inference access to the configured model
- An internet connection for model requests and the Marked.js CDN

### 1. Clone the repository

```bash
git clone https://github.com/carrielsxu/Triton2Go-GPT.git
cd Triton2Go-GPT
```

### 2. Create and activate a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Set your Hugging Face token

Create an access token in your [Hugging Face settings](https://huggingface.co/settings/tokens), then set `HF_TOKEN` in the terminal where you'll run the app.

**macOS / Linux**

```bash
export HF_TOKEN="your_hugging_face_token"
```

**Windows PowerShell**

```powershell
$env:HF_TOKEN = "your_hugging_face_token"
```

The app reads `HF_TOKEN` from the environment when it starts. It does not automatically load a `.env` file. Keep your actual token out of source files and commits.

### 5. Start the app

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. Type a request, then press **Enter** or click **Submit**.

Run the app from the repository's root directory so it can find `foods.csv` and the frontend files. This command starts Flask's development server with debug mode enabled.

## Example requests

- "Find vegan food under 500 calories."
- "Show me meals with at least 20 g protein."
- "What vegetarian options are available at Scholar's Pizza?"
- "Find dairy-free food below 600 calories with at least 15 g protein."

For the current filters, use phrases such as `under 500 calories` and `at least 20 g protein`. Use the dining location's name as it appears in the dataset.

Conversation history is passed to the model, but dataset filters are applied to the latest message. Repeat any dietary or nutrition requirements you want to keep in a follow-up request.

## Project files

| File | Purpose |
| --- | --- |
| [`app.py`](app.py) | Flask routes, frontend file serving, and the `/chat` endpoint |
| [`ml.py`](ml.py) | Dataset loading, filtering, and Hugging Face model requests |
| [`foods.csv`](foods.csv) | Food names, nutrition values, dietary and allergen labels, and dining locations |
| [`index.html`](index.html) | Chat interface |
| [`style.css`](style.css) | Page and chat styling |
| [`script.js`](script.js) | Message submission, conversation history, and response rendering |
| [`requirements.txt`](requirements.txt) | Python dependencies for the web app |
| [`testai.py`](testai.py) | Standalone Hugging Face connection check |
| [`AItraindraft.py`](AItraindraft.py), [`1.py`](1.py), [`binaryrecomendfoodfunction.py`](binaryrecomendfoodfunction.py) | Separate recommendation and decision-tree experiments |

The experimental scripts use additional libraries that are not included in the web app's `requirements.txt`.

## Dataset and current scope

Recommendations use the included `foods.csv`, which contains menu and nutrition information collected from Triton2Go. The app does not fetch live menus, prices, or item availability.

The implemented dietary filters cover vegan, vegetarian, gluten-free, and dairy-free requests. Other allergen columns are included in the dataset but do not have dedicated filters in the current backend. Confirm current ingredients and allergen information with campus dining staff when choosing food for an allergy.

This is an independent student project and is not an official UC San Diego or Triton2Go service.
