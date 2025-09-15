def configure_lighting(lights, instruction_line, x1, y1, x2, y2):
    if instruction_line[0] == 'toggle':
        for i in range(x1, x2 + 1):
            for n in range(y1, y2 + 1):
                lights[(i, n)] += 2
    elif instruction_line[0] == 'turn':
        if instruction_line[1] == 'off':
            for i in range(x1, x2 + 1):
                for n in range(y1, y2 + 1):
                    if lights[(i, n)] > 0:
                        lights[(i, n)] -= 1
        elif instruction_line[1] == 'on':
            for i in range(x1, x2 + 1):
                for n in range(y1, y2 + 1):
                    lights[(i, n)] += 1


if __name__ == "__main__":
    lights = {}
    for i in range(1000):
        for n in range(1000):
            lights[(i, n)] = 0
    file_path = 'input.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_list = line.split()
            points = [i for i in line_list if ',' in i]
            point1, point2 = points[0].split(','), points[1].split(',')
            x1, y1, x2, y2 = int(point1[0]), int(point1[1]), int(point2[0]), int(point2[1])
            configure_lighting(lights, line_list, x1, y1, x2, y2)
    counter = 0
    for ele in lights:
        counter += lights[ele]
    print(counter)



