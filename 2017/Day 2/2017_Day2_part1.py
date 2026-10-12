if __name__ == "__main__":
    with open('input.txt') as f:
        lines_list = f.readlines()
    lines_list = [line.strip().split() for line in lines_list]
    checksum = 0
    for group in lines_list:
        group_list = [int(ele) for ele in group]
        max_num, min_num = max(group_list), min(group_list)
        checksum += max_num - min_num
    print(checksum)