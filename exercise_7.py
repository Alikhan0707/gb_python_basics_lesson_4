from math import factorial

my_list = [i for i in range(20)]


def fibo_gen(some_list):

    for i in some_list:
        yield factorial(i)


for el in fibo_gen(my_list[:16]):

    print(el)