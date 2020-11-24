"""
import ply.yacc as yacc

#Importar los tokens
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

#...................... VARIABLES BOOLEANAS ............................................................Andres Morales

def p_VARIABLES_BOOLEANO(p):
    'declaracion_booleana : BOOL STRINGVAL ASSIGN booleano SEMICOLON'


def p_VALORES_BOOLEANAS(p):
    '''booleano : TRUE
                | FALSE'''

#...................... IMPRIMIR POR PANTALLA ............................................................ Andres Morales 

def p_IMPRIMR_PANTALLA(p):
    'imprimir : PRINT LPAREN opciones RPAREN SEMICOLON'

def p_OPCIONES_PANTALLA(p):
    '''opciones : LDQMARK STRINGVAL RDQMARK
                | STRINGVAL'''


def p_TIPO_ARREGLOS(p):
    '''tipo : NUM
            | INT
            | STRING
            | DOUBLE
            | VAR
            | DYNAMIC'''

def p_AGREGAR_VALOR(p):
    'agregar : STRINGVAL PUNTO ADD LPAREN LDQMARK ID RDQMARK RPAREN SEMICOLON'

def p_DECLARA_LISTA(p):
    'lista : LIST LESSTHAN tipo MORETHAN STRINGVAL SEMICOLON'

def p_DECLARA_CONJUNTOS(p):
    'conjuntos : SET STRINGVAL ASSIGN NEW SET LPAREN RPAREN SEMICOLON'

#def p_DECLARA_MAPAS(p):
#    'mapa : MAP LESSTHAN tipo COMA tipo MORETHAN STRINGVAL ASSIGN LBRACE LDQMARK ID RDQMARK COMA valor RBRACE SEMICOLON'

#...................... IF ............................................................

def p_CONDICIONAL(p):
    'if : IF LPAREN ID opcionesIf valor RPAREN LBRACE  RBRACE SEMICOLON'

def p_OPCIONES_IF(p):
    '''opcionesIf : LESSTHAN
                  | MORETHAN
                  | GQUAL
                  | LQUAL
                  | NOTEQUALS
                  | EQUALS'''



#...................... CODIGO DE VERIFICACION .........................................................................
parser = yacc.yacc()
"""
import ply.yacc as yacc

from main import tokens

def p_expression_plus(p):
     'expression : expression PLUS term'
     p[0] = p[1] + p[3]
 
 def p_expression_minus(p):
     'expression : expression MINUS term'
     p[0] = p[1] - p[3]
 
 def p_expression_term(p):
     'expression : term'
     p[0] = p[1]
 
 def p_term_times(p):
     'term : term TIMES factor'
     p[0] = p[1] * p[3]
 
 def p_term_div(p):
     'term : term DIVIDE factor'
     p[0] = p[1] / p[3]
 
 def p_term_factor(p):
     'term : factor'
     p[0] = p[1]
 
 def p_factor_num(p):
     'factor : NUMBER'
     p[0] = p[1]
 
 def p_factor_expr(p):
     'factor : LPAREN expression RPAREN'
     p[0] = p[2]
 
 # Error rule for syntax errors
 def p_error(p):
     print("Syntax error in input!")
 
 # Build the parser
 parser = yacc.yacc()
 
 while True:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
