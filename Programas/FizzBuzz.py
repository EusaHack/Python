'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 '''
# se genera funcion y se agrega variable
def fizz_buzz (number_end):
 # se realiza un ciclo for con rango iniciando en 1 hasta el numero de la variable + 1 
    for number in range(1,number_end+1):
   # se genera una condicion en donde si el numero al dividirlo entre 3 y 5 dan de residuo 0 imprima fizzzbuzz
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
      # se realiza otra condicion indicando si el numero al dividirlo entre 3 da de residuo 0 imprima fizz
        elif number % 3 == 0:
            print("fizz")
      # se realiza otra condicion indicando si el numero al dividirlo entre 5 da de residuo 0 imprima buzz  
        elif number % 5 == 0:
            print("buzz")
      # de no cumplir cualquier condicion imprima el numero
        else:
            print(number)

# se invoca la fucncion ingresando el valor de la variable          
fizz_buzz(100)
