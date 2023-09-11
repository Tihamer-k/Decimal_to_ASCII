import re
import math
from colorama import Fore, Style


def decimal_base_transform(num, base):
    # Se declaran variables en limpio para inicio de la función
    list_pow = []
    list_res = []

    # Obtenemos total dígitos del número
    digits = int(math.log10(num)) + 1

    # Obtenemos los resultados de la base por el exponente de acuerdo a la cantidad de dígitos del número
    for i in range(digits):
        list_pow.append(pow(base, i))
    # Invertimos orden de la lista obtenida
    list_pow.reverse()

    # Obtenemos una lista con los dígitos del número
    list_of_digits = [int(i) for i in str(num)]

    # Multiplicamos la lista de (base * exponente) * cada dígito del número
    for i in range(digits):
        list_res.append(list_pow[i] * list_of_digits[i])

    decimal_num = sum(list_res)  # Sumamos todos los datos de la lista

    # Convertimos el resultado de la lista a ASCII con la función chr()
    ascii_chr = chr(decimal_num)

    print(f"{num} con base {base} => sistema decimal: {decimal_num} => ASCII: {ascii_chr}")


def valid_input(input_text):
    regexp = r'^\d+\d+|(s|n)'
    if re.match(regexp, input_text):
        return re.search(regexp, input_text)


def valid_entry(data, id_option):
    x = False
    while not x:
        input_txt = valid_input(data)
        if input_txt:
            return data
        else:
            print("\n¡Formato de entrada no es correcto!" + Fore.RED + f" ({data})\n")
            if id_option == 1:
                print("Debe iniciar el número y su base separado con un '-'. ")
            elif id_option == 2:
                print("Debe indicar 's' para SÍ o 'n' para NO. ")
            data = input(Style.RESET_ALL + "\nIntenta de nuevo:\n")
