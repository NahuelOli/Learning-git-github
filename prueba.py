def run():
    print("""
    Bienvenido a 'Es capicua?'
    """)
    palabra = input("Escriba una palabra o un numero: ")
    palabra = palabra.replace (" ", "")
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        print("Es capicua.")
    else:
        print("Es capicua.")
    
    
    print("""
    Bienvenido a 'par o impar'
    """)
    numero = int(input("Escribe un numero: "))
    if numero % 2 == 0:
        print("El numero " + str(numero) + " es par.")
    else:
        print("El numero " + str(numero) + " es impar.")


if __name__ == "__main__":
    run()