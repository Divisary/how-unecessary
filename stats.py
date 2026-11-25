def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    words = book.split()
    return (len(words))

def char_count(book):
    char_dict = {}
    lower_book = book.lower()

    for char in lower_book:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(book: tuple[str, int]) -> int:
    return book[1]

def chars_dict_to_sorted_list(char_dict: dict[str, int]) ->  list[tuple[str, int]]:
    char_list = []
    new_char_list = []
    for char in char_dict:
        char_tuple = ()
        char_tuple = (char,) + (char_dict[char],)
        char_list.append(char_tuple)

    for i in char_list:
        new_char_list.append(i)
    sorted_list = sorted(new_char_list, reverse=True, key=sort_on)
    return sorted_list

def main(path):
    book = get_book_text(path)
    char_dict = char_count(book)
    num_words = (word_count(book))
    return path, chars_dict_to_sorted_list(char_dict), num_words
