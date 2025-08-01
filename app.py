@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        question = request.form.get("question")

        # Dummy logic
        if "exam" in question.lower():
            response = "Focus on past year questions and time management."
        elif "career" in question.lower():
            response = "Consider your interests and explore internships."
        else:
            response = "That's a great question! Keep learning."

    return render_template("index.html", response=response)
