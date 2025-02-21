# Function to count words in the text
def count_words(text):
    words = text.split()
    return len(words)

#Function to count characters in the text
def count_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

# Main function to process the book and display results
def main():
    #Path to the book file
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

        # Count words and print the result
        word_count = count_words(file_contents)
        print(word_count)

        #Count characters and print the result
        char_count = count_characters(file_contents)
        print(char_count)

# Test the count characters function with an example string
test_string = "Hello, World!"
test_result = count_characters(test_string)
print(test_result)

# Run the main function
if __name__ == "__main__":
    main()