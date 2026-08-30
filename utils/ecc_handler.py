from asymmetric.ecc import ECC


def handle_ecc(data):
    operation = data.get("operation")

    try:
        p = int(data.get("p"))
        a = int(data.get("a"))
        b = int(data.get("b"))
        n = int(data.get("n"))

        gx = int(data.get("gx"))
        gy = int(data.get("gy"))

    except (TypeError, ValueError):
        raise ValueError(
            "ECC domain parameters must be integers."
        )

    G = (gx, gy)

    ecc = ECC(
        p=p,
        a=a,
        b=b,
        G=G,
        n=n
    )

    if operation == "generate":

        multiples = ecc.list_multiples()

        private_key, public_key = (
            ecc.generate_keys()
        )

        return {
            "algorithm": "ecc",
            "operation": "generate",

            "domain": {
                "p": p,
                "a": a,
                "b": b,
                "G": G,
                "n": n
            },

            "multiples": multiples,

            "private_key": private_key,
            "public_key": public_key
        }

    elif operation == "ecdh":

        try:
            alice_private = int(
                data.get("alice_private")
            )

            bob_private = int(
                data.get("bob_private")
            )

        except (TypeError, ValueError):
            raise ValueError(
                "ECDH private keys must be integers."
            )

        if not 1 <= alice_private < n:
            raise ValueError(
                f"Alice's private key must be between 1 and {n - 1}."
            )

        if not 1 <= bob_private < n:
            raise ValueError(
                f"Bob's private key must be between 1 and {n - 1}."
            )

        result = ecc.ecdh(
            alice_private,
            bob_private
        )

        return {
            "algorithm": "ecc",
            "operation": "ecdh",

            "alice_private": result["alice_private"],
            "alice_public": result["alice_public"],

            "bob_private": result["bob_private"],
            "bob_public": result["bob_public"],

            "shared_key": result["shared_key"]
        }


    raise ValueError(
        "Invalid ECC operation."
    )