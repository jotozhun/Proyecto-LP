import ply.yacc as yacc

#Importar los toquens
from main import tokens

#......................OPERACIONES MATEMATICAS............................................................
def p_VARIABLES_NUMEROS(p):
    '''declarNum : NUM
                | INT
                | DOUBLE
                | VAR
                | DYNAMIC'''

def p_DECLARAR_NUMEROS(p):
    'resultado : declarNum STRINGVAL ASSIGN NUMBER SEMICOLON'

def p_VALOR(p):
    '''valor : NUMBER
             | ID'''

def p_SUMA(p):
    'resultado : valor PLUS valor SEMICOLON'

def p_RESTA(p):
    'resultado : valor MINUS valor SEMICOLON'

def p_MULTIPLIACION(p):
    'resultado : valor TIMES valor SEMICOLON'

def p_DIVISION(p):
    'resultado : valor DIVIDE valor SEMICOLON'

#...................... STRINGS .........................................................................

def p_STRING(p):
    'string : declarar STRINGVAL SEMICOLON'

def p_STRING_DECLARAR(p):
    '''declarar : VAR
                | STRING
                | DYNAMIC'''

#...................... CODIGO DE VERIFICACION .........................................................................
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)