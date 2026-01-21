# Global Variables
invalid_inputs = []

# --------------------------------------------------

puzzle_input = "2025\Day 2\Challenge 1\PuzzelInput.txt"

def file_to_list(path_to_input_file):
    with open(path_to_input_file, 'r') as file:
        line = file.read().strip()
        items = line.split(',')
    return items

list_of_input = file_to_list(puzzle_input)

# --------------------------------------------------

def is_pattern_number(string):
    # Split string in half and store each half to be compared
    first_half = string[:len(string)//2]  # everything from beginning until the half
    second_half = string[len(string)//2:]  # everything from half until the end
    return first_half == second_half
    
# --------------------------------------------------

def get_range(string):
    # Strings in the list are ranges like "11-35"
    bounds = string.split("-")
    min_str = bounds[0]
    max_str = bounds[1]
    
    min_num = int(min_str)
    max_num = int(max_str)

    list_of_numbers_in_range = list(range(min_num, max_num+1))
    list_of_strings = [str(num) for num in list_of_numbers_in_range]
    return list_of_strings

# --------------------------------------------------

for range_string in list_of_input:
    numbers_in_range = get_range(range_string)
    for number_string in numbers_in_range:
        if is_pattern_number(number_string):
            # Append to a list of all invalid inputs
            invalid_inputs.append(number_string)

# Convert to integers for summing
invalid_input_values = [int(value) for value in invalid_inputs]

total = sum(invalid_input_values)

print(total)
