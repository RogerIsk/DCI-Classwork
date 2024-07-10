import pytest
from classwork_4 import process_text

def test_palindrome():
    text = "madam"
    reversed_text, is_palindrome = process_text(text)
    assert reversed_text == "madam"
    assert is_palindrome is True

def test_not_palindrome():
    text = "hello"
    reversed_text, is_palindrome = process_text(text)
    assert reversed_text == "olleh"
    assert is_palindrome is False

def test_empty_string():
    text = ""
    reversed_text, is_palindrome = process_text(text)
    assert reversed_text == ""
    assert is_palindrome is True

def test_single_character():
    text = "a"
    reversed_text, is_palindrome = process_text(text)
    assert reversed_text == "a"
    assert is_palindrome is True

def test_palindrome_with_spaces():
    text = "a man a plan a canal panama"
    reversed_text, is_palindrome = process_text(text.replace(" ", ""))
    assert reversed_text == "amanaplanacanalpanama"
    assert is_palindrome is True

def test_palindrome_with_mixed_case():
    text = "Aba"
    reversed_text, is_palindrome = process_text(text.lower())
    assert reversed_text == "aba"
    assert is_palindrome is True