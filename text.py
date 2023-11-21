# function will convert string parameter to upper case
def to_upper(string):
    if isinstance(string, str):
        return string.upper()
    else:
        raise TypeError('You should write a string') # TASK 6

# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list):
    if isinstance(str_list, list):
        for word in str_list:
            if word.islower():
                return False
        return True
    else:
        raise TypeError ('You should put a list with strings') # TASK 6
    

# print(to_upper('tr'))
# print(to_word_list_isupper(['LS', 'SA']))