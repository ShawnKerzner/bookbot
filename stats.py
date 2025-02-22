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

def sort_char_counts(char_counts):
    # Convert dictionary into a list of single key dictionaries
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({char: count})

    # Define a sorting key to extract the count value from each dictionary
    def get_count(single_dict):
        return list(single_dict.values())[0]
    
    # Sort the list of dictionaries by count, in descending order
    char_list.sort(key=get_count, reverse=True)

    return char_list