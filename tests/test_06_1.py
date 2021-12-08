from aoc_2021.d06_Lanternfish.d06_Lanternfish_1 import load_input, iterate

def test_load_input():
    assert load_input("aoc_2021/d06_Lanternfish/inputs/test_input.txt") == [3,4,3,1,2]

def test_iterate():
    lanternfish = load_input("aoc_2021/d06_Lanternfish/inputs/test_input.txt")
    lanternfish = iterate(lanternfish)
    assert lanternfish == [2,3,2,0,1]
    lanternfish = iterate(lanternfish)
    assert lanternfish == [1,2,1,6,0,8]