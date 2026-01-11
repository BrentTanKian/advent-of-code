if __name__ == "__main__":
    file_path1, file_path2 = 'input.txt', 'input1.txt'
    mappings, main_str, elements, strings = [], '', [], []
    with open(file_path1, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_list = line.split()
            mappings.append((line_list[0], line_list[2]))
    with open(file_path2, 'r') as file1:
        lines = file1.readlines()
        main_str = lines[0]
    i = 0
    while i < len(main_str) - 1:
        if main_str[i].isupper() and main_str[i+1].islower():
            elements.append(main_str[i:i+2])
            i += 2
        elif main_str[i].isupper() and main_str[i+1].isupper():
            elements.append(main_str[i])
            i += 1
    for group in mappings:
        temp_elements = elements.copy()
        left, right = group[0], group[1]
        indexes = [i for i in range(len(elements)) if elements[i] == left]
        if indexes:
            for index in indexes:
                temp_elements[index] = right
                strings.append(''.join(temp_elements))
                temp_elements = elements.copy()
    print(len(set(strings)))

