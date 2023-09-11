from util import decimal_base_transform, valid_entry

if __name__ == '__main__':
    entry = 's'
    while entry == 's':
        entry = valid_entry(input("Ingrese el número y su base separado con un '-': "), 1)
        value = entry.split("-")
        a = int(value[0])
        b = int(value[1])
        decimal_base_transform(a, b)
        entry = valid_entry(input("¿Desea continuar? [s|n]"), 2)
