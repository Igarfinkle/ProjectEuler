def prob36():
    a=0
    for x in range(1,1000001):
        if palindrome(digitlist(x)) and palindrome(binary(x)):
            a+=x
    return a

