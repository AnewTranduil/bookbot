def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    print(text)
    words_count = count_words(text)
    print(words_count)
    letters = count_letters(text)
    print(letters)


def get_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    ltext = text.lower()
    letters = {}
    for i in range(0, len(ltext)):
        letter = ltext[i]
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters


main()
