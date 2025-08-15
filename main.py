import sys
from stats import get_num_words, get_num_char, get_list_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = get_num_words(sys.argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    num_char = get_list_dict(sys.argv[1])
    print("--------- Character Count -------")
    for i in range(0, len(num_char)):
        print(f"{num_char[i]["char"]}: {num_char[i]["count"]}")
    print("============= END ===============")

main()
