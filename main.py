import sys

if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
        return file_contents

from stats import words
from stats import get_letter_count
from stats import sort_letter_count

def main():
    book_text=get_book_text(sys.argv[1])
    word_count=words(book_text)
    letter_count=get_letter_count(book_text)
    sorted_letters=sort_letter_count(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in sorted_letters:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
main()