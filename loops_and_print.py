def enumerate_list(lista):
    lista_enu = []
    indice = 0
    for string in lista:
        if string:
            lista_enu.append(f"{indice}. {string}")
            indice = indice + 1
    return lista_enu

def enumerate_backwards(lista2):
    lista_enu2 = []
    indice = 0
    for string in lista2:
        if string:
            string_rev = string[::-1]
            lista_enu2.append(f"{indice}. {string_rev}")
            indice = indice + 1
    return lista_enu2
