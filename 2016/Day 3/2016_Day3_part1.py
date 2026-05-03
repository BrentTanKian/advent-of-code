if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.readlines()
    cleaned_lines = [line.strip() for line in content]
    counter = 0
    for line in cleaned_lines:
        new_line = sorted([int(i) for i in line.split()])
        if new_line[0] + new_line[1] > new_line[2]:
            counter += 1
    print(counter)