#main() is a function that takes the assigns the PATH, assigns function 'text' to read the PATH, and then prints 'text' to console.
def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

#get_book_text() takes the PATH to file, and returns the full set of text. 
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()