from flask import Flask, render_template, request

from classical.substitution import Substitution
from classical.double_transposition import DoubleTransposition

from symmetric.des import DES
from symmetric.aes import AES

from asymmetric.rsa import RSA
from asymmetric.ecc import ECC


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        algorithm = request.form.get("algorithm")

        if algorithm == "substitution":
            pass
        elif algorithm == "double_transposition":
            pass
        elif algorithm == "des":
            pass
        elif algorithm == "aes":
            pass
        elif algorithm == "rsa":
            pass
        elif algorithm == "ecc":
            pass

    return render_template("index.html",result=result)


if __name__ == "__main__":
    app.run(debug=True)