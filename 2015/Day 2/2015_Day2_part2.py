def wrapping_paper_area(dimensions):
    individual_dimensions = dimensions.split("x")
    length, width, height = int(individual_dimensions[0]), int(individual_dimensions[1]), int(individual_dimensions[2])
    sorted_dimensions = sorted([length, width, height])
    shortest_perimeter = (sorted_dimensions[0] * 2) + (sorted_dimensions[1] * 2)
    total_area = shortest_perimeter + (length * width * height)
    return total_area


if __name__ == "__main__":
    total_area = 0
    file_path = 'input.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            box_area = wrapping_paper_area(line)
            total_area += box_area
    print(total_area)