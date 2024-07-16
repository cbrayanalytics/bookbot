def main():
    book = "books/frankenstein.txt"
    content = open_book(book)
    print(f"--- Begin report of {book} ---")
    count = count_words(content)
    print(f"{count} words found in the document")
    print("")
    sorted_char_count = sort_chars(count_chars(content))
    for key, value in sorted_char_count:
        print(f"The '{key}' was found {value} times")
    print("--- End report ---")


def open_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def count_words(book):
    words = book.split()
    count = len(words)
    return count


def count_chars(book):
    char_dict = {}
    for char in book.lower():
        if char in char_dict.keys():
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def return_alpha(dict):
    subset_dict = {key: value for key, value in dict.items() if key.isalpha()}
    return subset_dict


def sort_chars(dict):
    alpha_dict = return_alpha(dict)
    sorted_char_counts = sorted(
        alpha_dict.items(), key=lambda item: item[1], reverse=True
    )
    return sorted_char_counts


main()
