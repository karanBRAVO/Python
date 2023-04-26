import random


def intro():
    print('****** Welcome to MASTERMIND ******')
    print(
        '~ you have to guess the 4-digit code using the colours [B R O Y G V W]')
    print('~ you have 10 tries')
    print("~ every character must be in uppercase")


def getCode():
    color = ['B', 'R', 'O', 'Y', 'G', 'V', 'W']
    code = ""
    i = 1
    while i <= 4:
        index = random.randint(0, len(color) - 1)
        code += color[index]
        i += 1
    return code


def printRes(corr_pos, incorr_pos, count):
    print(
        f'correct position: {corr_pos} || incorrect position: {incorr_pos} || tries left: {count}')


def mainGame():
    totalTries = 10
    code = getCode()
    print('testing only: ', code)
    for i in range(0, totalTries, 1):
        guessCode = input(f"{i+1}.) Guess code: ")
        tryLeft = 10 - (i + 1)
        if guessCode == code:
            printRes(4, 0, tryLeft)
            print('you guessed it correctly.')
            break
        else:
            corrPos = 0
            incorrPos = 0
            for index in range(0, len(code)):
                if guessCode[index] == code[index]:
                    corrPos += 1
                elif guessCode[index] != code[index]:
                    for c_index in range(0, len(code)):
                        if guessCode[index] == code[c_index]:
                            if guessCode[c_index] != code[c_index]:
                                incorrPos += 1
            printRes(corrPos, incorrPos, tryLeft)
            if tryLeft == 0:
                print('OOPS! you loose.')


if __name__ == "__main__":
    intro()
    mainGame()
