from classical.double_transposition import DoubleTransposition

from utils.analysis import frequency_analysis
from utils.parsers import parse_permutation_key
from utils.validators import validate_permutation_key


def handle_double_transposition(form):
    plaintext = form.get("plaintext", "")

    if not plaintext:
        raise ValueError("Plaintext cannot be empty.")

    row_key = parse_permutation_key(
        form.get("row_key", "")
    )

    column_key = parse_permutation_key(
        form.get("column_key", "")
    )

    validate_permutation_key(row_key)
    validate_permutation_key(column_key)

    cipher = DoubleTransposition()

    ciphertext = cipher.encrypt(
        plaintext,
        row_key,
        column_key
    )

    decrypted = cipher.decrypt(
        ciphertext,
        row_key,
        column_key
    )

    return {
        "type": "double_transposition",
        "algorithm": "Double Transposition",
        "plaintext": plaintext,
        "row_key": row_key,
        "column_key": column_key,
        "ciphertext": ciphertext,
        "decrypted": decrypted,
        "frequency": frequency_analysis(ciphertext)
    }