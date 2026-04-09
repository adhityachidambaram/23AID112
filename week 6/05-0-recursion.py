

def sum(list):    
    first = list[0]
    rest = list[1:]
    print(f"first = {first}, rest = {rest}, len(rest) = {len(rest)}")
    if len(rest) > 0:
        print(f"returning '{first}' + sum({rest})")
        return first + sum(rest)
    else:
        print(f"returning '{first}'")
        return first
    
print(sum([5,3,9,7,2]))