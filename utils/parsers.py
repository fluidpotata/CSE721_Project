def parse_permutation_key(value):
    if not value:
        raise ValueError("Permutation key cannot be empty.")

    try:
        value = value.replace(",", " ")

        return [
            int(i)
            for i in value.split()
        ]

    except ValueError:
        raise ValueError(
            "Permutation key must contain integers only."
        )