from ply import lex

# Dictionary for reserved words
reserved = {
    'program' : 'PROGRAM_KW',
   'integer' : 'INTEGER_KW',
   'real' : 'REAL_KW',
   'boolean' : 'BOOLEAN_KW',
   'function' : 'FUNCTION_KW',
   'begin' : 'BEGIN_KW',
   'end' : 'END_KW',
   'if' : 'IF_KW',
   'then' : 'THEN_KW',
   'else' : 'ELSE_KW',
   'while' : 'WHILE_KW',
   'do' : 'DO_KW',
   'for' : 'FOR_KW',
   'to' : 'TO_KW',
   'return' : 'RETURN_KW',
   'and' : 'AND_KW',
   'or' : 'OR_KW',
   'true' : 'TRUE_KW',
   'false' : 'FALSE_KW',
}
# List of token names.   This is always required
tokens = [
   'ID',
   'NUMBER',
   'FLOAT',
   'ADD_OP',
   'SUB_OP',
   'DIV_OP',
   'MUL_OP',
   'LEFT_PA',
   'RIGHT_PA',
   'GT_OP',
   'GE_OP',
   'LT_OP',
   'LE_OP',
   'EQ_OP',
   'ASSIGN_OP',
   'NE_OP',
   'COLON',
   'SEMICOLON',
   'COMMA',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_ADD_OP = r'\+'
t_SUB_OP = r'\-'
t_DIV_OP = r'\/'
t_MUL_OP = r'\*'
t_LEFT_PA = r'\('
t_RIGHT_PA = r'\)'
t_GT_OP = r'>'
t_GE_OP = r'>='
t_LT_OP = r'<'
t_LE_OP = r'<='
t_EQ_OP = r'='
t_ASSIGN_OP = r':='
t_NE_OP = r'<>'
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','

# define a definition and row-number for symbol table
symbol_table = {}
current_row = 1

# Identifiers and keywords recognizer
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')  # Check for reserved words
    global current_row
    if t.type == 'ID' and str(t.value) not in symbol_table:
        symbol_table[str(t.value)] = current_row
        current_row += 1
    return t

# A regular expression rule for float numbers
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    global current_row
    if t.type == 'FLOAT' and str(t.value) not in symbol_table:
        symbol_table[str(t.value)] = current_row
        current_row += 1
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    global current_row
    if t.type == 'NUMBER' and str(t.value) not in symbol_table:
        symbol_table[str(t.value)] = current_row
        current_row += 1
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Read the input file
input_file = open("input.txt", 'r')  # Replace with the actual filename
input_data = input_file.read()

lexer.input(input_data)

# Tokenize
output_data = []
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    elif tok.type == "ID" or tok.type == "NUMBER":
        output_data.append([f"{tok.value}", f"<{tok.type}, {symbol_table[str(tok.value)]}>"])
    else:
        output_data.append([f"{tok.value}", f"<{tok.type}, ->"])

# Create a file for writing the output
output_file = open("output.txt", 'w')  # Replace with the desired output file name
# Redirect standard output to the file
write_to_file = lambda x : output_file.write(x + '\n')

# Define the print_table function
def print_table(data):
    column1 = [row[0] for row in data]
    column2 = [row[1] for row in data]

    max_length1 = max(len(str(item)) for item in column1)
    max_length2 = max(len(str(item)) for item in column2)

    for row in data:
        write_to_file(f'{row[0] : <{max_length1}}     {row[1] : <{max_length2}}')

# Print the table to the output file
print_table(output_data)

# Close the output file
output_file.close()
# Finally you can open the file named "output.txt" and see the result.
print("Output has been written to 'output.txt' file")