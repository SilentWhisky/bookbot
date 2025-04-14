from stats import word_count


def main ():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    count = word_count(text)
    print (f"{count} words found in the document")


def get_book_text (filepath):

    with open(filepath) as f:
        return (f.read())
    
main()
    