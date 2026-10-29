def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    

def can_construct(ransomNote: str, magazine: str) -> bool:
    # Create a hash table to track the frequency of each letter.
    letter_counts = {}

    # Count how many times each character appears in the magazine.
    for char in magazine:
        letter_counts[char] = letter_counts.get(char, 0) + 1

    # Check whether the magazine contains enough of each character.
    for char in ransomNote:
        # Return False if the character is missing or has been used up.
        if char not in letter_counts or letter_counts[char] == 0:
            return False

        # Use one occurrence of the character.
        letter_counts[char] -= 1

    # All characters in the ransom note were available.
    return True
