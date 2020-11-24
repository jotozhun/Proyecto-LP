import ply.yacc as yacc

from main import tokens

#Expresiones matematicas


def p_cuerpo(p):
    '''cuerpo : asignacion
            | expresion
            | comparacion
            | sentenciaif
            | funciones'''

def p_funciones(p):
    '''funciones : declararFunc 
                 | usarFunc'''

def p_declararFunc(p):
    '''declararFunc : VOID ID LPAREN RPAREN LBRACE cuerpo RBRACE'''

def p_usarFunc(p):
    '''usarFunc : PRINT LPAREN STRINGVAL RPAREN SEMICOLON'''

def p_sentenciaif(p):
    'sentenciaif : IF LPAREN comparacion RPAREN COLON cuerpo'

def p_asignacion(p):
    '''asignacion : asignacionNumerica 
                  | asignacionString
                  | asignacionBoolean
                  | asignacionEstructuraDatos'''

def p_asignacionEstructuraDatos(p):
    '''asignacionEstructuraDatos : asignacionList
                                 | asignacionSet
                                 | asignacionMap'''

def p_asignacionList(p):
    '''asignacionList : LIST LESSTHAN tipoPrimitivo MORETHAN ID SEMICOLON'''

def p_asignacionSet(p):
    '''asignacionSet : SET ID ASSIGN NEW SET LPAREN RPAREN SEMICOLON'''

def p_asignacionMap(p):
    '''asignacionMap : MAP LESSTHAN tipoPrimitivo COMMA tipoPrimitivo MORETHAN ID SEMICOLON'''


 #Asignacion


 # Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
