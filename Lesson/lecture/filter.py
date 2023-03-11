# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# --------------------------------------------

# def select(f, col):                     # map заменяет эту функцию
#     return [f(x) for x in col]


# def where(f, col):                        # filter заменяет эту функцию
#     return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]

res = map(int, data)                                       # функция select
res = filter(lambda x: x % 2 == 0, res)                  # функция where
res = list(map(lambda x: (x, x ** 2), res))             # функция select
print(res)
