letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
cipher = {letters[i]: letters[(i-3) % len(letters)] for i in range(len(letters))}
decoder={v:k for k,v in cipher.items()}

def transform_message(message, cipher):
    tmsg = ''
    for c in message:
        if cipher.get(c)!=None:
            tmsg = tmsg + str(cipher.get(c))
        else:
            tmsg = tmsg +c
    return tmsg

test = "I come to bury Caesar, not to praise him."
ttest=transform_message(test,cipher)

