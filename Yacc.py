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

#...................... VARIABLES BOOLEANAS ............................................................

def p_VARIABLES_BOOLEANO(p):
    'declaracion_booleana : BOOL STRINGVAL ASSIGN booleano SEMICOLON'


def p_VALORES_BOOLEANAS(p):
    '''booleano : TRUE
                | FALSE'''

#...................... IMPRIMIR POR PANTALLA ............................................................

def p_IMPRIMR_PANTALLA(p):
    'imprimir : PRINT LPAREN opciones RPAREN SEMICOLON'

def p_OPCIONES_PANTALLA(p):
    '''opciones : LDQMARK STRINGVAL RDQMARK
                | STRINGVAL'''






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