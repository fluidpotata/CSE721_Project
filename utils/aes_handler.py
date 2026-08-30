from symmetric.aes import AES


def handle_aes(data):
    operation = data.get("operation")

    cipher = AES()

    if operation == "encrypt":
        plaintext = data.get("plaintext", "")

        if not plaintext:
            raise ValueError("Plaintext cannot be empty.")

        ciphertext = cipher.encrypt(plaintext)

        key = cipher.key.hex()

        round_keys = [
            round_key.hex()
            for round_key in cipher.round_keys
        ]

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

        try:
            cipher.key = bytes.fromhex(key)
        except ValueError:
            raise ValueError("AES key must be valid hexadecimal.")

        if len(cipher.key) != 16:
            raise ValueError(
                "AES-128 key must be exactly 16 bytes."
            )

        cipher.key_expansion()

        plaintext = cipher.decrypt(ciphertext)

        return {
            "algorithm": "aes",
            "operation": "decrypt",
            "plaintext": plaintext
        }

    raise ValueError("Invalid AES operation.")