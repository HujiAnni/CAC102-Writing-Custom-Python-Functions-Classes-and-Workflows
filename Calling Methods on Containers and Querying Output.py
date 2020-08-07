
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dict2 = {'c': 10, 'd': 20, 'e': 30, 'f': 40, 'g': 50}

set_A={i for i in dict1.keys()}
set_B={j for j in dict2.keys()}
shared_keys=set_A.intersection(set_B)

set_C={i for i in dict1.values()}
set_D={j for j in dict2.values()}
shared_values=set_C.intersection(set_D)
