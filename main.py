import sys
from stats import count_words, count_characters, sort_char_counts

# Main function to process the book and display results
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book")
        sys.exit(1)

    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        file_contents = f.read()
        # Count words and print the result
        word_count = count_words(file_contents)
        print(f"Found {word_count} total words")

        #Count characters and print the result
        char_count = count_characters(file_contents)
        sorted_char = sort_char_counts(char_count)
        
        print("--------- Character Count -------")

        for char_dict in sorted_char:
            for char, count in char_dict.items():
                print(f"{char}: {count}")


# Run the main function
if __name__ == "__main__":
    main()
