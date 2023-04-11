'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 '''
# se genera la funcion ingresando una variable
def hacker_translator(text):
 # se genera un diccionario con el valor de las letras
    leet = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
            "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
            "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"," ":" "}
  # se crea una variable la cual es una lista en donde se realiza un ciclo for para separar letras otro en donde se compara los items
  # del diccinario y si la letra coincide con la clave que guarde el valor 
    message = [value for letter in text for key,value in leet.items() if letter.upper() == key]
   # returna el valor descomprimido con la funcion map
    return " ".join(map(str, message))

# se imprime el mnesaje que se ingresa en la funcion 
print(hacker_translator("text proof that you encrypt messages"))
