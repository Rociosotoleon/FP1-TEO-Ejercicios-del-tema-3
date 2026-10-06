
def estiliza_mensaje(texto: str, alterna_may_min: bool = True, usa_dieresis = False, sustituye_espacios: str = True) -> str: 
    res = ""
    toca_mayusculas = True
    for caracter in texto:
        if c.isalpha() and alterna_may_min():
            if toca_mayuscula:
                c = c.upper()
            
            else:
                c = c.lower()
            toca_mayuscula = not toca_mayuscula
        
        
        res += c
        texto = res

    if usa_dieresis:
        texto = texto.replace("a", "ä").replace("e", "ë").replace("i", "ï").replace("o", "ö").replace("u", "ü")
        texto = texto.replace("A", "Ä").replace("E", "Ë").replace("I", "Ï").replace("O", "Ö").replace("U", "Ü")

    if sustituye_espacios:
        texto = texto.replace(" ", "*")

    return texto