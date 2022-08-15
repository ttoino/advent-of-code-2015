import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    a = inf.readline().strip().split()
    row, column = int(a[-3].removesuffix(",")), int(a[-1].removesuffix("."))

    x = row - 2 + column
    n = x * (x + 1) // 2 + column

    r = 20151125
    i = 1
    while i < n:
        i += 1
        r *= 252533
        r %= 33554393

    outf.write(str(r))
