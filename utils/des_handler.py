from symmetric.des import DES


def handle_des(data):
    operation = data.get("operation")

    cipher = DES()

    if operation == "encrypt":
        plaintext = data.get("plaintext", "")

        if not plaintext:
            raise ValueError("Plaintext cannot be empty.")

        ciphertext, key, round_keys = cipher.encrypt(plaintext)

        return {
            "algorithm": "des",
            "operation": "encrypt",
            "ciphertext": ciphertext,
            "key": key,
            "round_keys": round_keys
        }

    elif operation == "decrypt":
        ciphertext = data.get("ciphertext", "")
        key = data.get("key", "")

        if not ciphertext:
            raise ValueError("Ciphertext cannot be empty.")

        if not key:
            raise ValueError("DES key cannot be empty.")

        plaintext = cipher.decrypt(
            ciphertext,
            key
        )

        return {
            "algorithm": "des",
            "operation": "decrypt",
            "plaintext": plaintext
        }

    else:
        raise ValueError("Invalid DES operation.")