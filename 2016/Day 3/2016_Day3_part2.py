def triangle_checker(triangles):
    counter = 0
    for i in range(0, len(triangles), 3):
        group = sorted(triangles[i: i+3])
        if group[0] + group[1] > group[2]:
            counter += 1
    return counter

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.readlines()
    cleaned_lines = [line.strip() for line in content]
    col1, col2, col3 = [], [], []
    for line in cleaned_lines:
        new_line = [int(i) for i in line.split()]
        col1.append(new_line[0])
        col2.append(new_line[1])
        col3.append(new_line[2])
    valid_triangles = triangle_checker(col1) + triangle_checker(col2) + triangle_checker(col3)
    print(valid_triangles)