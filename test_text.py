import pytest
from text import to_upper, to_word_list_isupper

def test_upper1():
    assert to_upper('abcdef') == 'ABCDEF', 'to_upper function does not return expected value'

def test_word_list_isupper1():
    assert to_word_list_isupper(['I', 'LOVE', 'PYTHON']), 'to_word_list_isupper should return True'

def test_word_list_isupper2():
    assert not to_word_list_isupper(['i', 'LOVE', 'PYTHON']), 'to_word_list_isupper should return False'

def test_upper3():
    with pytest.raises(TypeError):
        to_upper(523)

def test_word_list_isupper3():
    with pytest.raises(TypeError):
        to_word_list_isupper("I LOVE YOU")