from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "It works as i expected :D"

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="vmetcd-1.mgt.depa.mx", port=5000, threaded=True, debug=True)
