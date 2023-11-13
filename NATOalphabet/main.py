import pandas

phonetics = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics = {row.letter: row.code for (index, row) in phonetics.iterrows()}


def make_nato():

    my_message = input("Enter your name: ").upper()
    letters_of_message = list(my_message)

    try:
        nato_message = [phonetics[letter] for letter in letters_of_message]
    except KeyError:
        print("You have entered an invalid character, which cannot be converted, please enter valid characters")
        make_nato()
    else:
        print(nato_message)


make_nato()