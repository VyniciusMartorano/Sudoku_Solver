def get_numbers_not_used_in_array(array: list) -> list:
    VALID_NUMBERS = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    return list(set(array).symmetric_difference(VALID_NUMBERS))

def get_not_used_in_quadrante(array: list, index_x: int, index_y: int) -> list:
    numbers = []
    start_linha = index_y - index_y % 3
    end_col = index_x - index_x % 3    
    for linha in range(3):
        for coluna in range(3): numbers.append(array[linha + start_linha][coluna + end_col])
    return get_numbers_not_used_in_array(numbers)

def get_numbers_of_collunm_by_index_x(lines: list, index_x: int) -> list:
    return [line[index_x] for line in lines]

def get_numbers_available_in_position_XY(data: list, index_x: int, index_y: int) -> list:
    col = set(get_numbers_not_used_in_array(get_numbers_of_collunm_by_index_x(data, index_x=index_x)))
    row = set(get_numbers_not_used_in_array(data[index_y]))
    quadrante = set(get_not_used_in_quadrante(data, index_x=index_x, index_y=index_y))
    return list(col & row & quadrante)

def solve_sudoku(data: list) -> bool:
    position = find_empty(data=data)
    if not position: return True
    else: y, x = position

    for num in range(1,10):
        if number_is_valid(data=data, num=num, index_y=y, index_x=x):
            data[y][x] = num
            if solve_sudoku(data=data): return True
            data[y][x] = 0
    return False

def number_is_valid(data: list, num: int, index_x: int, index_y: int) -> bool: 
    available_nums = get_numbers_available_in_position_XY(data=data, index_x=index_x, index_y=index_y)
    if num not in available_nums: return False
    return True

def find_empty(data: list):
    for y in range(9):
        for x in range(9):
            if data[y][x] == 0: return (y, x)
    return None

def read_file(path: str) -> list:
    data = []
    try:
        with open(path, 'r') as file:
            while True:        
                line = file.readline()[:-1]
                if line == '': break
                data.append([int(num) for num in line.split(';')])
            file.close()
            return data
    except: 
        print(f'não foi possivel abrir o arquivo:\n{path}')
        return []


def write_in_arq(path: str, content: list) -> None:
    try:
        with open(path, 'w+') as file:
            for linha in content:
                value = ''
                for item in linha: value += str(item) + ';'
                value += '\n'
                file.write(value)
            file.close()
    except FileExistsError: ...
    else: print(f'O arquivo {path} foi escrito com sucesso')

def print_sudoku(data: list) -> None:
    print('\nSolved game:\n')
    for row in range(len(data)):
        if row % 3 == 0 and row != 0: print("- - - - - - - - - - - - - ")
        for col in range(len(data[0])):
            if col % 3 == 0 and col != 0: print(" | ", end="")

            if col == 8: print(data[row][col])
            else: print(str(data[row][col]) + " ", end="")