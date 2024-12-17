import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.dolphin_patterns import greedy_match, DOLPHIN_PATTERNS

def test_greedy_match():
    # Test case: Single domain name
    test_domain = "secureupdate.com"
    expected_output = [
        ('s', 'consonant'),
        ('e', 'vowel'),
        ('c', 'consonant'),
        ('ure', 'vowel'),
        ('u', 'vowel'),
        ('p', 'consonant'),
        ('d', 'consonant'),
        ('a', 'vowel'),
        ('t', 'consonant'),
        ('e', 'vowel'),
        ('.', 'neutral'),
        ('c', 'consonant'),
        ('o', 'vowel'),
        ('m', 'consonant')
    ]


    # Run the greedy match function
    matches = greedy_match(test_domain, DOLPHIN_PATTERNS)

    # Assert the result matches the expected output
    assert matches == expected_output, f"Expected {expected_output}, got {matches}"
