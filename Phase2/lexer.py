# lexer.py
from ply import lex

reserved = {
    'program': 'PROGRAM_KW',
    'integer': 'INTEGER_KW',
    'real': 'REAL_KW',
    'boolean': 'BOOLEAN_KW',
    'function': 'FUNCTION_KW',
    'begin': 'BEGIN_KW',
    'end': 'END_KW',
    'if': 'IF_KW',
    'then': 'THEN_KW',
    'else': 'ELSE_KW',
    'while': 'WHILE_KW',
    'do': 'DO_KW',
    'for': 'FOR_KW',
    'to': 'TO_KW',
    'return': 'RETURN_KW',
    'and': 'AND_KW',
    'or': 'OR_KW',
    'true': 'TRUE_KW',
    'false': 'FALSE_KW',
}

tokens = [
    'ID',
    'INTEGER_NUMBER',
    'REAL_NUMBER',
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

t_ADD_OP = r'\+'
t_SUB_OP = r'-'
t_DIV_OP = r'/'
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

t_ignore_SPACE = r'[\s\n\r\t]+'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_REAL_NUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
