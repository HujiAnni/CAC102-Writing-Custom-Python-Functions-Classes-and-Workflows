def add(x,y):
    """
    Returns the sum of inputs x and y
    """
    result = x + y
    return result

def add2(x,y):
    """
    Returns the sum of inputs x and y if they can be added,
    and otherwise returns None and prints the statement:
    "Those two inputs cannot be added to each other."
    """
    try:
        result = x + y
        return result
    except TypeError:
        print("Those two inputs cannot be added to each other")
        return None
    


