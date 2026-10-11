from datetime import datetime


def es_palabra_valida(cadena: str) -> bool:
    if len(cadena.strip()) == 5 and cadena.isalpha():
        return True
    else:
        return False

def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple[int, float]:
    """Devuelve la diferencia entre dos datetime como minutos y segundos.

    Parámetros:
        inicio: datetime de inicio
        fin: datetime de fin
    Devuelve:
        Una tupla (minutos, segundos) con la diferencia entre ambos datetime.
    """
    tiempo_total = fin - inicio
    total_segundos = tiempo_total.total_seconds()
    tiempo_segundos = total_segundos % 60
    tiempo_minutos = int(total_segundos // 60)
    return (tiempo_minutos, tiempo_segundos)

def quitar_letra(cadena: str, caracter: str):
    res = ""
    borra = True
    for c in cadena:
        if c != caracter:
            res +=c
        else:
            if borra:
                borra = False
            else:
                res +=c
    return res


def marcar_verdes(palabra_secreta: str, intento: str) -> tuple[str, str]:
    cadena_verdes = ""
    cadena_restante = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == intento[i]:
            cadena_verdes += "V"
        else:
            cadena_verdes += "_"
            cadena_restante += palabra_secreta[i]
    return (cadena_verdes, cadena_restante)

def marcar_amarillos(intento: str, cadena_verdes: str, cadena_restante: str):
    colores = ""
    for i in range(len(intento)):
        if cadena_verdes[i] == "V":
            colores += "V"
        elif intento[i] in cadena_restante:
            colores += "A"
            cadena_restante.replace(intento[i], "")
        else:
            colores += "_"
    return colores


def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    cadena_verdes, cadena_restante = marcar_verdes(palabra_secreta, intento)
    colores = marcar_amarillos(intento, cadena_verdes, cadena_restante)
    return colores



