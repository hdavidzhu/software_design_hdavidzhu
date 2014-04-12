def reverse_lookup(d, v):
    all_keys = []
    for k in d:
        if d[k] == v:
            all_keys.append(k)
    return all_keys
    raise ValueError

known = {0:0, 1:1}
edit_distance = {}

def fibonacci(n):
    if n in known:
        return known[n]
    
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

def levenshtein_distance(s1,s2):
    """ Computes the Levenshtein distance between two input strings """
    if (s1,s2) in edit_distance:
        return edit_distance[(s1,s2)]
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    
    edit_distance[(s1,s2)] = min([int(s1[0] != s2[0]) + levenshtein_distance(s1[1:],s2[1:]), 1+levenshtein_distance(s1[1:],s2), 1+levenshtein_distance(s1,s2[1:])])
    return edit_distance[(s1,s2)]

if __name__ == '__main__':
    # print fibonacci(100)
    print levenshtein_distance('helsdajldkja;ldfkj;laskdjfl;kasjdf;lkjlo','gajdslkja;ldja;lkdjoodbye')