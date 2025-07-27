from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        # Dummy logic for now (can replace with AI call)
        answer = f"You asked: {question}. This is your AI-generated response."
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
