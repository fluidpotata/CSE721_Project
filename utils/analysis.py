from collections import Counter


def frequency_analysis(text):

    letters = [ch.upper() for ch in text if ch.isalpha()]

    total = len(letters)

    if total == 0:
        return []

    counts = Counter(letters)

    result = []

    for letter, count in counts.most_common():

        result.append({
            "letter": letter,
            "count": count,
            "percentage": round(
                count / total * 100,
                2
            )
        })

    return result