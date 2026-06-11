def initialize_screen(width, length):
    return [['.' for _ in range(width)] for _ in range(length)]

def rect_method(width, length, base_list):
    for i in range(length):
        for j in range(0, width):
            base_list[i][j] = '#'
    return base_list

def rotate_method(degree, pixel_list):
    for i in range(degree):
        last_ele = pixel_list.pop()
        pixel_list.insert(0, last_ele)
    return pixel_list


if __name__ == "__main__":
    with open('input.txt') as f:
        lines_list = f.readlines()
    cleaned_list = [i.strip() for i in lines_list]
    test_screen = initialize_screen(50, 6)
    for instruction in cleaned_list:
        instruction_list = instruction.split(' ')
        if instruction_list[0] == 'rect':
            dimensions = instruction_list[1]
            dimensions_list = dimensions.split('x')
            test_screen = rect_method(int(dimensions_list[0]), int(dimensions_list[1]), test_screen)
        elif instruction_list[0] == 'rotate':
            row_column_no, magnitude = int(instruction_list[2].split('=')[-1]), int(instruction_list[-1])
            if instruction_list[1] == 'row':
                selected_list = test_screen[row_column_no].copy()
                rotated_list = rotate_method(magnitude, selected_list)
                test_screen[row_column_no] = rotated_list
            elif instruction_list[1] == 'column':
                col_ele = [group[row_column_no] for group in test_screen]
                rotated_list = rotate_method(magnitude, col_ele.copy())
                start_index = 0
                while start_index < len(test_screen):
                    test_screen[start_index][row_column_no] = rotated_list[start_index]
                    start_index += 1
    counter = 0
    for group in test_screen:
        for ele in group:
            if ele == '#':
                counter += 1
    print(counter)
    for row in test_screen:
        print(row)