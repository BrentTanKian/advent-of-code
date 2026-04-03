import sys

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    instruction_list = content.split(", ")
    coordinates = [0, 0]
    storage = set()
    storage.add((0, 0))
    direction = 'N'
    index = 0
    while index < len(instruction_list):
        cur_instr = instruction_list[index]
        if direction == 'N':
            if cur_instr[0] == 'R':
                for i in range(1, int(cur_instr[1:]) + 1):
                    to_add = (coordinates[0] + i, coordinates[1])
                    if to_add in storage:
                        print(to_add)
                        sys.exit()
                    else:
                        storage.add(to_add)
                coordinates[0] += int(cur_instr[1:])
                direction = 'E'
            else:
                for i in range(1, int(cur_instr[1:]) + 1):
                    to_add = (coordinates[0] - i, coordinates[1])
                    if to_add in storage:
                        print(to_add)
                        sys.exit()
                    else:
                        storage.add(to_add)
                coordinates[0] -= int(cur_instr[1:])
                direction = 'W'           
        elif direction == 'S':
            if cur_instr[0] == 'R':
                for i in range(1, int(cur_instr[1:]) + 1):
                    to_add = (coordinates[0] - i, coordinates[1])
                    if to_add in storage:
                        print(to_add)
                        sys.exit()
                    else:
                        storage.add(to_add)
                coordinates[0] -= int(cur_instr[1:])
                direction = 'W'
            else:
                for i in range(1, int(cur_instr[1:]) + 1):
                    to_add = (coordinates[0] + i, coordinates[1])
                    if to_add in storage:
                        print(to_add)
                        sys.exit()
                    else:
                        storage.add(to_add)
                coordinates[0] += int(cur_instr[1:])
                direction = 'E'            
        elif direction == 'E':
            if cur_instr[0] == 'R':
                for i in range(1, int(cur_instr[1:]) + 1):
                    to_add = (coordinates[0], coordinates[1] - i)
                    if to_add in storage:
                        print(to_add)
                        sys.exit()
                    else:
                        storage.add(to_add)
                coordinates[1] -= int(cur_instr[1:])
                direction = 'S'
            else:
                for i in range(1, int(cur_instr[1:]) + 1):
                    to_add = (coordinates[0], coordinates[1] + i)
                    if to_add in storage:
                        print(to_add)
                        sys.exit()
                    else:
                        storage.add(to_add)
                coordinates[1] += int(cur_instr[1:])
                direction = 'N'
        elif direction == 'W':
            if cur_instr[0] == 'R':
                for i in range(1, int(cur_instr[1:]) + 1):
                    to_add = (coordinates[0], coordinates[1] + i)
                    if to_add in storage:
                        print(to_add)
                        sys.exit()
                    else:
                        storage.add(to_add)
                coordinates[1] += int(cur_instr[1:])
                direction = 'N'
            else:
                for i in range(1, int(cur_instr[1:]) + 1):
                    to_add = (coordinates[0], coordinates[1] - i)
                    if to_add in storage:
                        print(to_add)
                        sys.exit()
                    else:
                        storage.add(to_add)
                coordinates[1] -= int(cur_instr[1:])
                direction = 'S'
        index += 1
    print(coordinates)