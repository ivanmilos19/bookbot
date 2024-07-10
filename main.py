def main():
    path = 'books/frankenstein.txt'
    text = get_book_text(path)
    word_count = get_word_count(text)
    letter_occurrences = get_letter_occurrences(text)
    print(f'Word count: {word_count}')
    print(f'Letter occurrences: {letter_occurrences}')



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

def test(text):
    for c in text:
        print(c)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()