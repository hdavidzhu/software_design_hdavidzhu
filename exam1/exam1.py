def sum_squares_even(n):
    """
    inputs: integer n.
    returns: sum of the squares of allnon-negative enven integers less than or equal to n.
    """
    n = n - n%2
    ans = 0
    for  even in range(0,n+2,2):
        ans = ans + even**2
    return ans
# print sum_squares_even(5)

def pair_list_to_dictionary(l):
    """
    inputs: list.
    returns: dictionary where each consecutive pair of elements in input list is inserted into output dictionary as a key-value pair with first element in the pair being the key and the second being the value.
    """
    d = {}
    if len(l) % 2 == 1:
        del l[-1]
    for index in range(0,len(l),2):
        d[l[index]] = l[index+1] 
    return d
# print pair_list_to_dictionary([1,'a',5])
# print pair_list_to_dictionary(['hello','a','test','b','poop'])

def split_dictionary(d):
    """
    inputs: dictionary of string keys.
    returns: list of dictionaries such that first dictionary in the list contains all key-value pairs from the input dictionary whose keys start with an uppercase letter and second dictionary in the list contains all key-value pairs from the input dictionary whose keys start with a lower case letter.
    """
    uppercase = {}
    lowercase = {}
    for key in d:
        if key[0].isupper() == True:
            uppercase[key] = d[key]
        else:
            lowercase[key] = d[key]
    return [uppercase, lowercase]
# print split_dictionary({'a':2,'B':'hello','c':'t','Dog':'goodbye'})

def in_language(s):
    """
    inputs: string.
    returns: True if and only if the string begins with a sequence of zero or more 'a's, ends with an equal number of 'b's, and contain no other characters.
    """
    a_count, b_count = 0, 0

    for char in s:
        if char == 'a':
            a_count += 1
        else: break
    for char in s[::-1]:
        if char == 'b':
            b_count += 1
        else: break

    if a_count + b_count < len(s):
        return False
    else: 
        return a_count == b_count

# print in_language('aaab')
# print in_language('aaaccc')
# print in_language('')
# print in_language('aaaabbbb')
# print in_language('aaaacabadjlaksjflksajdfcbbbb')

class DNASequence:
    """Represents a sequence of DNA"""
    def __init__(self, nucleotides):
        """constructs a DNASequence with the specified nucleotides.
        nucleotides: the nucleotides represented as a string of capital letters in {'A', 'C', 'G', 'T'}"""
        self.nucleotides = nucleotides

    def get_reverse_compliment(self):
        """Computes the reverse complement of the DNA sequence.
        returns: the reverse complement DNA sequence represented as an object of type DNASequence"""
        self.nucleotides = self.nucleotides[::-1]
        # print type(DNASequence)
        # print type(self.reverse_nucleotides)
        # print type(self.nucleotides)
        return self.nucleotides
        

    def get_proportion_ACGT(self):
        """Computes the proportion of nucleotides in the DNA sequence that are 'A','C','G', and 'T'
        returns: a dictionary where each key is a nucleotide and the corresponding value is the proportion of nucleotides in the DNA sequence that are that nucleotide"""
        d = {}
        nuc_type = ['A','C','G','T']
        for nuc in nuc_type:
            d[nuc] = self.nucleotides.count(nuc)/float(len(self.nucleotides))
        return d

# DNA = DNASequence('ATCGATCGATCGATCGATCGATCG')
# DNA2 = DNASequence('ATCCATCCATCCATCCATCCATCCATCCATCCATCC')
# print DNA.get_reverse_compliment()
# print DNA2.get_reverse_compliment()
# print DNA.nucleotides
# print DNA.get_proportion_ACGT()
# print DNA2.get_proportion_ACGT()