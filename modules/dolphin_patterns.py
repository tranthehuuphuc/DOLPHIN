from typing import List, Dict, Tuple

# Updated DOLPHIN patterns
DOLPHIN_PATTERNS = {
    "vowels": {
        1: ["a", "e", "i", "o", "u"],
        2: ["ai", "al", "ar", "au", "aw", "ay", "ea", "ee", "ei",
            "er", "eu", "ew", "ey", "ia", "ie", "ir", "oa", "oe",
            "oi", "oo", "or", "ou", "ow", "oy", "ue", "ui", "ur"],
        3: ["air", "ear", "eer", "igh", "ign", "ing", 
            "ion", "oew", "ore", "our", "ure"]
    },
    "consonants": {
        1: ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
            "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"],
        2: ["bl", "br", "ch", "ck", "cl", "cr", "dr", "fl", "fr", 
            "gh", "gl", "gr", "kn", "ld", "lk", "mb", "mn", "mp", 
            "nd", "ng", "nk", "nt", "ph", "pl", "pn", "pr", "ps", 
            "qe", "qu", "rh", "sc", "sh", "sk", "sl", "sm", "sn", 
            "sp", "st", "sw", "th", "tr", "wh", "wr"],
        3: ["dge", "gue", "nch", "que", "shr", "spl", "spr", "squ", 
            "str", "tch", "thr"]
    }
}

class DolphinMatcher:
    def __init__(self, patterns: Dict):
        """
        Initialize the Dolphin Matcher with predefined patterns.
        """
        self.patterns = patterns
        self.max_pattern_length = max(
            len(pattern) 
            for pattern_type in patterns.values() 
            for length_group in pattern_type.values() 
            for pattern in length_group
        )
        # Precompute all valid patterns for fast lookup
        self.all_patterns = set()
        for pattern_type in patterns.values():
            for length_group in pattern_type.values():
                self.all_patterns.update(length_group)
    
    def _get_pattern_type(self, substring: str) -> str:
        """
        Determine the type of pattern (vowel, consonant, or neutral).
        """
        for pattern_type, type_patterns in self.patterns.items():
            for length_group in type_patterns.values():
                if substring in length_group:
                    return pattern_type[:-1]  # Remove 's' from 'vowels'/'consonants'
        return 'neutral'
    
    def construct_output_function(self, domain_name: str) -> List[Tuple[str, str]]:
        """
        Implements Algorithm 1: Construct the output function.
        """
        output = []
        current_state = "neutral"
        i = 0
        length = len(domain_name)
        
        while i < length:
            match_found = False
            for pattern_length in range(min(self.max_pattern_length, length - i), 0, -1):
                substring = domain_name[i:i + pattern_length]
                if substring in self.all_patterns:
                    pattern_type = self._get_pattern_type(substring)
                    
                    # Transition state logic (Algorithm 1)
                    if current_state == "neutral":
                        current_state = pattern_type
                    elif current_state != pattern_type:
                        current_state = "neutral"
                    
                    output.append((substring, pattern_type))
                    i += pattern_length
                    match_found = True
                    break
            
            # If no match found, process the single character
            if not match_found:
                output.append((domain_name[i], "neutral"))
                current_state = "neutral"
                i += 1
        
        return output

    def matching_function(self, domain_name: str) -> List[Tuple[str, str]]:
        """
        Implements state-based pattern matching with transitions.
        """
        output = []
        current_state = None
        i = 0
        length = len(domain_name)
        
        while i < length:
            match_found = False
            for pattern_length in range(self.max_pattern_length, 0, -1):
                if i + pattern_length > length:
                    continue
                substring = domain_name[i:i + pattern_length]
                pattern_type = self._get_pattern_type(substring)
                
                if pattern_type != "neutral":
                    if current_state != pattern_type:
                        current_state = pattern_type
                    output.append((substring, current_state))
                    i += pattern_length
                    match_found = True
                    break
            
            if not match_found:
                output.append((domain_name[i], "neutral"))
                i += 1
        
        return output
