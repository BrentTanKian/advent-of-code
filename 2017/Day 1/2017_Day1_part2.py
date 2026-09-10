if __name__ == "__main__":
    with open('input.txt') as f:
        lines_list = f.readlines()
    line_ele = lines_list[0]
    start_index, total, jump = 0, 0, len(line_ele) // 2
    while start_index < len(line_ele):
        jumped_index = start_index + jump
        if jumped_index > len(line_ele) - 1:
            jumped_index = jumped_index - len(line_ele)
        if line_ele[start_index] == line_ele[jumped_index]:
            total += int(line_ele[start_index])
        start_index += 1
    (print(total))