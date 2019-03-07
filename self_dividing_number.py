def number_to_list(num):
    list_of_number = list(str(num))
    dividable_numbers = []
    for number in list_of_number:
        number = int(number)
        dividable_numbers.append(number)
    return dividable_numbers


def self_divide_checker(num):
    counter = 0
    for element in number_to_list(num):
        if element == 0:
            return None
        elif num % element == 0:
            counter += 1
    if counter == len(number_to_list(num)):
        return num



def self_dividing_number(left, right):
    pre_filter = []
    answer = []
    for number in range(left, (right+1)):
        pre_filter.append(self_divide_checker(number))
    for element in pre_filter:
        if isinstance(element, int):
            answer.append(element)
    print(answer)

self_dividing_number(1, 22)

