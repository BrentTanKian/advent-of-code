def wrapping_paper_area(dimensions):
    individual_dimensions = dimensions.split("x")
    length, width, height = int(individual_dimensions[0]), int(individual_dimensions[1]), int(individual_dimensions[2])
    partial_area = (2 * length * width) + (2 * width * height) + (2 * length * height)
    small_additional_area = min([length * width, width * height, length * height])
    total_area = partial_area + small_additional_area
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