from classical.double_transposition import DoubleTransposition

from utils.analysis import frequency_analysis
from utils.parsers import parse_permutation_key
from utils.validators import validate_permutation_key


def handle_double_transposition(data):
    operation = data.get("operation")

    try:
        row = int(data.get("row"))
        col = int(data.get("col"))

    except (TypeError, ValueError):
        raise ValueError(
            "Rows and columns must be integers."
        )

    if row <= 0 or col <= 0:
        raise ValueError(
            "Rows and columns must be greater than zero."
        )


    row_key = parse_permutation_key(
        data.get("row_key", "")
    )

    col_key = parse_permutation_key(
        data.get("column_key", "")
    )

    validate_permutation_key(row_key)
    validate_permutation_key(col_key)

    if len(row_key) != row:
        raise ValueError(
            f"Row key must contain exactly {row} values."
        )

    if len(col_key) != col:
        raise ValueError(
            f"Column key must contain exactly {col} values."
        )


    cipher = DoubleTransposition(
        row,
        col
    )


    if operation == "encrypt":

        plaintext = data.get("plaintext", "")

        if not plaintext:
            raise ValueError(
                "Plaintext cannot be empty."
            )

        size = row * col

        if size < len(plaintext):
            raise ValueError(
                f"Matrix is too small. "
                f"{row} × {col} can hold {size} characters, "
                f"but plaintext contains {len(plaintext)} characters."
            )

        ciphertext = cipher.encrypt(
            plaintext,
            row_key,
            col_key
        )

        plaintext = cipher.decrypt(
            ciphertext,
            row_key,
            col_key
        )

        return {
            "algorithm": "double_transposition",
            "operation": "encrypt",

            "plaintext": plaintext,

            "row": row,
            "col": col,

            "row_key": row_key,
            "column_key": col_key,

            "ciphertext": ciphertext,
            "plaintext": plaintext,

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

        expected_size = row * col

        if len(ciphertext) != expected_size:
            raise ValueError(
                f"Ciphertext must contain exactly "
                f"{expected_size} characters for a "
                f"{row} × {col} matrix."
            )

        plaintext = cipher.decrypt(
            ciphertext,
            row_key,
            col_key
        )

        return {
            "algorithm": "double_transposition",
            "operation": "decrypt",

            "row": row,
            "col": col,

            "row_key": row_key,
            "column_key": col_key,

            "ciphertext": ciphertext,
            "plaintext": plaintext
        }


    raise ValueError(
        "Invalid Double Transposition operation."
    )