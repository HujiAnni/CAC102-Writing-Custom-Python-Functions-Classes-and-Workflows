my_list = [1, 3, 14, 22, 29, 43, 89, 102, 256]

def extract_even_numbers_in_list(alist):
    """
    Returns a list of the numbers in the input alist
    that are even numbers

    NOTE: n%2 == 0 if n is even,  n%2 == 1 if n is odd
    """
    result = []
    for elem in alist:
        if elem%2 == 0:
            result.append(elem)
    return result


def extract_digits_from_string(s):
    """
    Returns a list of all the digits that appear in a string,
    in the order in which they are encountered.
    """
    result = []
    for c in s:
        if c.isdigit():
            result.append(c)
    return result


def make_dict_of_squares(n):
    """
    Returns a dictionary that maps from integers to their squares, 
    starting with 0 and ending at one less than the input n
    """
    result = {}
    for i in range(n):
        result[i] = i*i
    return result
    
my_evens = extract_even_numbers_in_list(my_list)

s = 'The answer is 42, but many people guess 12.'
str_digits = extract_digits_from_string(s)

squares = make_dict_of_squares(10)

my_evens2=[elem for elem in my_list if  elem%2 == 0]
str_digits2=[c for c in s if c.isdigit()]

squares2={i:i*i for i in range(10)}
