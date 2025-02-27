from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    try:
        text = get_book_text(book)
        num_words = count_words(text)
        num_of_chars = count_chars(text)
        sorted_chars = sort_dict(num_of_chars)
        
        char_count_str = "\n".join(
            [str(char).strip("{}").replace("'", "") for char in sorted_chars if ' ' not in char]
        )
        
        print(f"""
============ BOOKBOT ============
Analyzing book found at {book}
----------- Word Count ----------
Found {num_words} total words.
--------- Character Count -------
{char_count_str}
============= END ===============
""")
    except FileNotFoundError:
        print(f"Error: Could not find book at {book}")

main()