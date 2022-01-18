''' os para limpiar pantalla, random para usar el metodo choise y elegir una palabra al asar'''
import os
import random


def clean_screen():
    '''
        funcion para limpiar la pantalla en cada iteracion del juego
        usa la libreria os
        no retorna ningun valor
    '''
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def select_secret_word():
    '''
        trae de un archivo externo una lista de palabras que seran las usadas en el juego
        selecciona una palabra al asar utilizando el metodo choice de la libreria random
    '''
    list_words = []
    with open("./files/hangman_data.txt", "r", encoding='utf-8') as f:
        for line in f:
            list_words.append(line)
    secret_word = (random.choice(list_words)).strip('\n')

    return secret_word


def paint_screen(num_paint):
    '''dibuja la pantalla del aorcado
    toma como argumento un nivel
    donde 1 es inicio y 7 es la ultima oportunidad del jugador
    '''
    if num_paint == 1:

        print('''
     **THE HANGMAN****

        +---+
      |   |
          |
          |
          |
          |
    =========
        ''')
    elif num_paint == 2:
        print('''
    **THE HANGMAN****
       +---+
      |   |
      O   |
          |
          |
          |
    =========
        ''')
    elif num_paint == 3:
        print('''
    **THE HANGMAN****
        +---+
      |   |
      O   |
      |   |
          |
          |
    =========
        ''')
    elif num_paint == 4:
        print('''
    **THE HANGMAN****
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
        ''')
    elif num_paint == 5:
        print('''
    **THE HANGMAN****
     +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
        ''')
    elif num_paint == 6:
        print('''
    **THE HANGMAN****
     +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
        ''')
    elif num_paint == 7:
        print('''
    **THE HANGMAN****
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
        ''')


def run():
    win = False
    win_word = []
    secret_word = select_secret_word()
    print(secret_word)  # REVICION **************************
    attempts = 1
    paint_screen(attempts)
    # dibuja el tablero
    num_letters = len(secret_word)
    print(num_letters)  # REVICION******************************
    board = ['_'] * num_letters
    for casilla in board:
        print(casilla, end=' ')
    while attempts < 6 and win ==  False:
        player_letter = input('\n\n\nIngrese una letra: ')
        if player_letter in secret_word:
            for idx, letter_word in enumerate(secret_word):
                if player_letter == letter_word:
                    board[idx] = player_letter
                    win_word.insert(idx, player_letter)
                    if len(win_word) == num_letters:
                        win = True
                        clean_screen()
                        break
                    clean_screen()
                    paint_screen(attempts)            
                    for casilla in board:
                        print(casilla, end=' ')

        else:
            attempts = attempts +1
            clean_screen()
            print(f'fallaste!! tienes: {attempts} intentos')
            paint_screen(attempts)


    if win == True:
        print(f'¡¡¡¡Haz Ganado!!!!!{secret_word}')
    else:
        clean_screen()
        print(f'PERDISTE!!!!')
        paint_screen(7)


if __name__ == '__main__':
    run()
