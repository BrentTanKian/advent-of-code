if __name__ == "__main__":
    command_list = []
    with open('input.txt', 'r') as file:
        for line in file:
            command_list.append(line.rstrip())
    # Set a to 1 instead of 0 for part 2's solution
    index, a, b = 0, 0, 0
    while index < len(command_list):
        current_command = command_list[index]
        individual_command_list = current_command.split()
        if len(individual_command_list) == 2:
            instr, term = individual_command_list[0], individual_command_list[1]
            if instr == 'hlf':
                if term == 'a':
                    a = a // 2
                else:
                    b = b // 2
                index += 1
            elif instr == 'tpl':
                if term == 'a':
                    a *= 3
                else:
                    b *= 3
                index += 1
            elif instr == 'inc':
                if term == 'a':
                    a += 1
                else:
                    b += 1
                index += 1
            elif instr == 'jmp':
                if term[0] == '-':
                    index -= int(term[1:])
                else:
                    index += int(term[1:])
        else:
            instr, term, offset = individual_command_list[0], individual_command_list[1][0], individual_command_list[2]
            if instr == 'jie' and term == 'a':
                if a % 2 == 0:
                    index += int(offset)
                else:
                    index += 1
            elif instr == 'jie' and term == 'b':
                if b % 2 == 0:
                    index += int(offset)
                else:
                    index += 1
            if instr == 'jio' and term == 'a':
                if a == 1:
                    index += int(offset)
                else:
                    index += 1
            elif instr == 'jio' and term == 'b':
                if b == 1:
                    index += int(offset)
                else:
                    index += 1
        print(a, b, index, individual_command_list)