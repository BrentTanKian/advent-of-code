def letter_counter(string):
    dictionary = {}
    for char in string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    dict_list = list(dictionary.items())
    # Change reverse=True to reverse=False for part 2's solution
    dict_list.sort(key=lambda x: x[1], reverse=True)
    return dict_list[0][0]


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.readlines()
    cleaned_lines = [line.strip() for line in content]
    column_length = len(cleaned_lines[0])
    column_str, correct_msg = [], ""
    for i in range(column_length):
        single_col_vals = ''
        for line in cleaned_lines:
            single_col_vals += line[i]
        column_str.append(single_col_vals)
    for col in column_str:
        char_to_add = letter_counter(col)
        correct_msg += char_to_add
    print(correct_msg)
