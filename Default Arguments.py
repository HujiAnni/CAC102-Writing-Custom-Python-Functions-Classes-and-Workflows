myname = 'My' + ' ' + 'Name'

def add_two_strings_with_separator(first, second, separator):
    yourname=first+separator+second
    return yourname

yourname=add_two_strings_with_separator("Your","Name"," ")
print(yourname)

def add_two_strings(first, second, separator=" "):
    yourname=first+separator+second
    return yourname

hername=add_two_strings("Her","Name")
her_name=add_two_strings("Her","Name","_")
print(hername)
print(her_name)

result1=add_two_strings(first='My',second='Name')
result2=add_two_strings(second='My',first='Name')
print(result1)
print(result2)
