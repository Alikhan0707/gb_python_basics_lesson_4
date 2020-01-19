some_list = [49, 20, 74, 3, 1, 5, 8, 17, 21, 18, 9, 4, 33, 45]

my_list = [i for i in some_list if some_list.index(i) > 0 if i - (some_list[some_list.index(i) - 1]) > 0]

print(my_list)