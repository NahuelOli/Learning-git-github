def run():



    palabra = input("Escriba una palabra o un numero: ")
    palabra = palabra.replace (" ", "")
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        print("Es capicua.")
    else:
        print("No es capicua.")



if __name__ == "__main__":
    run()