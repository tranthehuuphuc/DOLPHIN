# dolphin_patterns.py

from typing import List, Dict, Tuple, Set

# DOLPHIN patterns definition (exactly as in the paper)
DOLPHIN_PATTERNS = {
    "vowels": {
        1: ["a", "e", "i", "o", "u"],
        2: ["ai", "al", "ar", "au", "aw", "ay", "ea", "ee", "ei", 
            "er", "eu", "ew", "ey", "ia", "ie", "ir", "oa", "oe", 
            "oi", "oo", "or", "ou", "ow", "oy", "ue", "ui", "ur"],
        3: ["air", "ear", "eer", "igh", "ign", "ing", "ion", "oew", "ore", "our", "ure"]
    },
    "consonants": {
        1: ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", 
            "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"],
        2: ["bl", "br", "ch", "ck", "cl", "cr", "dr", "fl", "fr", "gh", "gl", "gr", 
            "kn", "ld", "lk", "mb", "mn", "mp", "nd", "ng", "nk", "nt", "ph", "pl", 
            "pn", "pr", "ps", "qe", "qu", "rh", "sc", "sh", "sk", "sl", "sm", "sn", 
            "sp", "st", "sw", "th", "tr", "wh", "wr"],
        3: ["dge", "gue", "nch", "que", "shr", "spl", "spr", "squ", "str", "tch", "thr"]
    }
}

def greedy_match(domain_name: str, patterns: Dict) -> List[Tuple[str, str]]:
    """
    Implement greedy matching algorithm for DOLPHIN patterns.
    
    Args:
        domain_name (str): Domain name to process
        patterns (Dict): Dictionary of DOLPHIN patterns
    
    Returns:
        List of tuples with matched substrings and their types
    """
    matcher = DolphinMatcher(patterns)
    return matcher.construct_output_function(domain_name)

class DolphinMatcher:
    def __init__(self, patterns: Dict):
        """
        Initialize the Dolphin Matcher with predefined patterns.
        
        Args:
            patterns (Dict): Dictionary of DOLPHIN patterns for vowels and consonants
        """
        self.patterns = patterns
        self.max_pattern_length = max(
            len(pattern) 
            for pattern_type in patterns.values() 
            for length_group in pattern_type.values() 
            for pattern in length_group
        )
        
        # Precompute all possible patterns for faster lookup
        self.all_patterns = set()
        for pattern_type in patterns.values():
            for length_group in pattern_type.values():
                self.all_patterns.update(length_group)
    
    def _is_valid_pattern(self, substring: str) -> bool:
        """
        Check if the substring is a valid DOLPHIN pattern.
        
        Args:
            substring (str): Substring to check
        
        Returns:
            bool: True if substring is a valid pattern, False otherwise
        """
        return substring in self.all_patterns
    
    def _get_pattern_type(self, substring: str) -> str:
        """
        Determine the type of pattern (vowel, consonant, or None)
        
        Args:
            substring (str): Substring to check
        
        Returns:
            str: Type of pattern ('vowel', 'consonant', or None)
        """
        for pattern_type, type_patterns in self.patterns.items():
            for length_group in type_patterns.values():
                if substring in length_group:
                    return pattern_type[:-1]  # Remove 's' from 'vowels'/'consonants'
        return None
    
    def construct_output_function(self, domain_name: str) -> List[Tuple[str, str]]:
        """
        Reconstruct the output function as described in Algorithm 1 of the paper.
        Implements a greedy matching approach with state-based output.
        
        Args:
            domain_name (str): Domain name to process
        
        Returns:
            List of tuples with matched substrings and their types
        """
        output = []
        i = 0
        length = len(domain_name)
        
        while i < length:
            # Try greedy matching from longest to shortest patterns
            match_found = False
            for pattern_length in range(min(self.max_pattern_length, length - i), 0, -1):
                substring = domain_name[i:i + pattern_length]
                
                if self._is_valid_pattern(substring):
                    pattern_type = self._get_pattern_type(substring)
                    output.append((substring, pattern_type))
                    i += pattern_length
                    match_found = True
                    break
            
            # If no pattern match, add individual character
            if not match_found:
                output.append((domain_name[i], 'neutral'))
                i += 1
        
        return output
    
    def matching_function(self, domain_name: str) -> List[Tuple[str, str]]:
        """
        Implements the matching function as described in Algorithm 2 of the paper.
        
        Args:
            domain_name (str): Domain name to process
        
        Returns:
            List of tuples with matched substrings and their types
        """
        # This method can be expanded to more closely match the paper's state machine
        # For now, it leverages the construct_output_function
        return self.construct_output_function(domain_name)