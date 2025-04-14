from stats import word_count
from stats import count_char


def main ():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    count = word_count(text)
    print (f"{count} words found in the document")
    print (count_char(text))

def get_book_text (filepath):

    with open(filepath) as f:
        return (f.read())
    
main()
    