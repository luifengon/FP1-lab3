from datetime import datetime


def es_palabra_valida(cadena: str) -> bool:
    if len(cadena.strip()) == 5 and cadena.isalpha():
        return True
    else:
        return False

def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    tiempo_total = fin - inicio
    tiempo_segundos = tiempo_total.total_seconds() % 60
    tiempo_minutos = tiempo_total.total_seconds() //60
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


# TODO: Escribe la cabecera completa e implementa la función marcar_verdes

# TODO: Escribe la cabecera completa e implementa la función marcar_amarillos

def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    """
    Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
    Devuelve:
        Una cadena de 5 caracteres con 'V', 'A' y '_'
    """
    # TODO: Implementa esta función
    return "_____"  # Elimina esta línea cuando la implementes


