def sum_of_squares(n):
    answer = 0
    for z in range(n+1):
        answer = answer + z**2
    return answer

def filter_out_negative_numbers(n):
    new_list = []
    for number in n:
        if number >= 0:
            new_list.append(number)
    return new_list

if __name__ == "__main__":
    print sum_of_squares(20)
    # print filter_out_negative_numbers([-2,5,10,-100,5])