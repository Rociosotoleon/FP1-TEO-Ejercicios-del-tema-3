
def es_palindromo(texto: str, ignora_espacios: bool = True, ignora_mayusculas: bool = True) -> bool:
    ''' 
    Devuelve True si el texto recibido es un palíndromo

    Paámetros:
    texto (str): el texto que queremos saber si es palindromo
    ignora_mayusciñas(bool) : si es True, se ignoran las mayúsculas 
    '''
    if ignora_espacios:
        texto = texto.replace(" ", "")

    if ignora_mayusculas:
        texto = texto.lower()
    
    res = ""
    for c in texto:
        res = c + res 

    
    return texto == res
