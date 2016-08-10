#!/usr/bin/python3

import random
import timeit
from time import sleep
def data_translation():
    # row.column to column.row
    def test1():
        columns = list(zip(*data))
        return columns

    def test2():
        columns = [[] for _ in data[0]]
        for row in data:
            for i, column in enumerate(row):
                columns[i].append(column)
        return columns

    data = [[random.randint(0,99999) for _ in range(9)] for _ in range(99)]
    repeat, number = 1,10000

    print("test1: ", timeit.repeat(test1, repeat=repeat, number=number))
    print("test2: ", timeit.repeat(test2, repeat=repeat, number=number))


def data_conversion():
    # str to int
    def test1():
        res = list(map(lambda x: list(map(lambda y: int(y), x)), data))
        return res

    def test2():
        res = []
        for row in data:
            new_row = []
            for column in row:
                new_row.append(int(column))
            res.append(new_row)
        return res

    data = [[str(random.randint(0,99999)) for _ in range(9)] for _ in range(99)]
    repeat, number = 1,1000

    print("test1: ", timeit.repeat(test1, repeat=repeat, number=number))
    print("test2: ", timeit.repeat(test2, repeat=repeat, number=number))

data_conversion()