import random
# Lista de palabras posibles
words = ["python", "programacion", "computadora", "código", "desarrollo",
"inteligencia"]
def set_secret_word(difficulty):
    # Elegir una palabra al azar
    secret_word = random.choice(words)
    if difficulty == "facil":
        # Mostrar todas las vocales
        vocales = "aeiou"
        word_displayed ="".join([letter if letter in vocales else "_" for letter in secret_word])
        guessed_letters.extend([letter for letter in word_displayed if letter != "_" and letter.isalpha()])
    elif difficulty == "medio":
        # Mostrar la primera y última letra
        word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
        guessed_letters.extend([secret_word[0], secret_word[-1]])
    elif difficulty == "dificil":
         #No mostrar ninguna letra
         word_displayed = "_" * len(secret_word)
    return secret_word, word_displayed
# Función para solicitar al usuario el nivel de dificultad
def select_difficulty():
    exit=True
    while exit:
        difficulty = input("Selecciona el nivel de dificultad (facil, medio, dificil): ").lower()
        if difficulty in ["facil", "medio", "dificil"]:
            exit=False
            return difficulty
        else:
            print("Nivel de dificultad no válido. Por favor, selecciona entre facil, medio o dificil.")
# Elegir el nivel de dificultad
difficulty = select_difficulty()
# Lista para almacenar las letras adivinadas
guessed_letters = []
# Establecer la palabra a adivinar según el nivel de dificultad
secret_word, word_displayed = set_secret_word(difficulty)
# Número máximo de fallos permitidos
max_fails = 10
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
i=1
while i <= max_fails:   
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     # Verificar si la letra ya ha sido adivinada
     if letter == "":
         print("Error:Esa no es una letra")
         continue
     else:
        if letter in guessed_letters:
            print("Ya has intentado con esa letra. Intenta con otra.")
            continue
        # Agregar la letra a la lista de letras adivinadas
        guessed_letters.append(letter)
        # Verificar si la letra está en la palabra secreta
        if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
        # Mostrar la palabra parcialmente adivinada
        letters = []
        for letter in secret_word:
             if letter in guessed_letters:
                 letters.append(letter)
             else:
                 letters.append("_")
        word_displayed = "".join(letters)
        print(f"Palabra: {word_displayed}")
        # Verificar si se ha adivinado la palabra completa
        if word_displayed == secret_word:
            print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
            break
     i+=1   
else:
     print(f"¡Oh no! Has agotado tus {max_fails} intentos.")
     print(f"La palabra secreta era: {secret_word}")