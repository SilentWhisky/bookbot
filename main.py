from stats import word_count
from stats import count_char
from stats import sort

def main ():
    book = "books/frankenstein.txt"
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
    
main()
    