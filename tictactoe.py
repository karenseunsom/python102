board = [
    ['x', 'x', '_'],
    ['_', 'o', 'x'],
    ['_', 'o', '_']
]

# print(board[0][1])


while True: 
        row_index = 0
        for row in board:
            col_index = 0
            for col in row:
                print(col, end='     ')
                col_index += 1
            print('')
            print('')
            row_index += 1

        pos_row = int(input('which row? '))
        pos_col = int(input('which column? '))

        board[pos_row][pos_col] = 'X'
