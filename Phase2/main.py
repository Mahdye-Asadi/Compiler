# main.py
from lexer import lexer
from parserr import parser, productions_list

# Read input from 'input.txt' file
with open('input.txt', 'r') as input_file:
    input_str = input_file.read()

# Parse the input
result = parser.parse(input_str, lexer=lexer)

# Rule numbers
rule_numbers = {}
rule_counter = 1
for productions in productions_list[::-1]:
    if productions not in rule_numbers:
        rule_numbers[productions] = rule_counter
        rule_counter += 1

# Additional logic or processing based on the parsed result
if result:
    print("Parsing successful!")
   # Alternatively, you can write the productions to the 'output.txt' file
    with open('output.txt', 'w') as output_file:
        for production in productions_list:
            if production in rule_numbers:
                rule_number = str(rule_numbers[production])
                formatted_line = f"{rule_number.ljust(5)} {production}"
                output_file.write(formatted_line + '\n')
else:
    print("Parsing failed!")
