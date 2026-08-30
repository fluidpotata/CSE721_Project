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

def validate_permutation_key(key):
    if not key:
        raise ValueError(
            "Permutation key cannot be empty."
        )

    expected = set(range(len(key)))

    if set(key) != expected:
        raise ValueError(
            f"Permutation key must contain each number "
            f"from 0 to {len(key) - 1} exactly once."
        )