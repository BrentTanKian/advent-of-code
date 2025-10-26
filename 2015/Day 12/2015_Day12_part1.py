if __name__ == "__main__":
    file_path = 'input.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_ele, i = lines[0], 0
        num_indexes, numbers = [], []
        while i < len(line_ele):
            if line_ele[i] == '-' or line_ele[i].isdigit():
                cur_num = line_ele[i]
                while line_ele[i+1].isdigit():
                    cur_num += line_ele[i+1]
                    i += 1
                numbers.append(int(cur_num))
            i += 1
        print(sum(numbers))