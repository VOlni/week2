
def hangman(word, letters):
    words = word
    for letter in words:
        if letter not in letters:
            letter = ' _ '
    return print(words)



hangman('python', ['a', 'r', 'y', 'i', 'o'])