from stats import words_counter, count_chars,sorted_output
import sys

def get_book_text (file_path):
    file_contents = None
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        book = get_book_text(sys.argv[1])
        num_of_words = words_counter(book)
        print(f"Found {num_of_words} total words")
        print("--------- Character Count -------")
        dict = count_chars(book)
        sorted_output(dict)
        print("============= END ===============")
        
    
    
main()
