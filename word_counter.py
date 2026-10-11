# Task 11: Word and Character Counter
# Name: M. Rohithanjan
# Track: Python Programming (Veda Technology Internship)


# Function to count characters with spaces and without spaces
def count_characters(text):
    total_chars = len(text)
    chars_without_spaces = len(text.replace(" ", ""))
    return total_chars, chars_without_spaces


# Function to count words using split()
def count_words(text):
    words = text.split()
    return len(words)


# Function to count sentences based on ., !, and ?
def count_sentences(text):
    sentence_count = 0
    previous_was_punct = False

    for char in text:
        if char == "." or char == "!" or char == "?":
            # Count consecutive punctuation like "..." or "?!" as one sentence end
            if not previous_was_punct:
                sentence_count = sentence_count + 1
                previous_was_punct = True
        else:
            previous_was_punct = False

    return sentence_count


# Function to count spaces in the paragraph
def count_spaces(text):
    space_count = text.count(" ")
    return space_count


# Function to display all calculated statistics
def show_results(text):
    total_chars, chars_without_spaces = count_characters(text)
    word_count = count_words(text)
    sentence_count = count_sentences(text)
    space_count = count_spaces(text)

    print("\n--- Text Analysis Results ---")
    print("Paragraph:")
    print(text)
    print("-" * 29)
    print("Total characters (with spaces) :", total_chars)
    print("Characters (without spaces)    :", chars_without_spaces)
    print("Total words                    :", word_count)
    print("Total sentences                :", sentence_count)
    print("Total spaces                   :", space_count)
    print("-" * 29)


def main():
    sample_text = (
        "Python is a simple and powerful programming language. "
        "It is great for beginners who want to learn coding! "
        "Can we use Python to process text and count words? "
        "Yes, string methods make text analysis very easy."
    )

    print("============================================================")
    print("   Word and Character Counter - Task 11 by M. Rohithanjan   ")
    print("============================================================")

    while True:
        print("\nMenu:")
        print("1. Enter my own paragraph")
        print("2. Use the sample paragraph")
        print("3. Exit")

        try:
            choice = input("\nEnter your choice (1-3): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting program. Goodbye!")
            break

        if choice == "1":
            try:
                text = input("\nEnter your paragraph:\n")
            except (EOFError, KeyboardInterrupt):
                print("\nInput cancelled.")
                continue

            # Check if the user entered nothing or only spaces
            if text.strip() == "":
                print("\nPlease enter a valid paragraph! Input cannot be empty or just spaces.")
            else:
                show_results(text)

        elif choice == "2":
            print("\nUsing the sample paragraph...")
            show_results(sample_text)

        elif choice == "3":
            print("\nThank you for using the Word and Character Counter. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
