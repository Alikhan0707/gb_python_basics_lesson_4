from functools import reduce

my_list = [i for i in range(10, 1001) if i % 2 == 0]


def mult_elem(el1, el2):

    return el1 * el2


print(reduce(mult_elem, my_list))