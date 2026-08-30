def validate_substitution_key(key):

    if len(key) != 26:
        raise ValueError(
            "Substitution key must contain exactly 26 letters."
        )

    if not key.isalpha():
        raise ValueError(
            "Substitution key must contain letters only."
        )

    if len(set(key)) != 26:
        raise ValueError(
            "Each letter in the key must be unique."
        )