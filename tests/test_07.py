from aoc_2021.d07_Treachery_of_Whales.d07_Treachery_of_Whales import load_input, calc_cost, get_min_cost_x

def test_load_input():
    assert load_input("aoc_2021/d07_Treachery_of_Whales/inputs/test_input.txt") == [16,1,2,0,4,2,7,1,2,14]

def test_calc_cost():
    horizontal_positions = load_input("aoc_2021/d07_Treachery_of_Whales/inputs/test_input.txt")
    assert calc_cost(2,horizontal_positions) == 37
    assert calc_cost(1,horizontal_positions) == 41
    assert calc_cost(3,horizontal_positions) == 39
    assert calc_cost(10,horizontal_positions) == 71

def test_get_min_cost_x():
    horizontal_positions = load_input("aoc_2021/d07_Treachery_of_Whales/inputs/test_input.txt")
    # part 1 code
    # assert get_min_cost_x(horizontal_positions) == (2,37) 
    # part 2 code
    assert get_min_cost_x(horizontal_positions) == (5, 168.0)