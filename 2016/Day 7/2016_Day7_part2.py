def checker(string):
    if string[0] == string[-1] and string[0] != string[1]:
        return True
    else:
        return False

def transform(string):
    return string[1] + string[0] + string[1]

if __name__ == "__main__":
    with open('input.txt') as f:
        lines_list = f.readlines()
    cleaned_list = [i.strip() for i in lines_list]
    count = 0
    for line in cleaned_list:
        outside_set, inside_set = set(), set()
        outside_status = True
        index = 0
        while index + 3 <= len(line):
            group = line[index:index+3]
            if '[' in group:
                outside_status = False
            elif ']' in group:
                outside_status = True
            if checker(group) and outside_status:
                outside_set.add(group)
            elif checker(group) and not outside_status:
                inside_set.add(group)
            index += 1
        for group in outside_set:
            if transform(group) in inside_set:
                count += 1
                break
    print(count)

