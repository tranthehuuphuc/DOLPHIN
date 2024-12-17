import math
from typing import List, Tuple, Dict

def compute_phonics_features(matches: List[Tuple[str, str]]) -> Dict[str, float]:
    """
    Extract phonics-based features from DOLPHIN pattern matching.
    """
    features = {
        'vowel_ratio': 0.0,
        'consonant_ratio': 0.0,
        'neutral_ratio': 0.0,
        'pattern_diversity': 0.0,
        'max_pattern_length': 0.0,
        'weighted_vowel_ratio': 0.0,
        'weighted_consonant_ratio': 0.0,
        'normalized_pattern_diversity': 0.0
    }
    
    if not matches:
        return features
    
    total_matches = len(matches)
    total_length = sum(len(pattern) for pattern, _ in matches)
    type_counts = {}
    max_pattern_length = 0

    for pattern, pattern_type in matches:
        type_counts[pattern_type] = type_counts.get(pattern_type, 0) + 1
        max_pattern_length = max(max_pattern_length, len(pattern))
    
    features['vowel_ratio'] = type_counts.get('vowel', 0) / total_matches
    features['consonant_ratio'] = type_counts.get('consonant', 0) / total_matches
    features['neutral_ratio'] = type_counts.get('neutral', 0) / total_matches

    features['weighted_vowel_ratio'] = sum(len(pattern) for pattern, p_type in matches if p_type == 'vowel') / total_length
    features['weighted_consonant_ratio'] = sum(len(pattern) for pattern, p_type in matches if p_type == 'consonant') / total_length

    features['pattern_diversity'] = len(set(p for _, p in matches)) / total_matches
    total_types = len(set(['vowel', 'consonant', 'neutral']))
    features['normalized_pattern_diversity'] = len(set(p for _, p in matches)) / total_types

    features['max_pattern_length'] = max_pattern_length
    
    return features

def compute_structural_features(domain: str) -> Dict[str, float]:
    """
    Extract structural and statistical features from a domain name.
    """
    features = {
        'length': len(domain),
        'subdomain_count': domain.count('.'),
        'entropy': 0.0
    }
    # Calculate Shannon entropy
    probabilities = [domain.count(c) / len(domain) for c in set(domain)]
    features['entropy'] = -sum(p * math.log2(p) for p in probabilities)
    
    return features

def extract_all_features(domain: str, matches: List[Tuple[str, str]]) -> Dict[str, float]:
    """
    Extract all features (phonics-based, structural, and statistical) for a domain.
    """
    features = {}
    # Add structural and statistical features
    features.update(compute_structural_features(domain))
    # Add phonics-based features
    features.update(compute_phonics_features(matches))
    
    return features
