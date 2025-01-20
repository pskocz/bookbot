def main():
    subject = "books/frankenstein.txt"
    text_to_parse = read_book(subject)
    letters = count_letters(text_to_parse)    
    words = count_words(text_to_parse)

    print(f"--- Begin raport of {subject} ---")
    print(f"{words} words found in the document")
    print()
    pretty_print(letters)
    print(f"--- End raport ---")

def read_book(book_name):
    with open(book_name) as f:
        file_contents = f.read()
    return file_contents

def count_words(text_to_parse):
    w_count = 0
    words = text_to_parse.split()
    w_count = len(words)
    return w_count
    
def count_letters(text_to_parse):
    l_count = {}
    string = text_to_parse.lower()
    lista = list(string)
    for elem in lista:
        if elem.isalpha():
            try:
                l_count[elem] += 1
            except KeyError:
                l_count[elem] = 1
    return l_count

def sort_on(dict):
    return dict['num']

def pretty_print(input):
    result_list = []  
    result = {}
    for k, v in input.items():
        result = ({"name": k, "num": v})
        result_list.append(result)
    result_list.sort(reverse=True, key=sort_on)
    for i in result_list:
        print(f"The '{i['name']}' character was found {i['num']} times")

main()
