#main() is a function that takes the assigns the PATH, assigns function 'text' to read the PATH, and then prints 'text' to console.
def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path) #call - access to document function
    num_words = get_num_words(text) #call - num of words function
    letter_count = get_letter_count(text) #call - character dictionary function
    #assignment "print a report", report has beginning and end text, lists word count, space, and then text of alphabet character count line by line.
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document.")
    print("")
    alph_list = letter_list(text)
    for dict_item in alph_list:
        for character, count in dict_item.items():
            print(f"The '{character}' character was found {count} times.")
    print("--- End report ---")
    
#function to get word count in text
def get_num_words(text):
    words = text.split()
    return len(words)
    #len() used over count += 1 for clarity and simplicity. 

#function to get path to text
def get_book_text(path):
    with open(path) as f:
        return f.read()

#function to get letter count in text
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
#first convert char dict into a list of dictionaries, then sort list by number of occurences.
    #side function prior to filter out non-alphabet with ".isalpha()"
#then add to main.py, and print in report
def letter_list(text):
    def sort_on(dict_item):
        return next(iter(dict_item.values()))
    alpha_list = []
    letter_count = get_letter_count(text)
    new_list = [{k: v} for k, v in letter_count.items()]
    for dict_item in new_list:
        for key, value in dict_item.items():
            if key.isalpha():
                alpha_list.append({key: value})
    alpha_list.sort(reverse=True, key=sort_on)
    ##def sort_on(alpha_list):
        ##return alpha_list[value]
    ##alpha_list.sort(reverse=True, key=sort_on)
    return alpha_list


#main() calls the above function as the primary end usage of the program. 
#good   
main()