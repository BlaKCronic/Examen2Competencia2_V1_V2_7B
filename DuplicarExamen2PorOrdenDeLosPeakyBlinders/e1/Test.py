from antlr4 import *
from ExprLexer import ExprLexer
import sys


def obtener_nombre_token(lexer, token):
    if token.type == -1:
        return "<EOF>"

    nombres = {
        lexer.ID: "ID",
        lexer.NUMBER: "NUMBER",
        lexer.STRING: "STRING",
        lexer.WS: "WS",
    }

    if token.type in nombres:
        return nombres[token.type]

    if 0 <= token.type < len(lexer.literalNames):
        nombre = lexer.literalNames[token.type]
        if nombre != "<INVALID>":
            return nombre

    return "TOKEN"


def detectar_estructuras(texto):
    estructuras = []
    if "public static void main" in texto:
        estructuras.append("Método main")
    if "System.out.println" in texto:
        estructuras.append("Impresiones con System.out.println")
    if "Scanner" in texto and "new Scanner" in texto:
        estructuras.append("Lectura de datos con Scanner")
    for tipo in ["int", "double", "String", "Boolean", "boolean", "int[]", "double[]", "String[]"]:
        if tipo in texto:
            estructuras.append(f"Variable de tipo {tipo}")
    if "class " in texto and "public class" in texto:
        estructuras.append("Clase principal")
    if "get" in texto and "set" in texto:
        estructuras.append("Getters and setters")
    for ciclo in ["for (", "while (", "do {"]:
        if ciclo in texto:
            estructuras.append(f"Ciclo detectado: {ciclo.strip()}")
    return estructuras


if len(sys.argv) < 2:
    print("Uso: py Test.py <archivo.java>")
    sys.exit(1)

ruta = sys.argv[1]
with open(ruta, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

print("Análisis de estructuras Java")
print("-" * 40)
for estructura in detectar_estructuras(texto):
    print("[OK]", estructura)

print("-" * 40)
print("Tokens del archivo:")

input_stream = FileStream(ruta)
lexer = ExprLexer(input_stream)
tokens = CommonTokenStream(lexer)
tokens.fill()

for token in tokens.tokens:
    print("Texto :", token.text)
    print("Linea :", token.line)
    print("Columna :", token.column)
    print("Tipo :", obtener_nombre_token(lexer, token))
    print("----------------------")