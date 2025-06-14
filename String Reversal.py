def reverse_string(input_str):
    """
    Reverses the input string and returns the result.
    
    Args:
        input_str (str): The string to be reversed
        
    Returns:
        str: The reversed string
    """
    return input_str[::-1]

# Test the function
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("Aditya"))  # Output: "aytidA"
print(reverse_string("Mhetre"))  # Output: "ertehM"