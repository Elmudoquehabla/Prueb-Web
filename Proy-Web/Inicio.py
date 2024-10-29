#Este es un comentario que no será interpretado como comando
print ("Hola, Contosoville!")
#Asocioso la variable town con el valor "Contosoville"
town = "Contosoville"
#Imprimo un mensaje sobre la ubicación secreta
print ("El pueblo que busco es " + town)
# Definir un poder (función) para cantar una frase.
def chant( phrase ):
    # Pegue tres copias e imprímalas como un mensaje.
    print( phrase + phrase + phrase )
#Invoca el poder de cantar la frase "¡Contosoville!"
chant( "Contosoville!" )
print ("-------------------------------")
# Defina una función para encontrar la verdad desplazando la letra en una cantidad específica
def lasso_letter( letter, shift_amount ):
    # Invocar la función ord para traducir la letra a su código ASCII 
    # Guarde el valor del código en la variable llamada letter_code
    letter_code = ord(letter.lower())

    # La representación numérica ASCII de la letra minúscula a
    a_ascci = ord('a')

    # El número de letras del alfabeto.
    alphabet_size = 26

    # La fórmula para calcular el número ASCII de la letra decodificada
    # Tenga en cuenta recorrer el alfabeto
    true_letter_code = a_ascci + (((letter_code - a_ascci) + shift_amount) % alphabet_size)

    # Convierte el número ASCII al carácter o letra
    decoded_letter = chr(true_letter_code)
    
    # Devuelve la carta decodificada
    return decoded_letter

# Definir una función para encontrar la verdad en un mensaje secreto
# Cambie las letras de una palabra en una cantidad específica para descubrir la palabra oculta
def lasso_word( word, shift_amount ):

    # Esta variable se actualiza cada vez que se decodifica otra letra.
    decoded_word = ""

    # Este bucle for itera a través de cada letra en el parámetro de palabra.
    for letter in word:
        # La función lasso_letter() se invoca con cada letra y la cantidad de turno
        # El resultado (la letra decodificada) se almacena en una variable llamada decoded_letter
        decoded_letter = lasso_letter(letter, shift_amount)

        # El valor decoded_letter se agrega al final del valor decoded_word
        decoded_word = decoded_word + decoded_letter

    # EL decoded_word se envía de vuelta a la línea de código que invocó esta función.
    return decoded_word

# Se decodifica el mensaje secreto entregado
print( "Cambiar Ncevy por 13 da: \n" + lasso_word( "Ncevy", 13 ) )
print( "Cambiar gpvsui por 25 da: \n" + lasso_word( "gpvsui", 25 ) )
print( "Cambiar ugflgkg por -18 da: \n" + lasso_word( "ugflgkg", -18 ) )
print( "Cambiar wjmmf por -1 da: \n" + lasso_word( "wjmmf", -1 ) )