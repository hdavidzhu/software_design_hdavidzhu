import sets

def exclusive_or_dict(d1,d2):
    d3 = {}
    for key in d1:
        if key not in d2:
            d3[key] = d1[key]
    for key in d2:
        if key not in d1:
            d3[key] = d2[key]
    return d3

if __name__ == '__main__':
    # d1 = {'a':5,'b':3}
    # d2 = {'a':7,'c':3}
    d1 = {'test':5,'b':7.0,3:'q'}
    d2 = {'b':'world',3:'q'}
    print exclusive_or_dict(d1,d2)