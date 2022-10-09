STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
PUNCTUATION = [
    '?', '.', '.', '!', '_', ':', '"', "'",
]
# Function to sort words by frequency
def print_word_freq(file):
# Open the file
    with open(file, "r") as file:
# Read the file
        text_content = file.read()
# Remove punctuation
    for char in text_content:
        if char in PUNCTUATION:
            text_content = text_content.replace(char, "")
            return text_content
# Split the content to separate words into a list 
    text_content = text_content.split()
# Change all the words to lower case
    text_content = [word.lower() for word in text_content]
# Take out all the 'STOP' words
    for word in text_content:
        if word in STOP_WORDS:
            text_content.remove(word)
# Separate the word and the counter into dictionary's 
    counter_dictionary = ()
    word_dictionary = ()
# define 'counter' and 'word' with 'integer' or '*' 
    for word in text_content:
        if word in counter_dictionary and word_dictionary:
            counter_dictionary[word] += 1
            word_dictionary[word] += '*'
        else:
            counter_dictionary[word] += 1
            word_dictionary[word] += '*'
# Sort the words from highest to lowest
# Lambda function arranges tuple into a value
    sorted_list = sorted(counter_dictionary.items())
    key = lambda tuple: tuple[1]

    sorted_dict = dict(sorted_list)

    for key in sorted_dict:
        print(f"{key} , {len(word_dictionary[key])} {word_dictionary[key]}")

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
