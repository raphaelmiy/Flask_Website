from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "This is where the website content goes."

if __name__ == "__main__":
    app.run(debug=True)