"""
Write a function that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i+1 elements from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6]. 
"""
def cumusum(numbers):
    total = 0
    for i in range(len(numbers)-1):
        cumulative[i+1] = numbers[i+1] + numbers[i]
    return cumulative

"""
Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.
"""
def has_duplicates(n):
    counter = 0
    while n[0] != n[counter]:
        counter = counter + 1
        if counter == len(n) - 1:
            break

if __name__ == "__main__":
    # print cumusum([2,3,4])