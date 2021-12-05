import pytest
from aoc_2021.d04_GiantSquid.d04_GiantSquid_1 import load_input, check_if_board_has_won, check_board_for_number_and_mark, sum_unmarked_numbers, run_through_draws

def test_load_input():
    filepath = "aoc_2021/d04_GiantSquid/inputs/test_input.txt"
    ret_vals = load_input(filepath)
    assert ret_vals["remaining_draws"] == [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    assert len(ret_vals["grids"]) == 3
    assert len(ret_vals["grids"][0]) == 5
    assert len(ret_vals["grids"][0][0]) == 5

def test_mark_board():
    board = [[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]]

    target_board = [[1,2,3,4,None],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]]

    assert check_board_for_number_and_mark(board,5) == target_board

def test_check_board_won():
    filepath = "aoc_2021/d04_GiantSquid/inputs/test_input.txt"
    ret_vals=load_input(filepath)
    for board in ret_vals["grids"]:
        #Returns false for complete boards
        assert check_if_board_has_won(board) == False

    board = [[1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [None,None,None,None,None]]
    assert check_if_board_has_won(board) == True

    board = [[1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [None,None,None,None,5]] 
    assert check_if_board_has_won(board) == False

    board = [[1,2,3,None,5],
            [1,2,3,None,5],
            [1,2,3,None,5],
            [1,2,3,None,5],
            [1,2,3,None,5]] 
    assert check_if_board_has_won(board) == True

    board = [[1,2,3,None,5],
            [1,2,3,None,5],
            [1,2,3,None,5],
            [1,2,3,None,5],
            [1,2,3,4,5]] 
    assert check_if_board_has_won(board) == False

def test_sum_unmarked_nums():
    board = [[1,2,3,None,5],
            [1,2,3,None,5],
            [1,2,3,None,5],
            [1,2,3,None,5],
            [1,2,3,None,5]] 
    assert sum_unmarked_numbers(board) == 55

def test_run_through_boards():
    filepath = "aoc_2021/d04_GiantSquid/inputs/test_input.txt"
    ret_vals=load_input(filepath)
    (last_draw,complete_board) = run_through_draws(ret_vals["remaining_draws"], ret_vals["grids"])
    assert last_draw == 24
    assert complete_board == [[None, None, None, None, None],
                                [10, 16, 15, None, 19],
                                [18, 8,None, 26, 20],
                                [22, None, 13, 6, None],
                                [None, None, 12, 3, None]]



