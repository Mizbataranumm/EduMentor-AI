from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        question = request.form.get("question")
        
        # Dummy AI response (you can replace this with ChatGPT API later)
        if "exam" in question.lower():
            response = "Focus on past year questions and time management."
        elif "career" in question.lower():
            response = "Consider your interests and explore internships in that area."
        else:
            response = "That's a great question! Keep learning and stay curious."

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
