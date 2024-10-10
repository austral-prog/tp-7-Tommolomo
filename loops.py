def index_of_by_index(word, lista, index):
    for i in range(index, len(lista)):
        if lista[i] == word:
            return i
    return -1

def index_of_empty(lista):
    for i in range(len(lista)):
        if lista[i] == "":
            return i
    return -1

def index_of(word, lista):
    for i in range(len(lista)):
        if lista[i] == word:
            return i
    return -1

def put(word, lista):
    for index, value in enumerate(lista):
        if value == "":
            lista[index] = word
            return index
    return -1


def remove(word, lista):
    count = 0
    for index, value in enumerate(lista):
        if value == word:
            lista[index] = ""
            count += 1
    return count
