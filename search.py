t = (5,(1,2),((1),(9)))
def max_val(t):
    max = -100
    for item in t:
        if type(item) == int:
            if item > max:
                max = item
        elif type(item) == tuple or type(item) == list:
            if max_val(item) > max:
                max = max_val(item)
    return max
print(max_val(t))
