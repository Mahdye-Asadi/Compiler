# parser.py
from ply import yacc, lex
from lexer import tokens

precedence = (
    ('left', 'LEFT_PA', 'RIGHT_PA'),
    ('left', 'MUL_OP', 'DIV_OP'),
    ('left', 'ADD_OP', 'SUB_OP'),
    ('left', 'AND_KW', 'OR_KW'),
)

def p_start(p):
    '''start : PROGRAM_KW ID SEMICOLON decList funcList block'''
    p[0] = {'program_id': p[2], 'declarations': p[4], 'functions': p[5], 'block': p[6]}
    slice_to_production(p)

def p_decList(p):
    '''decList : empty
                | decs
                | decList decs'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = list(filter(None, (p[1], p[2])))
    else:
        pass
    slice_to_production(p)

def p_decs(p):
    '''decs : type varList SEMICOLON'''
    if len(p) == 4:
        p[0] = [p[1]] + p[2]
    else:
        pass
    slice_to_production(p)

def p_type(p):
    '''type : INTEGER_KW
            | REAL_KW
            | BOOLEAN_KW'''
    p[0] = p[1]
    slice_to_production(p)

def p_varList(p):
    '''varList : ID
               | varList COMMA ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = p[1] + [p[3]]
    slice_to_production(p)

def p_funcList(p):
    '''funcList : funcList funcDec
                | empty'''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    elif len(p) == 2:
        p[0] = p[1]
    else:
        pass
    slice_to_production(p)

def p_funcDec(p):
    '''funcDec : FUNCTION_KW ID parameters COLON type decList block'''
    p[0] = (p[2], p[3], p[5], p[6], p[7])
    slice_to_production(p)

def p_parameters(p):
    '''parameters : LEFT_PA decList RIGHT_PA'''
    p[0] = p[2]
    slice_to_production(p)

def p_block(p):
    '''block : BEGIN_KW stmtList END_KW'''
    p[0] = p[2]
    slice_to_production(p)

def p_stmtList(p):
    '''stmtList : stmt
                | stmtList stmt'''
    if len(p) == 3:
        p[0] = [p[1]] if not isinstance(p[1], list) else p[1]
        p[0].append(p[2])
    elif len(p) == 2:
        p[0] = [p[1]] if not isinstance(p[1], list) else p[1]
    slice_to_production(p)

def p_stmt(p):
    '''stmt : ID ASSIGN_OP expr SEMICOLON
            | IF_KW expr THEN_KW stmt
            | IF_KW expr THEN_KW stmt ELSE_KW stmt
            | WHILE_KW expr DO_KW stmt
            | FOR_KW ID ASSIGN_OP expr TO_KW expr DO_KW stmt
            | RETURN_KW expr SEMICOLON
            | block'''
    if (len(p) == 5 or len(p) == 4) and p[2] == ':=':
        p[0] = (p[1], p[2], p[3])
    elif len(p) == 5 and p[1] == 'if':
        p[0] = (p[2], p[4])
    elif len(p) == 7 and p[1] == 'if':
        p[0] = (p[2], p[4], p[6])
    elif len(p) == 5 and p[1] == 'while':
        p[0] = (p[2], p[4])
    elif len(p) == 9 and p[1] == 'for':
        p[0] = (p[2], p[4], p[6], p[8])
    elif len(p) == 4 and p[1] == 'return':
        p[0] = p[2]
    elif len(p) == 2:
        p[0] = p[1]
    slice_to_production(p)

def p_expr(p):
    '''expr : expr AND_KW expr
            | expr OR_KW expr
            | expr MUL_OP expr
            | expr DIV_OP expr
            | expr ADD_OP expr
            | expr SUB_OP expr
            | expr relop expr
            | LEFT_PA expr RIGHT_PA
            | INTEGER_NUMBER
            | REAL_NUMBER
            | TRUE_KW
            | FALSE_KW
            | ID LEFT_PA actualparamlist RIGHT_PA
            | ID'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        if p[1] == '(':
            p[0] = p[2]
        else:
            p[0] = (p[1], p[2], p[3])
    slice_to_production(p)

def p_actualparamlist(p):
    '''actualparamlist : expr
                        | actualparamlist COMMA expr
                        | ID
                        | empty'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[3]
    elif len(p) == 4:
        p[0] = p[1] + p[3]
    else:
        pass
    slice_to_production(p)

def p_relop(p):
    '''relop : GT_OP 
            | GE_OP 
            | LT_OP 
            | LE_OP 
            | EQ_OP 
            | NE_OP'''
    p[0] = p[1]
    slice_to_production(p)

def p_empty(p):
    '''empty : '''
    p[0] = ''
    slice_to_production(p)

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc(debug=True)

# Add a list to store the production rules
productions_list = []

# Function to add the current production to the list
def slice_to_production(p):
    production = f"{p.slice[0]} ->"
    for item in p.slice[1:]:
        if isinstance(item, lex.LexToken):
            production += f" {item.type}"
        else:
            production += f" {item}"
    productions_list.append(production)