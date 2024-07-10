def process_text(text):
    """Reverses the given text and checks if it is a palindrome."""
    reversed_text = text[::-1]
    is_palindrome = (text == reversed_text)
    return reversed_text, is_palindrome