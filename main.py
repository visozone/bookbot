def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_chars_counters(text)
    get_characters_report(book_path, num_words, chars)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_chars_counters(text):
    lowercase_text = text.lower()
    chars = dict()

    for i in lowercase_text:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1

    return(chars)

def get_characters_report(book_path, num_words, chars):
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    characters_list = list()

    for char in chars:
        if char.isalpha():
            tuple = (char, chars[char])
            characters_list.append(tuple)
    
    characters_list.sort()

    for char in characters_list:
        print(f"The '{char[0]}' character was found {char[1]} times")

    print("--- End report ---")


main()