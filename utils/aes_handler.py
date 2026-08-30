from symmetric.aes import AES


def handle_aes(data):
    operation = data.get("operation")

    cipher = AES()

    if operation == "encrypt":
        plaintext = data.get("plaintext", "")

        if not plaintext:
            raise ValueError("Plaintext cannot be empty.")

        ciphertext, key, round_keys = cipher.encrypt(
            plaintext
        )

        return {
            "algorithm": "aes",
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
            raise ValueError("AES key cannot be empty.")

        plaintext = cipher.decrypt(
            ciphertext,
            key
        )

        return {
            "algorithm": "aes",
            "operation": "decrypt",
            "plaintext": plaintext
        }

    raise ValueError("Invalid AES operation.")