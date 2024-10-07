import re

def guion(texto: str) -> str:
    patron = r"(.{2})(.{6})"
    reemplazo = r"\1-\2-"
    cadena_modificada = re.sub(patron, reemplazo, texto)
    return cadena_modificada.upper()