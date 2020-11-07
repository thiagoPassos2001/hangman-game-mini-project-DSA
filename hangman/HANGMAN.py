# Hangman Game (Jogo da Forca) 
# Object Oriented Programming (Programação Orientada a Objetos)

# Import
import random

# Board (Tabuleiro)
board = ['''

>>>>>>>>>>HANGMAN<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
=========''']

# Method randomly reading a word from the word bank (Método para ler uma palavra de forma aleatória do banco de palavras)
def rand_word():

        with open("word_bank.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))]

# Class the Hangman Game (Classe do Jogo da Forca)
class Hangman:

    # init method (Método Construtor)
    def __init__(self, word):

        self.word = word.strip()
        self.missed_letters = []
        self.guessed_letters = []

    
    # Method that checks the current state of game (Método que checa o estado atual de jogo)
    def checkGame(self):

        current = 1

        for i in self.word:
            if i in self.guessed_letters:
                current *= 1
            else:
                current *= 0

        if len(self.missed_letters) == len(board)-1:
            current = 2

        return current

    # Method that prints the current state of game (Método que imprime o estado atual de jogo)
    def currentState(self):

        current = self.checkGame()

        if current == 1:

            print('Congratulations! You Win.')
            print('Correct word: ',end='')
            [print(i,end=' ') for i in self.word]
            print('\n')

            return current

        elif current == 2:

            print(board[len(self.missed_letters)])
            print('You lose!')

            return current
            
        else:

            print(board[len(self.missed_letters)])

            print('Missed Letters:')
            [print(i,end=' ') for i in self.missed_letters]
            print('\n')

            print('Guessed Letters:')
            [print(i,end=' ') for i in self.guessed_letters]
            print('\n')

            for i in self.word:
                if i in self.guessed_letters:
                    print(i, end=' ')
                else:
                    print('_', end=' ')

            return current

    # Method that receives the inserted letter (Método que recebe a letra inserida)
    def inputLetter(self, letter):

        letter = letter.upper()
        list_letter =  self.missed_letters + self.guessed_letters

        if not letter in list_letter:

            if len(letter) > 1:
                print('Enter only one letter!')
            elif letter in self.word:
                self.guessed_letters.append(letter)
                print('"{}" Correct letter!'.format(letter))
            else:
                self.missed_letters.append(letter)
                print('"{}" Wrong letter!'.format(letter))

        else:
            print('Letter already inserted. Try again!')

# Method Main - Execution the game (Método Main - Execução do jogo)
def main():

    game = Hangman(rand_word().upper())
    game.currentState()
    print('\n')

    while game.checkGame() == 0:
        new_letter = input('| New letter: ')
        game.inputLetter(new_letter)
        game.currentState()

    print('End Game')

# Starting (Iniciando)		
if __name__ == "__main__":
    main()