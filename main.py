def main():
    book_path = "/home/galileos_journey/workspace/github.com/Gravitation-Force/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = times_for_charecter(text)
    char_count.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    for item in char_count:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def times_for_charecter(text):
    lowered_string = text.lower()
    characters = {}
    for character in lowered_string:
        if character.isalpha() == True:
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
    character_list = [{"char": char, "num": count} for char, count in characters.items()]
    return character_list

def sort_on(char_count):
    return char_count["num"]

main()



