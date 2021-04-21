def run():
   
   
    palabra = input("Escriba una palabra: ")
    palabra = palabra.replace (" ", "")
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        print("Es .")
    else:
        print("No es .")



if __name__ == "__main__":
    run()