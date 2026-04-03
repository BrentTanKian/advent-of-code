if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    instruction_list = content.split(", ")
    coordinates = [0, 0]
    direction = 'N'
    index = 0
    while index < len(instruction_list):
        cur_instr = instruction_list[index]
        if direction == 'N':
            if cur_instr[0] == 'R':
                coordinates[0] += int(cur_instr[1:])
                direction = 'E'
            else:
                coordinates[0] -= int(cur_instr[1:])
                direction = 'W'
        elif direction == 'S':
            if cur_instr[0] == 'R':
                coordinates[0] -= int(cur_instr[1:])
                direction = 'W'
            else:
                coordinates[0] += int(cur_instr[1:])
                direction = 'E'
        elif direction == 'E':
            if cur_instr[0] == 'R':
                coordinates[1] -= int(cur_instr[1:])
                direction = 'S'
            else:
                coordinates[1] += int(cur_instr[1:])
                direction = 'N'
        elif direction == 'W':
            if cur_instr[0] == 'R':
                coordinates[1] += int(cur_instr[1:])
                direction = 'N'
            else:
                coordinates[1] -= int(cur_instr[1:])
                direction = 'S'
        index += 1
    print(coordinates)
