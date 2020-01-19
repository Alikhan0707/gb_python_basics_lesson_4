some_list = [1, 2, 2, 2, 54, 4, 3, 6, 5, 5, 5, 7, 10]

my_list = [i for i in some_list if i not in some_list[:some_list.index(i)] and i not in some_list[some_list.index(i) + 1:]]

print(my_list)