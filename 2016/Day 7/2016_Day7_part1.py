def checker(string):
    if string[0] == string[-1] and string[1] == string[2] and string[0] != string[1]:
        return True
    else:
        return False

if __name__ == "__main__":
    with open('input.txt') as f:
        lines_list = f.readlines()
    cleaned_list = [i.strip() for i in lines_list]
    count = 0
    for line in cleaned_list:
        outside_check, inside_check = 0, 0
        outside_status = True
        index = 0
        while index + 4 <= len(line):
            group = line[index:index+4]
            if '[' in group:
                outside_status = False
            elif ']' in group:
                outside_status = True
            if checker(group) and outside_status:
                outside_check += 1
            elif checker(group) and not outside_status:
                inside_check += 1
            index += 1
        if outside_check >= 1 and inside_check == 0:
            count += 1
    print(count)