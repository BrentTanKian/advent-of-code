def find_number(cur_position, instruction):
    master_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for letter in instruction:
        if letter == 'U':
            cur_position[0] -= 1
            if cur_position[0] < 0:
                cur_position[0] = 0
        elif letter == 'D':
            cur_position[0] += 1
            if cur_position[0] > 2:
                cur_position[0] = 2
        elif letter == 'L':
            cur_position[1] -= 1
            if cur_position[1] < 0:
                cur_position[1] = 0
        elif letter == 'R':
            cur_position[1] += 1
            if cur_position[1] > 2:
                cur_position[1] = 2
    return [cur_position, master_list[cur_position[0]][cur_position[1]]]


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.readlines()
    cleaned_lines = [line.strip() for line in content]
    position = [1, 1]
    bathroom_code = ''
    for instruction in cleaned_lines:
        results = find_number(position, instruction)
        position = results[0]
        bathroom_code += str(results[1])
    print(bathroom_code)
