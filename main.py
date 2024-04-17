#main() is a function that takes the assigns the PATH, assigns function 'text' to read the PATH, and then prints 'text' to console.
def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document.")
    
#solution splits into another function "get_num_words". Code amended below due to solution clarity
def get_num_words(text):
    words = text.split()
    return len(words)
    #len() used over count += 1 for clarity and simplicity. 


#get_book_text() takes the PATH to file, and returns the full set of text. 
def get_book_text(path):
    with open(path) as f:
        return f.read()

#main() calls the above function as the primary end usage of the program.    
main()