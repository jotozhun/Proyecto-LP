import ply.yacc as yacc
import logging
from main import *

lista=[]
data='''int x;;'''
#Expresiones matematicas


def p_sentencia(p):
    '''sentencia : cuerpo
                | cuerpo sentencia
                | declararFuncMultiple'''

def p_cuerpo(p):
    '''cuerpo : asignacion
            | expresionMat
            | expresionComp
            | sentenciasConditional
            | sentenciasIterativas
            | usarFunc'''

def p_declararFuncMultiple(p):
    '''declararFuncMultiple : declararFunc
                            | declararFunc declararFuncMultiple'''

def p_declararFunc(p):
    '''declararFunc : declararFuncNoArgs
                    | declararFuncArgs'''

def p_declararFuncArgs(p):
    '''declararFuncArgs : VOID ID LPAREN funcArgumentos RPAREN LBRACE cuerpoBloque RBRACE'''

def p_funcArgumentos(p):
    '''funcArgumentos : argumento
                      | argumento COMMA funcArgumentos'''

def p_argumentos(p):
    '''argumento : asignacionNum
                 | asignacionStr'''

def p_declararFuncNoArgs(p):
    '''declararFuncNoArgs : VOID ID LPAREN RPAREN LBRACE cuerpoBloque RBRACE'''

def p_cuerpoBloque(p):
    '''cuerpoBloque : cuerpo
                    | cuerpo cuerpoBloque'''

def p_usarFunc(p):
    '''usarFunc : PRINT LPAREN STRINGVAL RPAREN SEMICOLON
                | PRINT LPAREN NUMBER RPAREN SEMICOLON
                | PRINT LPAREN ID RPAREN SEMICOLON'''

def p_sentenciasConditional(p):
    '''sentenciasConditional : sentenciaif
                             | sentenciaif anidadaelseif
                             | sentenciaif sentenciaelse'''
def p_anidadaelseif(p):
    '''anidadaelseif : sentenciaelseif
                    |   sentenciaelseif anidadaelseif
                    |   sentenciaelseif sentenciaelse'''


def p_sentenciaif(p):
    'sentenciaif : IF LPAREN expresionComp RPAREN LBRACE cuerpoBloque RBRACE'

def p_sentenciaelseif(p):
    '''sentenciaelseif :  ELSE IF LPAREN expresionComp RPAREN LBRACE cuerpoBloque RBRACE'''

def p_sentenciaelse(p):
    '''sentenciaelse :  ELSE LBRACE cuerpoBloque RBRACE'''


#def p_operacionesVariables(p):
 #   'operacionesVariables : ID PLUS ID SEMICOLON'

def p_sentenciasIterativas(p):
    '''sentenciasIterativas : sentenciafor
                            | sentenciawhile'''

def p_incremDecrem(p):
    '''incremDecrem : ID PLUS PLUS
                    | ID MINUS MINUS'''

def p_sentenciafor(p):
    '''sentenciafor : FOR LPAREN asignacion expresionComp SEMICOLON incremDecrem RPAREN LBRACE cuerpoBloque RBRACE'''

def p_sentenciawhile(p):
    '''sentenciawhile : WHILE LPAREN expresionComp RPAREN LBRACE cuerpoBloque RBRACE'''

def p_asignacion(p):
    '''asignacion : asignacionNumerica SEMICOLON
                  | asignacionString SEMICOLON
                  | asignacionBoolean SEMICOLON
                  | asignacionEstructuraDatos SEMICOLON'''

def p_asignacionEstructuraDatos(p):
    '''asignacionEstructuraDatos : asignacionList
                                 | asignacionSet
                                 | asignacionMap'''

def p_asignacionList(p):
    '''asignacionList : LIST LESSTHAN tipoPrimitivo MORETHAN ID'''

def p_asignacionSet(p):
    '''asignacionSet : SET ID ASSIGN NEW SET LPAREN RPAREN'''

def p_asignacionMap(p):
    '''asignacionMap : MAP LESSTHAN tipoPrimitivo COMMA tipoPrimitivo MORETHAN ID'''

def p_asignacionBoolean(p):
    '''asignacionBoolean : BOOL ID ASSIGN expresionBoolean'''

def p_asignacionNumerica(p):
    '''asignacionNumerica : asignacionNum
                          | asignacionNumInit'''

def p_asignacionNum(p):
    '''asignacionNum : tipoNumeric ID'''

def p_asignacionNumInit(p):
    '''asignacionNumInit : tipoNumeric ID ASSIGN expresionMat
                            | ID ASSIGN expresionMat'''

def p_asignacionString(p):
    '''asignacionString : asignacionStr
                        | asignacionStrInit'''

def p_asignacionStr(p):
    'asignacionStr : tipoString ID'

def p_asignacionStrInit(p):
    'asignacionStrInit : tipoString ID ASSIGN expresionString'

def p_expresionString(p):
    '''expresionString : STRINGVAL'''

def p_comparacion(p):
    'expresionComp : valor operadoresComp valor'

def p_expresion_matematica(p):
    '''expresionMat : valor operadoresMat valor
                    | valor'''

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
    print(p)
    lista.append("Errores sintacticos " + str(p) + "\n")


for i in lista:
    print(i)

# Build the parser
#inityacc = open("yaccErrors.txt", "w")
#inityacc.close()
lexDefinition()
parser = yacc.yacc()

#parser = yacc.yacc()
def analizadorSintactico(entrada):
    yaccResult = parser.parse(entrada, tracking=True)
    #yaccResult = str(p)
    print(yaccResult)
    return yaccResult

#logging.basicConfig(filename="yaccResult.txt", filemode="w", level=logging.ERROR)
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

#f=open("algoritmo.txt")
#s = f.read()
#print(s)
result = parser.parse(data, tracking=True)
print(lista)
#f.close()