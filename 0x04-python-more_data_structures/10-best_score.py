#!/usr/bin/python3
def best_score(a_dictionary):
    """Return key with biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)
    
    temp_key = list(a_dictionary.keys())[0]
    temp_value = a_dictionary[temp_key]
    for key, value in a_dictionary.items():
        if value > temp_value:
            temp_key = key
            temp_value = value
    return (temp_key)
