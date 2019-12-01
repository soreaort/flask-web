from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Looks like it is not updating automatically :("

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="vmetcd-1.mgt.depa.mx", port=5000, threaded=True, debug=True)
