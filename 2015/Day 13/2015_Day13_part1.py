import itertools

def calculate_happiness(single_name_list):
    total_happiness = 0
    for i in range(len(single_name_list)):
        if i != len(single_name_list) - 1:
            cur_ele, next_ele = single_name_list[i], single_name_list[i+1]
        else:
            cur_ele, next_ele = single_name_list[i], single_name_list[0]
        net_happiness_gain = storage[cur_ele][next_ele] + storage[next_ele][cur_ele]
        total_happiness += net_happiness_gain
    return total_happiness


if __name__ == "__main__":
    file_path = 'input.txt'
    storage, names, happiness = {}, set(), []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_list = line.split()
            first_name, second_name, gain_or_lose, units = line_list[0], line_list[-1][:-1], line_list[2], line_list[3]
            names.add(first_name)
            names.add(second_name)
            if first_name not in storage:
                storage[first_name] = {}
            if gain_or_lose == 'lose':
                storage[first_name][second_name] = int('-' + units)
            else:
                storage[first_name][second_name] = int(units)
    name_list = list(names)
    name_permutations = list(itertools.permutations(name_list))
    for name_list in name_permutations:
        happiness.append(calculate_happiness(name_list))
    print(max(happiness))