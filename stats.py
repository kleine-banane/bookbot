def get_book_text(path):
    with open(path) as book:
        text = book.read()
    return text

def count_words(text):
    words = text.split()
    return len(words) 

def count_chars(text):
    number_of_chars = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in number_of_chars:
            number_of_chars[char] += 1
        else: 
            number_of_chars[char] = 1
    return number_of_chars

def sort_dict(dict):
    sorted_list = []
    for key, value in sorted(dict.items(), key=lambda item: item[1], reverse=True):
        sorted_list.append({key:value})
    del sorted_list[0]
    return sorted_list
