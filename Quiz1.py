with open ("currency.txt", "r") as file_object:
    for line in file_object:
        key, sep, value = line.strip().partition(" ")
    return int(key), value
        

def readcurrency(currency.txt):
    print readcurrency
    