from aoc_2021.d06_Lanternfish.d06_Lanternfish_2 import load_input, iterate
from collections import Counter

def test_load_input():
    assert load_input("aoc_2021/d06_Lanternfish/inputs/test_input.txt") == Counter({1: 1, 2: 1, 3: 2, 4:1})

def test_iterate():
    lanternfish = load_input("aoc_2021/d06_Lanternfish/inputs/test_input.txt")
    lanternfish = iterate(lanternfish)
    assert lanternfish == Counter({0: 1, 1: 1, 2: 2, 3: 1, 4:0, 6:0, 8:0})
    lanternfish = iterate(lanternfish)
    assert lanternfish == Counter({0: 1, 1: 2, 2: 1, 3: 0, 4: 0, 5:0, 6:1, 7:0, 8:1})