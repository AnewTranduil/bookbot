def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    print(text)
    words_count = count_words(text)
    print(words_count)


def get_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


main()
