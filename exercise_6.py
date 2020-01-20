from itertools import count, cycle


def count_to(start, stop):

    my_list = []

    for i in count(start):
        if i > stop:
            return my_list
            break
        else:
            my_list.append(i)


i = count_to(5, 25)

print(i)


def print_cycle(some_list):

    cycle_i = cycle(some_list)
    c = 0

    while c < len(i):

        print(next(cycle_i))

        c += 1


print_cycle(i)