from asymmetric.rsa import RSA


def handle_rsa(data):
    operation = data.get("operation")

    if operation == "generate_keys":
        key_size = int(data.get("key_size", 512))

        if key_size not in (512, 1024):
            raise ValueError(
                "RSA key size must be 512 or 1024 bits."
            )

        rsa = RSA(key_size=key_size)

        public_key, private_key = rsa.generate_keys()

        e, n = public_key
        d, _ = private_key

        return {
            "algorithm": "rsa",
            "operation": "generate_keys",
            "key_size": key_size,

            "public_key": {
                "e": str(e),
                "n": str(n)
            },

            "private_key": {
                "d": str(d),
                "n": str(n)
            }
        }


    elif operation == "encrypt":
        plaintext = data.get("plaintext", "")

        if not plaintext:
            raise ValueError(
                "Plaintext cannot be empty."
            )

        try:
            e = int(data.get("e"))
            n = int(data.get("n"))

        except (TypeError, ValueError):
            raise ValueError(
                "Invalid RSA public key."
            )

        rsa = RSA()

        ciphertext = rsa.encrypt(
            plaintext,
            public_key=(e, n)
        )

        return {
            "algorithm": "rsa",
            "operation": "encrypt",
            "plaintext": plaintext,
            "ciphertext": str(ciphertext)
        }

    elif operation == "decrypt":

        try:
            ciphertext = int(
                data.get("ciphertext")
            )

            d = int(data.get("d"))
            n = int(data.get("n"))

        except (TypeError, ValueError):
            raise ValueError(
                "Invalid RSA ciphertext or private key."
            )

        rsa = RSA()

        plaintext = rsa.decrypt(
            ciphertext,
            private_key=(d, n)
        )

        return {
            "algorithm": "rsa",
            "operation": "decrypt",
            "plaintext": plaintext
        }


    raise ValueError("Invalid RSA operation.")