from string import ascii_lowercase


def getNextLetterAlphabet(letter: str):
    try:
        if type(letter) == str and len(letter) == 1 and letter.isalpha():
            next_letter = letter.translate(
                str.maketrans(ascii_lowercase, ascii_lowercase[1:] + "a")
            )
            return next_letter
        else:
            raise Exception("Character has to be one letter from a to z")
    except Exception as incorrect_input_error:
        print("Incorrect input of letter:", incorrect_input_error)


# print(getNextLetterAlphabet("r"))
