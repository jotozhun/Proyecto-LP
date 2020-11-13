import ply.lex as lex

reserved = {
    'num':'NUM',
    'int':'INT',
    'double':'DOUBLE',
    'bool': 'BOOL',
    'var':'VAR',
    'string':'STRING',
    'dynamic': 'DYNAMIC',
    'if':'IF',
    'else':'ELSE',
    'for':'FOR',
    'while':'WHILE',
    'List':'LIST',
    'Map':'MAP',
    'Set':'SET'
}

tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

t_ignore = ' \t'

def t_error(t):
    print('Illegal character "%s"' %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = """
MAP<int> for efe
"""
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)