# FAQ Chatbot (Flask + TF-IDF)

This project is a simple FAQ Chatbot built using Python, Flask, and Scikit-Learn.  
It takes a user question, compares it with predefined FAQs using TF-IDF and cosine similarity, and returns the best matching answer.

---

## Features

- Machine-learning-based FAQ matching using TF-IDF
- Real-time chatbot interface with Flask
- 30+ predefined FAQs stored in JSON format
- Handles unknown questions with fallback responses
- Lightweight and easy to extend

---

## Project Structure

```
project_folder/
│── app.py
│── model.py
│── faq_data.json
│── static/
│     └── style.css
│── templates/
│     └── index.html
│── requirements.txt
│── README.md
```

---

## Technologies Used

- Python 3.x  
- Flask  
- Scikit-Learn (TF-IDF, cosine similarity)  
- HTML, CSS  
- JSON  

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/faq-chatbot.git
cd faq-chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

Start the Flask application:

```bash
python app.py
```

Open the following URL in the browser:

```
http://127.0.0.1:5000/
```

---

## How It Works

1. All FAQ questions are loaded from `faq_data.json`.
2. Questions are converted into TF-IDF vectors using Scikit-Learn.
3. When the user asks a question:
   - The input is also converted into a TF-IDF vector.
   - Cosine similarity is calculated between the user query and stored FAQs.
   - The highest-scoring FAQ answer is returned.
4. If similarity is below a threshold, a fallback response is shown.

---

## Code Overview

### TF-IDF Matching Logic (model.py)

```python
query_vec = vectorizer.transform([user_query])
cosine_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
best_index = cosine_sim.argmax()
```

### Flask Application (app.py)

```python
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_question = request.form.get("question", "")
        bot_answer = get_best_answer(user_question)
        return render_template("index.html",
                               question=user_question,
                               answer=bot_answer)
    return render_template("index.html")
```

---

## Example

**User:** How do I track my order?  
**Bot:** You can track your order using the tracking link sent to your email.

---

## Future Improvements

- Add semantic search using sentence transformers
- Add voice input
- Add chatbot-style UI (chat bubbles)
- Add admin panel to manage FAQs
- Deploy on Render, Railway, or Vercel

---

## Author

Medaballi  Yamini  
Python and ML Developer  

