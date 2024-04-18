#main() is a function that takes the assigns the PATH, assigns function 'text' to read the PATH, and then prints 'text' to console.
def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path) #call - access to document function
    num_words = get_num_words(text) #call - num of words function
    letter_count = get_letter_count(text) #call - character dictionary function
    print(letter_count)
    
#solution splits into another function "get_num_words". Code amended below due to solution clarity
def get_num_words(text):
    words = text.split()
    return len(words)
    #len() used over count += 1 for clarity and simplicity. 

#get_book_text() takes the PATH to file, and returns the full set of text. 
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
#Next Assignment: count number of each letter in total over entire document. Care for uppercase. end result = print a dictionary of values. 
def get_letter_count(text):
    letter_list = {}
    for characters in text:
        lowered_characters = characters.lower()
        if lowered_characters not in letter_list:
            letter_list[lowered_characters]=1
        else:
            letter_list[lowered_characters]+=1
    return letter_list

#next assignment: Condense previous two functions (char dict and num words) into a report!

#main() calls the above function as the primary end usage of the program.    
main()