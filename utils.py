import unidecode

def lowercase(string):
    return string.lower()

def deaccent(string):
    return unidecode.unidecode(string)