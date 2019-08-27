def bomber(field):
    if not field or len(field[0]) < 1:
        return 0
    
    for row in range(0, len(field)):
        row_stack = []
        num_enemies = 0
        for col in range(0, len(field[0])):
            if field[row][col] == '0':
                row_stack.append((row, col))
            elif field[row][col] == 'E':
                num_enemies += 1
            if field[row][col] == 'W' or col == len(field[0])-1:
                while row_stack:                    
                    r, c = row_stack.pop(0)
                    field[r][c] = str(num_enemies)
                num_enemies = 0
    # print(field)

    for col in range(0, len(field[0])):
        col_stack = []
        num_enemies = 0
        max_r_enemies = 0
        for row in range(0, len(field)):
            if field[row][col] == 'E':
                num_enemies += 1
            if field[row][col] == '0':
                col_stack.append((row, col))
            if str(field[row][col]).isdigit() and int(field[row][col]) > 0:
                col_stack.append((row, col))

            if field[row][col] == 'W' or row == len(field) - 1:
                while col_stack:                    
                    r, c = col_stack.pop(0)
                    field[r][c] = (int(field[r][c]) + int(num_enemies))
                num_enemies = 0
    
    # print('-------')
    # print(field)
    res = 0
    for row in range(0, len(field)):
        for col in range(0, len(field[0])):
            if str(field[row][col]).isdigit():
                res = max(res, int(field[row][col]))

    return res
            
  
