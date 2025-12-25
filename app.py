from flask import Flask, render_template, request
from scanner import run_scanner

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def dashboard():
    results = []
    scanned_url = None
    if request.method == "POST":
        scanned_url = request.form.get("url")
        results = run_scanner(scanned_url)
    return render_template("dashboard.html", results=results, scanned_url=scanned_url)

if __name__ == "__main__":
    app.run(debug=True)
