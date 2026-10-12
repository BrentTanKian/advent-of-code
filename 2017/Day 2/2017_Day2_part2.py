if __name__ == "__main__":
    with open('input.txt') as f:
        lines_list = f.readlines()
    lines_list = [line.strip().split() for line in lines_list]
    checksum = 0
    for group in lines_list:
        group_list = [int(ele) for ele in group]
        group_list.sort()
        cur_index, factor, indicator = len(group_list) - 1, 0, 0
        while cur_index > 1:
            for i in range(cur_index):
                if group_list[cur_index] % group_list[i] == 0:
                    factor = group_list[i]
                    indicator += 1
                    break
            if indicator == 1:
                checksum += group_list[cur_index] // factor
                break
            cur_index -= 1
    print(checksum)