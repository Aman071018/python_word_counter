def count_words(text):

    words = text.split()
    
    return len(words)

def main():
    print("Welcome to the Word Counter!")
    print("Please enter a sentence or paragraph:")

    # user input
    user_input = input("> ")
    
    # Check if the input is empty
    if not user_input.strip():
        print("Error: Empty input. Please enter some text.")
        return
    
    # Count words
    word_count = count_words(user_input)
    
    # Display word count
    print(f"Number of words: {word_count}")

if __name__ == "__main__":
    main()