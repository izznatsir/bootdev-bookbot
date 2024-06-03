def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        words_count = count_words(text)
        chars_count = count_chars(text)
        chars_count_list = char_count_dict_to_sorted_list(chars_count)

        print("---Begin report of books/frankenstein.txt ---")
        print(f"{words_count} words found in the document:")
        print()

        for char_count in chars_count_list:
            print(f"The '{char_count["char"]}' character was found {char_count["count"]} times")
        
        print()
        print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def char_count_dict_to_sorted_list(char_count_dict):
    list = []
    for char in char_count_dict:
        if not char.isalpha():
            continue
        count = char_count_dict[char]
        list.append({
            "char": char,
            "count": count
        })
    list.sort(reverse=True, key=sort_on)
    return list

def count_words(text):
    return len(text.split())

def count_chars(text):
    count = {}
    for char in text:
        char = char.lower()
        if not (char in count):
            count[char] = 0
        count[char] += 1
    return count

main()
