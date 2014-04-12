def factorial(n):
    if n==0:
        return 1
    return factorial(n-1)*n

def fib(n):
    if n==0 or n==1:
        return 1
    return fib(n-1) + fib(n-2)

def is_palindrome(string):
    length = len(string)
    if length == 0 or length == 1:
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:length-1])
    else:
        return False

if __name__ == "__main__":
    # print factorial(998)
    # print fib(6)
    print is_palindrome("asdadasd")