from stats import main
import sys

def print_report(path, character, count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {count} total words")

    print("--------- Character Count -------")
    for char in character:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")

    print("============= END ===============")

if  len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path, character, count = main(sys.argv[1])
print_report(path, character, count)
