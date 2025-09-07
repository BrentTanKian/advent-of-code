def string_checker(string):
    exclude_list = ["ab", "cd", "pq", "xy"]
    for ele in exclude_list:
        if ele in string:
            return 0
    vowel_val = 0
    vowel_list = ["a", "e", "i", "o", "u"]
    for ele in vowel_list:
        counts = string.count(ele)
        vowel_val += counts
    if vowel_val < 3:
        return 0
    string_letters = set([letter for letter in string])
    for letter in string_letters:
        group = letter + letter
        if group in string:
            return 1
    return 0


if __name__ == "__main__":
    counter = 0
    file_path = 'input.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            val = string_checker(line)
            counter += val
    print(counter)

