from classical.substitution import Substitution

from analysis import frequency_analysis
from validators import validate_substitution_key


def handle_substitution(form):
    plaintext = form.get("plaintext", "")
    key = form.get("substitution_key", "").upper()

    validate_substitution_key(key)

    cipher = Substitution()

    ciphertext = cipher.encrypt(
        plaintext,
        key
    )

    decrypted = cipher.decrypt(
        ciphertext,
        key
    )

    return {
        "type": "substitution",
        "algorithm": "Substitution Cipher",
        "plaintext": plaintext,
        "key": key,
        "ciphertext": ciphertext,
        "decrypted": decrypted,
        "frequency": frequency_analysis(ciphertext)
    }