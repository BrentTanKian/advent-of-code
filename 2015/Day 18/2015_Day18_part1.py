def clean_array(array, master_array_rows, master_array_columns):
    new_array = []
    for group in array:
        if group[0] != -1 and group[0] < master_array_rows and group[1] != -1 and group[1] < master_array_columns:
            new_array.append(group)
    return new_array


if __name__ == "__main__":
    file_path = 'input.txt'
    arrays = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[:-1]:
            arrays.append([i for i in line[:-1]])
    arrays.append([i for i in lines[-1]])
    master_array_row, master_array_columns = len(arrays), len(arrays[0])
    for z in range(100):
        to_turn_on = []
        to_turn_off = []
        for i in range(len(arrays)):
            for j in range(len(arrays[i])):
                current = arrays[i][j]
                neighbours = []
                above = [(i-1, j-1), (i-1, j), (i-1, j+1)]
                same_level = [(i, j-1), (i, j+1)]
                below = [(i+1, j-1), (i+1, j), (i+1, j+1)]
                neighbours.extend(above)
                neighbours.extend(same_level)
                neighbours.extend(below)
                true_neighbours = clean_array(neighbours, master_array_row, master_array_columns)
                true_neighbours_ele = [arrays[group[0]][group[1]] for group in true_neighbours]
                if current == "#":
                    if true_neighbours_ele.count("#") != 2 and true_neighbours_ele.count("#") != 3:
                        to_turn_off.append((i, j))
                elif current == ".":
                    if true_neighbours_ele.count("#") == 3:
                        to_turn_on.append((i, j))
        for group in to_turn_off:
            arrays[group[0]][group[1]] = "."
        for group in to_turn_on:
            arrays[group[0]][group[1]] = "#"
    counter = 0
    for i in range(len(arrays)):
        for j in range(len(arrays[i])):
            if arrays[i][j] == "#":
                counter += 1
    print(counter)


