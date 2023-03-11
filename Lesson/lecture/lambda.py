# my_list = [1, 2, 3, 5, 8, 15, 23, 38]
#
# print([(value, value**2) for i, value in enumerate(my_list) if value % 2 == 0])

# ------------------------------------
def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = select(lambda x: (x, x**2), res)
print(res)
