from stats import get_num_words,get_char_count
def get_book_text(filePath):
    with open(filePath,'r', encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    return text

if __name__ == "__main__":
    text=main()
    print(f"Found {get_num_words(text)} total words")
    char_frequency= get_char_count(text)
    print(char_frequency)
   