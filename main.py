def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words_count = count_words(text)
    letters = count_letters(text)
    pletters = pretty_letters(letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print("")
    for letter in pletters:
        print(f"The '{letter["name"]}' character was found {letter["num"]} times")
    print("--- End report ---")


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


def sort_on(dict):
    return dict["num"]


def pretty_letters(letters):
    p_letters = []
    for letter in letters:
        if letter.isalpha():
            letter_dict = {
                "name": letter,
                "num": letters[letter]
            }
            p_letters.append(letter_dict)
    p_letters.sort(reverse=True, key=sort_on)
    return p_letters


main()
