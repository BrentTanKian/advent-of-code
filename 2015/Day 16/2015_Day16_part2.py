if __name__ == "__main__":
    master_dict = {"children": 3,
                    "cats": 7,
                    "samoyeds": 2,
                    "pomeranians": 3,
                    "akitas": 0,
                    "vizslas": 0,
                    "goldfish": 5,
                    "trees": 3,
                    "cars": 2,
                    "perfumes": 1}
    correct_sue_number = 0
    file_path = 'input.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            sue_number = 0
            ele, counts = [], []
            line_data = line.split()
            for n in range(1, len(line_data)):
                if n == 1:
                    sue_number = int(line_data[n][:-1])
                elif n % 2 == 0:
                    ele.append((line_data[n][:-1]))
                else:
                    if n != len(line_data) - 1:
                        counts.append(int(line_data[n][:-1]))
                    else:
                        counts.append(int(line_data[n]))
            line_dict, checker = dict(zip(ele, counts)), 0
            for i in line_dict:
                if (
        (i in ['cats', 'trees'] and line_dict[i] <= master_dict[i]) or
        (i in ['pomeranians', 'goldfish'] and line_dict[i] >= master_dict[i]) or
        (i not in ['cats', 'trees', 'pomeranians', 'goldfish'] and line_dict[i] != master_dict[i])
                ):
                    checker += 1
                    break
            if checker == 0:
                correct_sue_number = sue_number
    print(correct_sue_number)

