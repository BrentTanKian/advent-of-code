import random

if __name__ == "__main__":
    file_path1, file_path2 = 'input.txt', 'input1.txt'
    mappings, main_str = [], ''
    with open(file_path1, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_list = line.split()
            mappings.append((line_list[0], line_list[2]))
    with open(file_path2, 'r') as file1:
        lines = file1.readlines()
        main_str = lines[0]
    steps = 0
    target = main_str
    while True:
        main_str = target
        steps = 0
        random.shuffle(mappings)
        mappings.sort(key=lambda x: len(x[1]), reverse=True)
        while main_str != "e":
            changed = False
            for left, right in mappings:
                idx = main_str.rfind(right)
                if idx != -1:
                    main_str = main_str[:idx] + left + main_str[idx + len(right):]
                    steps += 1
                    changed = True
                    break
            if not changed:
                break
        if main_str == "e":
            print(steps, main_str)
            break