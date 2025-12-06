from flask import Flask, render_template, request
from model import get_best_answer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    user_question = ""
    bot_answer = ""
    if request.method == "POST":
        user_question = request.form.get("question", "")
        bot_answer = get_best_answer(user_question)
    return render_template("index.html",
                           question=user_question,
                           answer=bot_answer)

if __name__ == "__main__":
    app.run(debug=True)
