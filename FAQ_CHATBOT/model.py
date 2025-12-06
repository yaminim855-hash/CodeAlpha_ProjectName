import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQs
with open("faq_data.json", "r") as f:
    faqs = json.load(f)

questions = [item["question"] for item in faqs]

# Convert FAQs → TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(questions)

def get_best_answer(user_query: str) -> str:
    """Return best matching FAQ answer."""
    
    if not user_query.strip():
        return "Please type a question."

    query_vec = vectorizer.transform([user_query])
    cosine_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()

    best_index = cosine_sim.argmax()
    best_score = cosine_sim[best_index]

    # Low similarity → generic response
    if best_score < 0.2:
        return "Sorry, I couldn't find a relevant answer. Try rephrasing."

    return faqs[best_index]["answer"]
