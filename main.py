import ply.lex as lex

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
    'add':'ADD',
    'Map':'MAP',
    'Set':'SET',
    'print':'PRINT',
    'new':'NEW',
    'void':'VOID'
}

tokens = [
    'STRINGVAL',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'COMMA',
    'PUNTO',
    'SEMICOLON',
    'COLON',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LESSTHAN',
    'MORETHAN',
    'ASSIGN',
    'ID',
    'LDQMARK',
    'RDQMARK',
    'SQMARK',
    'GQUAL',
    'LQUAL',
    'EQUALS',
    'NOTEQUALS'
]

tokens += list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
#t_STRINGVAL = r'(^\'[^\']*\'$|^\"[^\']*\"$)'
t_ASSIGN = r'='
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LESSTHAN = r'<'
t_MORETHAN = r'>'
t_COMMA = r','
t_COLON = r':'
t_SEMICOLON = r';'
t_LDQMARK = r'\“'
t_RDQMARK = r'\”'

t_GQUAL = r'\>\='
t_LQUAL = r'\<\='
t_EQUALS = r'\=\='
t_NOTEQUALS = r'\!\='
t_PUNTO = r'\.'



def t_ID(t):
    r'[a-z_][a-zA-Z0-9_]*'
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


def lexAnalizer(texto):
    lexer.input(texto)
    result = ""
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        result += (str(tok) + "\n")
    return result

lexer = lex.lex()

print(lexAnalizer("Ya pues mi prro quedate fresco"))
'''
file = open("archivo.txt", encoding="utf8")

for line in file:
    lexer.input(line)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
'''
#Analizador Sintactico.................................................
