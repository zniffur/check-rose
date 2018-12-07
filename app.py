from flask import Flask, jsonify
from check import check_rose_html


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/system")
def system():
    name = 'Docker'
    mail = 'my_email@gmail.com'
    return jsonify(
        system=name,
        email=mail
    )


@app.route("/check")
def check_rose():
    mystring = check_rose_html()
    return mystring


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080, threaded=True)
