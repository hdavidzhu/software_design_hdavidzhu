from numpy import linspace

def get_complementary_base(n):
    """
    Returns the complementary base pair for any input nucleotide.
    """
    n  = n.upper()
    if n == 'A':
        return 'T'
    elif n == 'T':
        return 'A'
    elif n == 'C':
        return 'G'
    elif n == 'G':
        return 'C'
    else:
        raise Exception("Please insert an actual nucleotide.") 

# def is_between(x, y, z):

# def random_float(start, stop):