stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def total_price(x, y):
    return sum([[q[1] for q in x.items()][i] * [p[1] for p in y.items()][i] for i in range(len(stock)])


print(total_price(stock, prices))
# I'm sorry it was a challenge



