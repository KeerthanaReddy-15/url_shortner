from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)
url_mapping = {}

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None
    if request.method == "POST":
        original_url = request.form["original_url"]
        short_code = generate_short_code()
        url_mapping[short_code] = original_url
        short_url = request.host_url + short_code
    return render_template("index.html", short_url=short_url)

@app.route("/<short_code>")
def redirect_to_original(short_code):
    original_url = url_mapping.get(short_code)
    if original_url:
        return redirect(original_url)
    return "Invalid short URL", 404

if __name__ == ("__main__"):
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
