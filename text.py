# function will convert string parameter to upper case
def to_upper(text):
    #Task6 start check if the parameter is a string
    if isinstance(text, str) == False:
        raise TypeError("the parameter should be a string")
    # Task6 end
    return text.upper()


# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list):
    #Task6 start check if the parameter is a list
    if isinstance(str_list, list) == False:
        raise TypeError("the parameter should be a list")
    # Task6 end
    for word in str_list:
        if word.islower():
            return False
    return True

