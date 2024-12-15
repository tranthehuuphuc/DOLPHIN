# feature_extraction.py

from typing import List, Tuple, Dict

def compute_phonics_features(matches: List[Tuple[str, str]]) -> Dict[str, float]:
    """
    Extract phonics-based features from DOLPHIN pattern matching.
    
    Args:
        matches (List[Tuple[str, str]]): List of matched substrings with their types
    
    Returns:
        Dict[str, float]: Extracted phonics features
    """
    # Initialize feature dictionary
    features = {
        'vowel_ratio': 0.0,
        'consonant_ratio': 0.0,
        'neutral_ratio': 0.0,
        'pattern_diversity': 0.0,
        'max_pattern_length': 0.0
    }
    
    # If no matches, return default features
    if not matches:
        return features
    
    # Compute feature calculations
    total_matches = len(matches)
    
    # Compute type ratios
    type_counts = {}
    max_pattern_length = 0
    
    for pattern, pattern_type in matches:
        # Track pattern type counts
        type_counts[pattern_type] = type_counts.get(pattern_type, 0) + 1
        
        # Track max pattern length
        max_pattern_length = max(max_pattern_length, len(pattern))
    
    # Calculate ratios
    features['vowel_ratio'] = type_counts.get('vowel', 0) / total_matches
    features['consonant_ratio'] = type_counts.get('consonant', 0) / total_matches
    features['neutral_ratio'] = type_counts.get('neutral', 0) / total_matches
    
    # Pattern diversity (number of unique pattern types)
    features['pattern_diversity'] = len(set(p for _, p in matches)) / total_matches
    
    # Max pattern length
    features['max_pattern_length'] = max_pattern_length
    
    return features