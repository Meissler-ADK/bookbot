from stats import word_counter, get_letters_in_text, sorted_letter_count
import sys

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def display_counts(path, word_count, letter_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in letter_count:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    file_contents = get_book_text(path)
    total_words = word_counter(file_contents)
    total_letters = get_letters_in_text(file_contents)
    sorted_letters = sorted_letter_count(total_letters)
    display_counts(path, total_words, sorted_letters)

main()