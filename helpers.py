# File containing all the helper functions for main.py file, for better code readability

import re
from config import DEBUG, RESULT_REGEX

def get_total_results(full_text:str) -> any:
    """
    Extracts the total number of results from a given `full_text` string.

    Args:
        full_text (str): The input string to search for the pattern.

    Returns:
        str or None: The total number of results if found, None otherwise.
    """
    
    # Search for the pattern in the full_text string
    match = re.search(RESULT_REGEX, full_text)

    if match:
        # Extract the number from the match group
        number = match.group(1)
        return number
    else:
        return None

def debug(text:str) -> None:
    """
    Print the given `text` to the console if DEBUG==True

    Args:
        text (str): The text to print.
    """
    if DEBUG:
        print(text)