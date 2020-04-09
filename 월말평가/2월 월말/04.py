def q4(word): 
    check = ['s', 'a', 'f', 'y']
    for w in word:
        if w in check:
            return True
    else:
        return False
print(q4('fish')) 
print(q4('united')) 
print(q4('galaxy'))
