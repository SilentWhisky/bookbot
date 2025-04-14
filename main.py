from stats import word_count
from stats import count_char
from stats import sort
import sys


def main (path):
    
    book = path
    text = get_book_text(book)
    count = word_count(text)
    dict = count_char(text)
    sorted_dict = sort(dict)

    print (f"""============ BOOKBOT ============
    Analyzing book found at {book}...
    ----------- Word Count ----------
    Found {count} total words
    --------- Character Count -------""")
    for char, num in sorted_dict:
        print (f"{char}: {num}")

def get_book_text (filepath):

    with open(filepath) as f:
        return (f.read())
    
if len(sys.argv) < 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
    