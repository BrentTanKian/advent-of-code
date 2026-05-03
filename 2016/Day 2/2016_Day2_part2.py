def find_number(cur_position, instruction):
    master_list = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0], [0, 0, 'D', 0, 0]]
    for letter in instruction:
        if letter == 'U':
            first_coord = cur_position[0]-1
            if first_coord < 0:
                first_coord = 0
        elif letter == 'D':
            first_coord = cur_position[0]+1
            if first_coord > 4:
                first_coord = 4
        if letter == 'U' or letter == 'D':
            new_position = [first_coord, cur_position[1]]
        if letter == 'L':
            second_coord = cur_position[1]-1
            if second_coord < 0:
                second_coord = 0            
        elif letter == 'R':
            second_coord = cur_position[1]+1
            if second_coord > 4:
                second_coord = 4   
        if letter == 'L' or letter == 'R':
            new_position = [cur_position[0], second_coord]
        new_value = master_list[new_position[0]][new_position[1]]
        if new_value == 0:
            continue
        else:
            cur_position = new_position
    return [cur_position, master_list[cur_position[0]][cur_position[1]]]


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.readlines()
    cleaned_lines = [line.strip() for line in content]
    position = [2, 0]
    bathroom_code = ''
    for instruction in cleaned_lines:
        results = find_number(position, instruction)
        position = results[0]
        bathroom_code += str(results[1])
    print(bathroom_code)