import ply.lex as lex

tokens = [
    'STRINGVAL',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'COMMA',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LESSTHAN',
    'MORETHAN',
    'ASSIGN',
    'ID',
]

reserved = {
    'num':'NUM',
    'int':'INT',
    'double':'DOUBLE',
    'bool': 'BOOL',
    'true':'TRUE',
    'false':'FALSE',
    'var':'VAR',
    'String':'STRING',
    'dynamic': 'DYNAMIC',
    'if':'IF',
    'else':'ELSE',
    'for':'FOR',
    'while':'WHILE',
    'List':'LIST',
    'Map':'MAP',
    'Set':'SET'
}

tokens += list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
#t_STRINGVAL = r'(^\'[^\']*\'$|^\"[^\']*\"$)'
t_ASSIGN = r'='
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LESSTHAN = r'<'
t_MORETHAN = r'>'
t_COMMA = r','
t_SEMICOLON = r';'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    #r'\d+'
    r'[+-]?\d + (\.\d+)?'
    return t

def t_STRINGVAL(t):
    r'"{1}([^\\"]|\\(.|\n))*"{1}'
    t.lexer.lineno += t.value.count("\n")
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

file = open("archivo.txt")

for line in file:
    lexer.input(line)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)