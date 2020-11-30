import ply.yacc as yacc
import logging
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

def p_asignacionBoolean(p):
    '''asignacionBoolean : BOOL ID ASSIGN expresionBoolean SEMICOLON'''

def p_asignacionNumerica(p):
    'asignacionNumerica : tipoNumeric ID ASSIGN expresion SEMICOLON'

def p_asignacionString(p):
    'asignacionString : tipoString ID ASSIGN expresionString SEMICOLON'

def p_expresion(p):
    '''expresion : valor'''

def p_expresionString(p):
    '''expresionString : STRINGVAL'''

def p_comparacion(p):
    'comparacion : valor operadoresComp expresion'

def p_expresion_matematica(p):
    'expresion : valor operadoresMat expresion'

def p_expresionBoolean(p):
    '''expresionBoolean : TRUE
                        | FALSE'''

def p_operadoresMat(p):
    '''operadoresMat : MINUS
                    | PLUS
                    | TIMES
                    | DIVIDE'''

def p_operadoresComp(p):
    '''operadoresComp : MORETHAN
                        | LESSTHAN
                        | GQUAL
                        | LQUAL
                        | NOTEQUALS
                        | EQUALS'''

def p_valor(p):
    '''valor : NUMBER
             | ID'''

def p_tipoPrimitivo(p):
    '''tipoPrimitivo : tipoNumeric
                     | tipoString'''

def p_tipoNumeric(p):
    '''tipoNumeric : NUM
                   | INT
                   | DOUBLE'''

def p_tipoString(p):
    '''tipoString : STRING
                  | VAR
                  | DYNAMIC'''
 #Asignacion


 # Error rule for syntax errors
def p_error(p):
    logging.debug("Syntax error in input!")
    print("Syntax error in input!")

# Build the parser


logging.basicConfig(filename="yaccErrors.txt", filemode="w", level=logging.DEBUG)
#parser = yacc.yacc()



def analizadorSintactico(entrada):
    parser = yacc.yacc()
    return str(parser.parse(entrada))
    #yaccResult = str(parser.parse(entrada))
    #return yaccResult

"""
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)


f=open("algoritmo.txt")
s = f.read()
print(s)
result = parser.parse(s)
print(result)
f.close()
"""