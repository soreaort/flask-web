from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Looks like it is not updating automatically :("

if __name__ == "__main__":
    app.run(debug=True)
