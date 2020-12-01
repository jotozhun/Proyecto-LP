import ply.yacc as yacc
import logging
from main import tokens, lexDefinition

#Expresiones matematicas


def p_sentencia(p):
    '''sentencia : cuerpo
                | cuerpo sentencia'''

def p_cuerpo(p):
    '''cuerpo : asignacion
            | expresion
            | comparacion
            | sentenciasConditional
            | sentenciasIterativas
            | funciones'''

def p_funciones(p):
    '''funciones : declararFunc 
                 | usarFunc'''

def p_declararFunc(p):
    '''declararFunc : VOID ID LPAREN RPAREN LBRACE cuerpoBloque RBRACE'''

def p_cuerpoBloque(p):
    '''cuerpoBloque : cuerpo
                    | cuerpo cuerpoBloque'''

def p_usarFunc(p):
    '''usarFunc : PRINT LPAREN STRINGVAL RPAREN SEMICOLON'''

def p_sentenciasConditional(p):
    '''sentenciasConditional : sentenciaif
                             | sentenciaelseif
                             | sentenciaelse'''

def p_sentenciaif(p):
    'sentenciaif : IF LPAREN comparacion RPAREN LBRACE cuerpoBloque RBRACE'

def p_sentenciaelseif(p):
    '''sentenciaelseif : ELSE IF LPAREN comparacion RPAREN LBRACE cuerpoBloque RBRACE'''

def p_sentenciaelse(p):
    '''sentenciaelse : ELSE LBRACE cuerpoBloque RBRACE'''

def p_sentenciasIterativas(p):
    '''sentenciasIterativas : sentenciafor
                            | sentenciawhile'''

def p_incremDecrem(p):
    '''incremDecrem : ID PLUS PLUS
                    | ID MINUS MINUS'''

def p_sentenciafor(p):
    '''sentenciafor : FOR LPAREN asignacion comparacion SEMICOLON incremDecrem RPAREN LBRACE cuerpoBloque RBRACE'''

def p_sentenciawhile(p):
    '''sentenciawhile : WHILE LPAREN comparacion RPAREN LBRACE cuerpoBloque RBRACE'''

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

inityacc = open("yaccErrors.txt", "w")
inityacc.close()
logging.basicConfig(filename="yaccErrors.txt", filemode="w", level=logging.DEBUG)
lexDefinition()
parser = yacc.yacc()




def analizadorSintactico(entrada):
    #parser = yacc.yacc()
    return str(parser.parse(entrada))
    #yaccResult = str(parser.parse(entrada))
    #return yaccResult
'''
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
    '''

f=open("algoritmo.txt")
s = f.read()
print(s)
result = parser.parse(s, tracking=True)
print(result)
f.close()
