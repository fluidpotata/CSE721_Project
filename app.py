from flask import Flask, render_template, request, jsonify

from utils.substitution_handler import handle_substitution
from utils.transposition_handler import handle_double_transposition
from utils.des_handler import handle_des
from utils.aes_handler import handle_aes
from utils.rsa_handler import handle_rsa
from utils.ecc_handler import handle_ecc


app = Flask(__name__)


handlers = {
    "substitution": handle_substitution,
    "double_transposition": handle_double_transposition,
    "des": handle_des,
    "aes": handle_aes,
    "rsa": handle_rsa,
    "ecc": handle_ecc
}


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        algorithm = request.form.get("algorithm")
        try:
            handler = handlers.get(algorithm)

            if handler is None:
                raise ValueError("Invalid algorithm selected.")
            result = handler(request.form)

        except ValueError as e:
            error = str(e)

    return render_template(
        "index.html",
        result=result,
        error=error
    )


@app.route("/api/crypto", methods=["POST"])
def crypto():
    data = request.get_json()

    try:
        algorithm = data.get("algorithm")

        handler = handlers.get(algorithm)

        if handler is None:
            raise ValueError("Invalid algorithm selected.")

        result = handler(data)

        return jsonify({
            "success": True,
            "result": result
        })

    except ValueError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)