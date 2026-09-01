from classical.substitution import Substitution

from utils.analysis import frequency_analysis
from utils.validators import validate_substitution_key


def handle_substitution(data):
    operation = data.get("operation")

    key = data.get(
        "substitution_key",
        ""
    ).upper()

    validate_substitution_key(key)

    cipher = Substitution()

    if operation == "encrypt":

        plaintext = data.get(
            "plaintext",
            ""
        )

        if not plaintext:
            raise ValueError(
                "Plaintext cannot be empty."
            )

        ciphertext = cipher.encrypt(
            plaintext,
            key
        )

        return {
            "algorithm": "substitution",
            "operation": "encrypt",

            "plaintext": plaintext,
            "key": key,

            "ciphertext": ciphertext,

            "frequency":
                frequency_analysis(ciphertext)
        }

    elif operation == "decrypt":

        ciphertext = data.get(
            "ciphertext",
            ""
        )

        if not ciphertext:
            raise ValueError(
                "Ciphertext cannot be empty."
            )

        plaintext = cipher.decrypt(
            ciphertext,
            key
        )

        return {
            "algorithm": "substitution",
            "operation": "decrypt",

            "ciphertext": ciphertext,
            "key": key,

            "plaintext": plaintext,

            "frequency":
                frequency_analysis(ciphertext)
        }


    raise ValueError(
        "Invalid Substitution operation."
    )