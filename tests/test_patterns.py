# Test cases for dolphin_patterns.py

from dolphin_patterns import greedy_match, DOLPHIN_PATTERNS

def test_greedy_match():
    domain = "nationalgeographic"
    matches = greedy_match(domain, DOLPHIN_PATTERNS)
    expected = [
        ('n', 'consonant'), ('a', 'vowel'), ('t', 'consonant'),
        ('ion', 'vowel'), ('al', 'vowel'), ('g', 'consonant'),
        ('e', 'vowel'), ('o', 'vowel'), ('gr', 'consonant'),
        ('a', 'vowel'), ('ph', 'consonant'), ('i', 'vowel'),
        ('c', 'consonant')
    ]
    assert matches == expected