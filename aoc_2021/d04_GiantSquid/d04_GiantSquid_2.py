## Input:
# one long line of numbers to be drawn - this should be loaded into remaining_draws
# any number of 5x5 boards:
# * the boards are separated by empty lines
# * the numbers within each line are separated by spaces

## Goal:
# Work out which board wins first
# Sum all of the unmarked numbers (i.e. numbers that have not been drawn)
# Multiply this some by the last number called (at the time of winning)

import sys
import os

def load_input(filepath):
    f = open(filepath)
    lines = f.readlines()
    f.close()
    remaining_draws = [int(x) for x in lines[0].rstrip().split(',')]
    grids = proc_grid_input(lines[2:])
    ret_vals = {"remaining_draws":remaining_draws,
                "grids":grids}
    return ret_vals


def proc_grid_input(grid_input):
    grids = []
    cur_grid=[]
    for line in grid_input:
        if len(line.strip())!=0:
            cur_grid.append([int(x)for x in line.rstrip().split()])
        else:
            grids.append(cur_grid)
            cur_grid = []
    grids.append(cur_grid) # add last grid
    return grids

def check_board_for_number_and_mark(board,target_num):
    if board is None:
        return None
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == target_num:
                board[y][x] = None
    return board


def check_if_board_has_won(board):
    if board is None:
        return None
    # check rows
    any_row_completed =  any(map(lambda row: all(map(lambda num: num is None ,row)),board))
    # check cols
    any_col_completed = any([all([row[x_pos] is None for row in board]) for x_pos in range(len(board[0]))])
    return (any_row_completed or any_col_completed)

def run_through_draws(remaining_draws, grids):
    last_completed_board = None
    last_completed_board_draw = None
    remaining_incomplete_grids = grids

    for cur_draw in remaining_draws:
        for i in range(0, len(remaining_incomplete_grids)):
            board = remaining_incomplete_grids[i]
            check_board_for_number_and_mark(board,cur_draw)
            if check_if_board_has_won(board):
                last_completed_board = board
                last_completed_board_draw = cur_draw
                remaining_incomplete_grids[i] = None
    #print(last_completed_board)
    return (last_completed_board_draw,last_completed_board,)

def sum_unmarked_numbers(board):
    return sum([sum([0 if x is None else x for x in row]) for row in board])


def main():
    try:
        file_dict = {"test":"test_input",
                    "prod":"input"}
        file_str = file_dict[sys.argv[1]]
    except:
        raise ValueError("Expected second command line argument to specify 'test' or 'prod'")

    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    input_dict = load_input(f"./inputs/{file_str}.txt")
    grids = input_dict["grids"]
    remaining_draws= input_dict["remaining_draws"]
    (last_draw,complete_board) = run_through_draws(remaining_draws, grids)
    sum_unmarked_nums = sum_unmarked_numbers(complete_board)
    print(sum_unmarked_nums * last_draw)

if __name__ == "__main__":       
    main()



    

    




