if __name__ == "__main__":
    with open('input.txt') as f:
        lines_list = f.readlines()
    line_ele = lines_list[0]
    start_index, total = 0, 0
    while start_index < len(line_ele) - 1:
        if line_ele[start_index] == line_ele[start_index + 1]:
            total += int(line_ele[start_index])
        start_index += 1
    if line_ele[-1] == line_ele[0]:
        total += int(line_ele[-1])
    print(total)