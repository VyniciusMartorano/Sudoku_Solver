import os
from functions_sudoku import solve_sudoku, write_in_arq, print_sudoku, read_file



os.system('cls')
input_sudoku_path = os.path.dirname(__file__) + '//sudoku_input.txt'
output_sudoku_path = os.path.dirname(__file__) + '//sudoku_output.txt'
full_game = read_file(input_sudoku_path)


if full_game:
    if solve_sudoku(data=full_game):
        write_in_arq(path=output_sudoku_path, content=full_game)
        print_sudoku(data=full_game)
    else: print('Não foi possivel resolver o soduko')
