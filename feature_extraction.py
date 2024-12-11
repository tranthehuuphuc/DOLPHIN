# This file computes features based on DOLPHIN patterns

def compute_phonics_features(matches):
    """
    Computes phonics-based features from matched patterns.

    Args:
        matches (list): List of tuples (substring, type).

    Returns:
        dict: Phonics-based features.
    """
    vowels = [item for item in matches if item[1] == "vowel"]
    consonants = [item for item in matches if item[1] == "consonant"]
    total_length = len(matches)

    vowel_ratio = len(vowels) / total_length if total_length > 0 else 0
    repeated_chars = len(set(item[0] for item in matches if matches.count(item) > 1)) / total_length
    consecutive_consonants = sum(1 for i in range(len(consonants) - 1)
                                 if consonants[i][0] + consonants[i + 1][0]) / total_length

    return {
        "vowel_ratio": vowel_ratio,
        "repeated_chars": repeated_chars,
        "consecutive_consonants": consecutive_consonants
    }