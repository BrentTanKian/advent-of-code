def string_checker(string):
    checker = 0
    for i in range(len(string)-1):
        cur_string = string[i:i+2]
        if string.count(cur_string) >= 2:
            checker += 1
            break
    for i in range(len(string)-2):
        cur_string = string[i:i+3]
        if cur_string[0] == cur_string[2]:
            checker += 1
            break
    if checker == 2:
        return 1
    return 0


if __name__ == "__main__":
    counter = 0
    file_path = 'input.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            val = string_checker(line)
            counter += val
    print(counter)