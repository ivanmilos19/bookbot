def main():
    path = 'books/frankenstein.txt'
    text = get_book_text(path)
    word_count = get_word_count(text)
    letter_occurences = get_letter_occurrences(text)    
    sorted_letter_occurences = chars_dict_to_list(letter_occurences)
    print(f'--- Begin report of {path} ---')
    print(f'Word count: {word_count}')
    print()

    for item in sorted_letter_occurences:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def sort_on(dict):
    return dict["num"]

def chars_dict_to_list(dict):
    list = []
    for key in dict:
        list.append({"char": key, "num": dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list

def get_word_count(text):
    return len(text.split())

def get_letter_occurrences(text):
    letter_occurrences = {}
    for char in text:
        lowered = char.lower()
        if lowered in letter_occurrences:
            letter_occurrences[lowered] += 1
        else:
            letter_occurrences[lowered] = 1
    return letter_occurrences
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()