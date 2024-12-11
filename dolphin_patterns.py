## dolphin_patterns.py
# This file defines DOLPHIN patterns and implements the greedy matching algorithm

# DOLPHIN patterns definition
DOLPHIN_PATTERNS = {
    "vowels": {
        1: ["a", "e", "i", "o", "u"],
        2: ["ai", "al", "ar", "au", "aw", "ay", "ea", "ee", "ei", "er", "eu", "ew", "ey", "ia", "ie", "ir", "oa", "oe", "oi", "oo", "or", "ou", "ow", "oy", "ue", "ui", "ur"],
        3: ["air", "ear", "eer", "igh", "ign", "ing", "ion", "oew", "ore", "our", "ure"]
    },
    "consonants": {
        1: ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"],
        2: ["bl", "br", "ch", "ck", "cl", "cr", "dr", "fl", "fr", "gh", "gl", "gr", "kn", "ld", "lk", "mb", "mn", "mp", "nd", "ng", "nk", "nt", "ph", "pl", "pn", "pr", "ps", "qe", "qu", "rh", "sc", "sh", "sk", "sl", "sm", "sn", "sp", "st", "sw", "th", "tr", "wh", "wr"],
        3: ["dge", "gue", "nch", "que", "shr", "spl", "spr", "squ", "str", "tch", "thr"]
    }
}

def greedy_match(domain_name, patterns):
    """
    Splits a domain name into DOLPHIN patterns using a greedy matching algorithm.

    Args:
        domain_name (str): The domain name to process.
        patterns (dict): The DOLPHIN patterns for vowels and consonants.

    Returns:
        list: A list of tuples (matched substring, its type).
    """
    i = 0  # Start index
    length = len(domain_name)
    result = []

    while i < length:
        match_found = False

        # Try to match trigraphs, digraphs, and single characters in order
        for size in [3, 2, 1]:
            if i + size > length:
                continue

            substring = domain_name[i:i + size]

            # Check for vowels
            if substring in patterns["vowels"].get(size, []):
                result.append((substring, "vowel"))
                i += size
                match_found = True
                break

            # Check for consonants
            elif substring in patterns["consonants"].get(size, []):
                result.append((substring, "consonant"))
                i += size
                match_found = True
                break

        # Handle unmatched characters (neutral)
        if not match_found:
            result.append((domain_name[i], "neutral"))
            i += 1

    return result