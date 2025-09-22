def process_bitwise_variables(line_string):
    line_string_list = line_string.split()
    relevant_variable_list = []
    if "NOT" in line_string_list:
        relevant_variable_list.append(line_string_list[1])
    elif "LSHIFT" in line_string_list or "RSHIFT" in line_string_list or len(line_string_list) == 3:
        relevant_variable_list.append(line_string_list[0])
    elif "AND" in line_string_list or "OR" in line_string_list:
        if not is_integer(line_string_list[0]):
            relevant_variable_list.append(line_string_list[0])
        if not is_integer(line_string_list[2]):
            relevant_variable_list.append(line_string_list[2])
    return relevant_variable_list

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def process_bitwise_operations(line_string, variables):
    line_string_list = line_string.split()
    if "NOT" in line_string_list:
        cur_value = variables[line_string_list[1]]
        final_value = ~cur_value & 0xFFFF
        variables[line_string_list[-1]] = final_value
    elif "LSHIFT" in line_string_list:
        cur_value = variables[line_string_list[0]]
        lshift_amount = int(line_string_list[2])
        final_value = cur_value << lshift_amount
        variables[line_string_list[-1]] = final_value
    elif "RSHIFT" in line_string_list:
        cur_value = variables[line_string_list[0]]
        rshift_amount = int(line_string_list[2])
        final_value = cur_value >> rshift_amount
        variables[line_string_list[-1]] = final_value
    elif "AND" in line_string_list:
        cur_value2 = variables[line_string_list[2]]
        if is_integer(line_string_list[0]):
            cur_value1 = int(line_string_list[0])
        else:
            cur_value1 = variables[line_string_list[0]]
        final_value = cur_value1 & cur_value2
        variables[line_string_list[-1]] = final_value
    elif "OR" in line_string_list:
        cur_value1, cur_value2 = variables[line_string_list[0]], variables[line_string_list[2]]
        final_value = cur_value1 | cur_value2
        variables[line_string_list[-1]] = final_value
    elif len(line_string_list) == 3:
        variables[line_string_list[-1]] = variables[line_string_list[0]]

if __name__ == "__main__":
    file_path = 'input.txt'
    variables, instructions = {}, []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_list = line.split()
            if len(line_list) == 3 and is_integer(line_list[0]):
                variables[line_list[-1]] = int(line_list[0])
            else:
                instructions.append(line)
    while instructions:
        for instruction in instructions:
            relevant_variables = process_bitwise_variables(instruction)
            if (len(relevant_variables) == 1 and relevant_variables[0] in variables) or (len(relevant_variables) == 2 and relevant_variables[0] in variables and relevant_variables[1] in variables):
                process_bitwise_operations(instruction, variables)
                instructions.remove(instruction)
    print(variables['a'])




